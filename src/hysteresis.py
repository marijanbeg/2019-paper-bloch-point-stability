import os
import sys
import pickle
import numpy as np
import helpers as hlp
from finmag import Simulation as Sim
from finmag.energies import Exchange, DMI, Demag, Zeeman

# geometry parameters
d = 150  # disk diameter (nm)
hb = 20  # bottom layer thickness (nm)
ht = 10  # top layer thickness (nm)
lmax = 3  # discretisation (nm)

# FeGe material parameters
Ms = 3.84e5  # magnetisation saturation (A/m)
A = 8.78e-12  # exchange energy constant (J/m)
D = 1.58e-3  # DMI constant (J/m**2)

mu0 = 4*np.pi*1e-7  # magnetic constant (N/A**2)

# initial magnetisation configuration
m_init = (0, 0, 1)

# Create an array of external fields for which the system is relaxed.
Bmax = 1  # maximum field in hysteresis (T)
dB = 0.1  # field step (T)
B_array = np.concatenate([np.arange(Bmax, -Bmax, -dB),
                          np.arange(-Bmax, Bmax+1e-12, dB)])

# Define and create results directory.
basename = 'd{}hb{}ht{}'.format(d, hb, ht)
rdir = '../results/hysteresis/{}'.format(basename)
if rdir != './' and not os.path.exists(rdir):
    os.makedirs(rdir)

# Create mesh and simulation.
mesh = hlp.disk_with_internal_boundary(d, hb, ht, lmax)
sim = Sim(mesh, Ms, unit_length=1e-9)

# Add energies.
sim.add(Exchange(A))
sim.add(DMI(hlp.D_init(D)))
sim.add(Demag())
sim.add(Zeeman((0, 0, 0)))

# Turn off precession.
sim.do_precession = False

# Initialise the system.
sim.set_m(m_init)

for state, B in enumerate(B_array):
    # Set field.
    sim.set_H_ext((0, 0, B/mu0))

    # Relax the system.
    sim.relax(stopping_dmdt=0.1)

    # Save the vtk file for visualisation.
    pvd_filename = '{}/state_{}.pvd'.format(rdir, state)
    sim.save_vtk(pvd_filename, overwrite=True)

    # Save the hdf5 file for data analysis.
    h5_filename = '{}/state_{}'.format(rdir, state)
    sim.llg.m_field.save_hdf5(h5_filename, 0)
    sim.llg.m_field.close_hdf5()

    # Compute values of system properties.
    data = hlp.analyse(sim.llg.m_field.f)
    pkl_filename = '{}/state_{}.pkl'.format(rdir, state)
    f = open(pkl_filename, "wb")
    pickle.dump(data, f)
    f.close()

import os
import sys
import pickle
import numpy as np
import helpers as hlp
from finmag import Simulation as Sim
from finmag.energies import Exchange, DMI, Demag

# geometry parameters
d = 150  # disk diameter (nm)
hb = 20  # bottom layer thickness (nm)
ht = 10  # top layer thickness (nm)
lmax = 3  # discretisation (nm)

# FeGe material parameters
Ms = 3.84e5  # magnetisation saturation (A/m)
A = 8.78e-12  # exchange energy constant (J/m)
D = 1.58e-3  # DMI constant (J/m**2)

# initial magnetisation configuration
m_init = (0, 0, 1)

# Define and create results directory.
basename = 'd{}hb{}ht{}'.format(d, hb, ht)
rdir = '../results/creation/{}'.format(basename)
if rdir != './' and not os.path.exists(rdir):
    os.makedirs(rdir)

# Create mesh and simulation.
mesh = hlp.disk_with_internal_boundary(d, hb, ht, lmax)
sim = Sim(mesh, Ms, unit_length=1e-9)

# Add energies.
sim.add(Exchange(A))
sim.add(DMI(hlp.D_init(D)))
sim.add(Demag())

# Set Gilbert damping to the experimental value [Beg2017].
sim.alpha = 0.28

# Initialise the system.
sim.set_m(m_init)

# time evolution
T = 500e-12  # total simulation time (s)
dt = 1e-12  # time step (s)
t_array = np.arange(0, T+dt/2, dt)
for t in t_array:
    sim.run_until(t)

    # Save the vtk file for visualisation.
    pvd_filename = '{}/t{}.pvd'.format(rdir, int(np.round(t/1e-12)))
    sim.save_vtk(pvd_filename, overwrite=True)

    # Save the hdf5 file for data analysis.
    h5_filename = '{}/t{}'.format(rdir, int(np.round(t/1e-12)))
    sim.llg.m_field.save_hdf5(h5_filename, 0)
    sim.llg.m_field.close_hdf5()

    # Compute values of system properties.
    data = hlp.analyse(sim.llg.m_field.f)
    txt_filename = '{}/t{}.txt'.format(rdir, int(np.round(t/1e-12)))
    with open(txt_filename, "wb") as f:
        f.write(str(data))

import os
import gc
import sys
import pickle
import numpy as np
import helpers as hlp
from finmag import Simulation as Sim
from finmag.energies import Exchange, DMI, Demag

# geometry parameters
d = 150  # disk diameter (nm)
hb = 20  # bottom layer thickness (nm)
lmax = 3  # discretisation (nm)

# FeGe material parameters
Ms = 3.84e5  # magnetisation saturation (A/m)
A = 8.78e-12  # exchange energy constant (J/m)
D = 1.58e-3  # DMI constant (J/m**2)

# initial magnetisation configuration
m_init = (0, 0, 1)

# We vary the thickness of the top layer.
for ht in np.arange(2, 19, 1):
    # Create mesh and simulation.
    mesh = hlp.disk_with_internal_boundary(d, hb, ht, lmax)
    sim = Sim(mesh, Ms, unit_length=1e-9)

    # Add energies. No Zeeman because the system is in zero field.
    sim.add(Exchange(A))
    sim.add(DMI(hlp.D_init(D)))
    sim.add(Demag())

    # Turn off precession to speed up simulations.
    sim.do_precession = False

    # Initialise the system.
    sim.set_m(m_init)

    # Relax the system with reduced stopping dmdt value for higher
    # precision.
    sim.relax(stopping_dmdt=0.1)

    # Define and create results directory.
    basename = 'd{}hb{}ht{}'.format(d, hb, ht)
    rdir = '../results/stability/{}'.format(basename)
    if rdir != './' and not os.path.exists(rdir):
        os.makedirs(rdir)

    # Save the vtk file for visualisation.
    pvd_filename = '{}/{}.pvd'.format(rdir, basename)
    sim.save_vtk(pvd_filename, overwrite=True)

    # Save the hdf5 file for data analysis.
    h5_filename = '{}/{}'.format(rdir, basename)
    sim.llg.m_field.save_hdf5(h5_filename, 0)
    sim.llg.m_field.close_hdf5()

    # Compute values of system properties.
    data = hlp.analyse(sim.llg.m_field.f)
    txt_filename = '{}/{}.txt'.format(rdir, basename)
    with open(txt_filename, 'w') as f:
        f.write(str(data))

    # Delete simulation object.
    sim.shutdown()
    del sim
    gc.collect()

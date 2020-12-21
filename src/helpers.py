import os
import textwrap
import numpy as np
import dolfin as df


def disk_with_internal_boundary(d, hb, ht, lmax):
    # gmsh geometry script (obtained using gmsh)
    geo_script = textwrap.dedent('""\
    lmax = DefineNumber[ $lmax$, Name "Parameters/lmax" ];
    rad = DefineNumber[ $rad$, Name "Parameters/rad" ];
    hb = DefineNumber[ $hb$, Name "Parameters/hb" ];
    ht = DefineNumber[ $ht$, Name "Parameters/ht" ];
    Point(1) = {0, 0, 0, lmax};
    Point(2) = {rad, 0, 0, lmax};
    Point(3) = {-rad, 0, 0, lmax};
    Point(4) = {0, rad, 0, lmax};
    Point(5) = {0, -rad, 0, lmax};
    Circle(1) = {4, 1, 2};
    Circle(2) = {2, 1, 5};
    Circle(3) = {5, 1, 3};
    Circle(4) = {3, 1, 4};
    Line Loop(5) = {4, 1, 2, 3};
    Ruled Surface(6) = {5};
    Extrude {0, 0, -hb} {
      Surface{6};
    }
    Extrude {0, 0, ht} {
      Surface{6};
    }
    Surface Loop(51) = {27, 15, 19, 23, 28, 45, 49, 37, 41, 50};
    """)

    # Replace parameters in the gmsh geometry script.
    geo_script = geo_script.replace('$rad$', str(d/2.))
    geo_script = geo_script.replace('$hb$', str(hb))
    geo_script = geo_script.replace('$ht$', str(ht))
    geo_script = geo_script.replace('$lmax$', str(lmax))

    # Write the geometry script to the .geo file.
    geo_filename = 'disk_with_boundary.geo'
    geo_file = open(geo_filename, 'w')
    geo_file.write(geo_script)
    geo_file.close()

    # Create a 3d mesh.
    gmsh_command = ('gmsh disk_with_boundary.geo -3 -optimize '
                    '-o disk_with_boundary.msh')
    os.system(gmsh_command)

    # Convert msh mesh format to the xml (required by dolfin).
    dc_command = 'dolfin-convert disk_with_boundary.msh disk_with_boundary.xml'
    os.system(dc_command)

    # Load the mesh and create a dolfin object.
    mesh = df.Mesh('disk_with_boundary.xml')

    # Delete all temporary files.
    os.system('rm disk_with_boundary.geo')
    os.system('rm disk_with_boundary.msh')
    os.system('rm disk_with_boundary.xml')

    return mesh


def D_init(D):
    def wrapped_function(pos):
        x, y, z = pos
        # The mesh was created so that the boundary between grains is
        # at z=0.
        if z <= 0:
            return -D
        else:
            return D
    return wrapped_function


def s_number(m, dx):
    s_density = df.dot(m, df.cross(df.Dx(m, 0), df.Dx(m, 1)))
    return 1/(4*np.pi) * df.assemble(s_density*dx)


def average(m, dx):
    # Compute volume.
    S = df.FunctionSpace(m.function_space().mesh(), 'CG', 1)
    unit_function = df.interpolate(df.Constant(1), S)
    volume = df.assemble(unit_function*dx)

    # Compute average
    mx = df.assemble(m[0]*dx)/volume
    my = df.assemble(m[1]*dx)/volume
    mz = df.assemble(m[2]*dx)/volume

    return [mx, my, mz]


def analyse(m):
    # Create two subdomains (0 and 1).
    subdomains = df.CellFunction('size_t', m.function_space().mesh(), 0)
    for cell in df.cells(m.function_space().mesh()):
        cell_midpoint = cell.midpoint()
        if cell_midpoint.z() > 0:
            subdomains[cell] = 1
    dx = df.Measure('dx')[subdomains]

    # Populate dictionary.
    data = dict()
    data['average_total'] = average(m, dx('everywhere'))
    data['average_bottom'] = average(m, dx(0))
    data['average_top'] = average(m, dx(1))
    data['S_total'] = s_number(m, dx('everywhere'))
    data['S_bottom'] = s_number(m, dx(0))
    data['S_top'] = s_number(m, dx(1))

    return data

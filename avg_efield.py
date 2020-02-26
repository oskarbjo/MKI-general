

import numpy as np

E1 = np.loadtxt(r"E:\CST\MKIcool\HV CONDITIONING DEBUGGING\deflector efield\field_data\deflector_1mm_50x50mesh.txt",skiprows=2)
# E1 = np.loadtxt(r"E:\CST\MKIcool\HV CONDITIONING DEBUGGING\deflector efield\field_data\deflector_1mm_100x150mesh.txt",skiprows=2)
# E1 = np.loadtxt(r"E:\CST\MKIcool\HV CONDITIONING DEBUGGING\deflector efield\field_data\deflector_0mm_50x50mesh.txt",skiprows=2)
# E1 = np.loadtxt(r"E:\CST\MKIcool\HV CONDITIONING DEBUGGING\deflector efield\field_data\deflector_0mm_100x150mesh.txt",skiprows=2)

E1 = np.loadtxt(r"E:\CST\MKIcool\HV CONDITIONING DEBUGGING\deflector efield\field_data\deflector_1mm_50x50mesh_2.txt",skiprows=2)
E1 = np.loadtxt(r"E:\CST\MKIcool\HV CONDITIONING DEBUGGING\deflector efield\field_data\deflector_1mm_80x80mesh.txt",skiprows=2)

# E1 = np.loadtxt(r,skiprows=2)
E1 = np.loadtxt(r"E:\CST\MKIcool\HV CONDITIONING DEBUGGING\deflector_and_ring\field_data\ring_deflector.txt",skiprows=2)

xmin = np.min(E1[:,0])*1e-3
xmax = np.max(E1[:,0])*1e-3
ymin = np.min(E1[:,1])*1e-3
ymax = np.max(E1[:,1])*1e-3
zmin = np.min(E1[:,2])*1e-3
zmax = np.max(E1[:,2])*1e-3
dV = (E1[1,0]*1e-6-E1[0,0]*1e-6)**3
V = (xmax - xmin) * (ymax - ymin) * (zmax - zmin)
E1abs=np.zeros(len(E1[:,0]))

for i in range(0,len(E1[:,0])):
    E1abs[i] = np.sqrt(np.power(E1[i,3],2) + np.power(E1[i,4],2) + np.power(E1[i,5],2))

maxInd=np.where(E1abs == np.max(E1abs))

Eavg = np.sum(E1abs)*dV/V
Emax = np.max(E1abs)
maxPos = [E1[maxInd[0][0],0],E1[maxInd[0][0],1],E1[maxInd[0][0],2]]


print('Eavg = ' + str(Eavg))
print('Emax = ' + str(Emax))
print('Emax pos = ' + str(maxPos))
print('Deflector to HV busbar transition is at [0.0, 27.0-offset, 254.1]')






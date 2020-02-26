
import numpy as np
import matplotlib.pyplot as plt


Ez_26_ring_HVbus = np.loadtxt(r"E:\CST\MKIcool\HV CONDITIONING DEBUGGING\deflector_and_ring\Predicted voltages on stripes\data\HV_at_busbar_Ez_-26.6.txt",skiprows=2)
Ez_25_ring_HVbus = np.loadtxt(r"E:\CST\MKIcool\HV CONDITIONING DEBUGGING\deflector_and_ring\Predicted voltages on stripes\data\HV_at_busbar_Ez_-25.6.txt",skiprows=2)
Eabs_26_ring_HVbus = np.loadtxt(r"E:\CST\MKIcool\HV CONDITIONING DEBUGGING\deflector_and_ring\Predicted voltages on stripes\data\HV_at_busbar_Eabs_-26.6.txt",skiprows=2)
Eabs_25_ring_HVbus = np.loadtxt(r"E:\CST\MKIcool\HV CONDITIONING DEBUGGING\deflector_and_ring\Predicted voltages on stripes\data\HV_at_busbar_Eabs_-25.6.txt",skiprows=2)

Ez_26_ring_HVbusSC = np.loadtxt(r"E:\CST\MKIcool\HV CONDITIONING DEBUGGING\deflector_and_ring\Predicted voltages on stripes\data\HV_at_busbar+SC_Ez_-26.6.txt",skiprows=2)
Ez_25_ring_HVbusSC = np.loadtxt(r"E:\CST\MKIcool\HV CONDITIONING DEBUGGING\deflector_and_ring\Predicted voltages on stripes\data\HV_at_busbar+SC_Ez_-25.6.txt",skiprows=2)
Eabs_26_ring_HVbusSC = np.loadtxt(r"E:\CST\MKIcool\HV CONDITIONING DEBUGGING\deflector_and_ring\Predicted voltages on stripes\data\HV_at_busbar+SC_Eabs_-26.6.txt",skiprows=2)
Eabs_25_ring_HVbusSC = np.loadtxt(r"E:\CST\MKIcool\HV CONDITIONING DEBUGGING\deflector_and_ring\Predicted voltages on stripes\data\HV_at_busbar+SC_Eabs_-25.6.txt",skiprows=2)


Ez_26_macor_HVbus = np.loadtxt(r"E:\CST\MKIcool\HV CONDITIONING DEBUGGING\Macor design\data\HV_at_busbar_Ez_-26.6.txt",skiprows=2)
Ez_25_macor_HVbus = np.loadtxt(r"E:\CST\MKIcool\HV CONDITIONING DEBUGGING\Macor design\data\HV_at_busbar_Ez_-25.6.txt",skiprows=2)
Eabs_26_macor_HVbus = np.loadtxt(r"E:\CST\MKIcool\HV CONDITIONING DEBUGGING\Macor design\data\HV_at_busbar_Eabs_-26.6.txt",skiprows=2)
Eabs_25_macor_HVbus = np.loadtxt(r"E:\CST\MKIcool\HV CONDITIONING DEBUGGING\Macor design\data\HV_at_busbar_Eabs_-25.6.txt",skiprows=2)

Ez_26_macor_HVbusSC = np.loadtxt(r"E:\CST\MKIcool\HV CONDITIONING DEBUGGING\Macor design\data\HV_at_busbar+SC_Ez_-26.6.txt",skiprows=2)
Ez_25_macor_HVbusSC = np.loadtxt(r"E:\CST\MKIcool\HV CONDITIONING DEBUGGING\Macor design\data\HV_at_busbar+SC_Ez_-25.6.txt",skiprows=2)
Eabs_26_macor_HVbusSC = np.loadtxt(r"E:\CST\MKIcool\HV CONDITIONING DEBUGGING\Macor design\data\HV_at_busbar+SC_Eabs_-26.6.txt",skiprows=2)
Eabs_25_macor_HVbusSC = np.loadtxt(r"E:\CST\MKIcool\HV CONDITIONING DEBUGGING\Macor design\data\HV_at_busbar+SC_Eabs_-25.6.txt",skiprows=2)

Max_Ez_along_tube_modified_macor = np.loadtxt(r"E:\CST\MKIcool\HV CONDITIONING DEBUGGING\Modified macor design\data\max_Ez_along_tube.txt",skiprows=2)
Max_Ez_along_tube_original_macor = np.loadtxt(r"E:\CST\MKIcool\HV CONDITIONING DEBUGGING\Macor design\data\max_Ez_along_tube_origina_macor.txt",skiprows=2)


Eabs_along_x_macor_chamfer = np.loadtxt(r"E:\CST\MKIcool\HV CONDITIONING DEBUGGING\Macor design\data\Eabs_along_x_macor_withmetalchamfer.txt",skiprows=2)
Eabs_along_x_macor_nochamfer = np.loadtxt(r"E:\CST\MKIcool\HV CONDITIONING DEBUGGING\Macor design\data\Eabs_along_x_macor_nometalchamfer.txt",skiprows=2)

scale = 1e6
N1=420
N1stop = 940
plt.figure()
plt.plot(Ez_26_ring_HVbus[0:N1,0],Ez_26_ring_HVbus[0:N1,1]/scale,color='blue',label='Ez along alumina tube surface')
# plt.plot(Ez_25_ring_HVbus[0:N1,0],Ez_25_ring_HVbus[0:N1,1],color='blue',linestyle='--')
plt.plot(Ez_25_ring_HVbus[N1:N1stop,0],Ez_25_ring_HVbus[N1:N1stop,1]/scale,color='blue')
# plt.plot(Ez_26_ring_HVbus[N1:N1stop,0],Ez_26_ring_HVbus[N1:N1stop,1],color='blue',linestyle='--')
p2=plt.plot(Eabs_26_ring_HVbus[0:N1,0],Eabs_26_ring_HVbus[0:N1,1]/scale,color='red',label='Eabs along alumina tube surface')
# plt.plot(Eabs_25_ring_HVbus[0:N1,0],Eabs_25_ring_HVbus[0:N1,1],color='red',linestyle='--')
plt.plot(Eabs_25_ring_HVbus[N1:N1stop,0],Eabs_25_ring_HVbus[N1:N1stop,1]/scale,color='red')
# plt.plot(Eabs_26_ring_HVbus[N1:N1stop,0],Eabs_26_ring_HVbus[N1:N1stop,1],color='red',linestyle='--')
plt.xlabel('Position along beam pipe [mm]')
plt.ylabel('E-field [kV/mm]')
plt.grid()


plt.figure()
plt.plot(Ez_26_ring_HVbusSC[0:N1,0],Ez_26_ring_HVbusSC[0:N1,1]/scale,color='blue')
# plt.plot(Ez_25_ring_HVbus[0:N1,0],Ez_25_ring_HVbus[0:N1,1],color='blue',linestyle='--')
plt.plot(Ez_25_ring_HVbusSC[N1:N1stop,0],Ez_25_ring_HVbusSC[N1:N1stop,1]/scale,color='blue')
# plt.plot(Ez_26_ring_HVbus[N1:N1stop,0],Ez_26_ring_HVbus[N1:N1stop,1],color='blue',linestyle='--')
plt.plot(Eabs_26_ring_HVbusSC[0:N1,0],Eabs_26_ring_HVbusSC[0:N1,1]/scale,color='red')
# plt.plot(Eabs_25_ring_HVbus[0:N1,0],Eabs_25_ring_HVbus[0:N1,1],color='red',linestyle='--')
plt.plot(Eabs_25_ring_HVbusSC[N1:N1stop,0],Eabs_25_ring_HVbusSC[N1:N1stop,1]/scale,color='red')
# plt.plot(Eabs_26_ring_HVbus[N1:N1stop,0],Eabs_26_ring_HVbus[N1:N1stop,1],color='red',linestyle='--')
plt.legend()
plt.xlabel('Position along beam pipe [mm]')
plt.ylabel('E-field [kV/mm]')
plt.title('Fields along alumina tube, current MKI design')
plt.grid()

N=38
Nstop = 85
plt.figure()
plt.plot(Ez_26_macor_HVbus[0:N,0],Ez_26_macor_HVbus[0:N,1]/scale,color='blue',label='Ez along alumina tube surface')
# plt.plot(Ez_25_macor_HVbus[0:N,0],Ez_25_macor_HVbus[0:N,1],color='blue',linestyle='--')
plt.plot(Ez_25_macor_HVbus[N:Nstop,0],Ez_25_macor_HVbus[N:Nstop,1]/scale,color='blue')
# plt.plot(Ez_26_macor_HVbus[N:Nstop,0],Ez_26_macor_HVbus[N:Nstop,1],color='blue',linestyle='--')
p2=plt.plot(Eabs_26_macor_HVbus[0:N,0],Eabs_26_macor_HVbus[0:N,1]/scale,color='red',label='Eabs along alumina tube surface')
# plt.plot(Eabs_25_macor_HVbus[0:N,0],Eabs_25_macor_HVbus[0:N,1],color='red',linestyle='--')
plt.plot(Eabs_25_macor_HVbus[N:Nstop,0],Eabs_25_macor_HVbus[N:Nstop,1]/scale,color='red')
# plt.plot(Eabs_26_macor_HVbus[N:Nstop,0],Eabs_26_macor_HVbus[N:Nstop,1],color='red',linestyle='--')
plt.xlabel('Position along beam pipe [mm]')
plt.ylabel('E-field [kV/mm]')
plt.grid()

plt.figure()
plt.plot(Ez_26_macor_HVbusSC[0:N,0],Ez_26_macor_HVbusSC[0:N,1]/scale,color='blue')
# plt.plot(Ez_25_macor_HVbus[0:N,0],Ez_25_macor_HVbus[0:N,1],color='blue',linestyle='--')
plt.plot(Ez_25_macor_HVbusSC[N:Nstop,0],Ez_25_macor_HVbusSC[N:Nstop,1]/scale,color='blue')
# plt.plot(Ez_26_macor_HVbus[N:Nstop,0],Ez_26_macor_HVbus[N:Nstop,1],color='blue',linestyle='--')
plt.plot(Eabs_26_macor_HVbusSC[0:N,0],Eabs_26_macor_HVbusSC[0:N,1]/scale,color='red')
# plt.plot(Eabs_25_macor_HVbus[0:N,0],Eabs_25_macor_HVbus[0:N,1],color='red',linestyle='--')
plt.plot(Eabs_25_macor_HVbusSC[N:Nstop,0],Eabs_25_macor_HVbusSC[N:Nstop,1]/scale,color='red')
# plt.plot(Eabs_26_macor_HVbus[N:Nstop,0],Eabs_26_macor_HVbus[N:Nstop,1],color='red',linestyle='--')
plt.xlabel('Position along beam pipe [mm]')
plt.ylabel('E-field [kV/mm]')
plt.legend()
plt.title('Fields along alumina tube, modified MKI design with macor support')
plt.grid()



ymax = 60
ymin = -15
plt.figure(figsize=(14, 6))
plt.plot(Ez_26_ring_HVbus[0:N1,0],Ez_26_ring_HVbus[0:N1,1]/scale,color='blue',label='Ez along alumina tube surface, original MKI design')
plt.plot(Ez_25_ring_HVbus[N1:N1stop,0],Ez_25_ring_HVbus[N1:N1stop,1]/scale,color='blue')
plt.plot(Ez_26_macor_HVbus[0:N,0],Ez_26_macor_HVbus[0:N,1]/scale,color='blue',label='Ez along alumina tube surface, macor design',linestyle='--')
plt.plot(Ez_25_macor_HVbus[N:Nstop,0],Ez_25_macor_HVbus[N:Nstop,1]/scale,color='blue',linestyle='--')
p2=plt.plot(Eabs_26_ring_HVbus[0:N1,0],Eabs_26_ring_HVbus[0:N1,1]/scale,color='red',label='Eabs along alumina tube surface, original MKI design')
plt.plot(Eabs_25_ring_HVbus[N1:N1stop,0],Eabs_25_ring_HVbus[N1:N1stop,1]/scale,color='red')
plt.plot(Eabs_26_macor_HVbus[0:N,0],Eabs_26_macor_HVbus[0:N,1]/scale,color='red',label='Eabs along alumina tube surface, macor design',linestyle='--')
plt.plot(Eabs_25_macor_HVbus[N:Nstop,0],Eabs_25_macor_HVbus[N:Nstop,1]/scale,color='red',linestyle='--')
plt.grid()
plt.xlabel('Position along beam pipe [mm]')
plt.ylabel('E-field [kV/mm]')
plt.legend()
plt.title('Fields along alumina tube surface, busbar at HV')
plt.ylim([ymin,ymax])

plt.figure(figsize=(14, 6))
plt.plot(Ez_26_ring_HVbusSC[0:N1,0],Ez_26_ring_HVbusSC[0:N1,1]/scale,color='blue',label='Ez along alumina tube surface, original MKI design')
plt.plot(Ez_25_ring_HVbusSC[N1:N1stop,0],Ez_25_ring_HVbusSC[N1:N1stop,1]/scale,color='blue')
plt.plot(Ez_26_macor_HVbusSC[0:N,0],Ez_26_macor_HVbusSC[0:N,1]/scale,color='blue',label='Ez along alumina tube surface, macor design',linestyle='--')
plt.plot(Ez_25_macor_HVbusSC[N:Nstop,0],Ez_25_macor_HVbusSC[N:Nstop,1]/scale,color='blue',linestyle='--')
p2=plt.plot(Eabs_26_ring_HVbusSC[0:N1,0],Eabs_26_ring_HVbusSC[0:N1,1]/scale,color='red',label='Eabs along alumina tube surface, original MKI design')
plt.plot(Eabs_25_ring_HVbusSC[N1:N1stop,0],Eabs_25_ring_HVbusSC[N1:N1stop,1]/scale,color='red')
plt.plot(Eabs_26_macor_HVbusSC[0:N,0],Eabs_26_macor_HVbusSC[0:N,1]/scale,color='red',label='Eabs along alumina tube surface, macor design',linestyle='--')
plt.plot(Eabs_25_macor_HVbusSC[N:Nstop,0],Eabs_25_macor_HVbusSC[N:Nstop,1]/scale,color='red',linestyle='--')
plt.grid()
plt.xlabel('Position along beam pipe [mm]')
plt.ylabel('E-field [kV/mm]')
plt.legend()
plt.title('Fields along alumina tube surface, busbar & SC at HV')
plt.ylim([ymin,ymax])


plt.figure(figsize=(14, 6))
N1=120
N2=420
N3=38
N4=12
plt.plot(Ez_26_macor_HVbusSC[N4:N3,0],Ez_26_macor_HVbusSC[N4:N3,1]/scale,color='blue',label='Ez along bottom of alumina tube surface')
plt.plot(Max_Ez_along_tube_original_macor[N1:N2,0],Max_Ez_along_tube_original_macor[N1:N2,1]/scale,color='blue',label='Highest Ez along alumina tube surface',linestyle='--')
plt.grid()
plt.xlabel('Position along beam pipe [mm]')
plt.ylabel('E-field [kV/mm]')
plt.legend()
plt.title('Fields along alumina tube surface, busbar & SC at HV')
plt.ylim([-2,2])


plt.figure(figsize=(14, 6))
plt.plot(Max_Ez_along_tube_original_macor[N1:N2,0],Max_Ez_along_tube_original_macor[N1:N2,1]/scale,color='blue',label='Highest Ez along alumina tube surface, original macor design')
plt.plot(Max_Ez_along_tube_modified_macor[N1:N2,0],Max_Ez_along_tube_modified_macor[N1:N2,1]/scale,color='blue',label='Highest Ez along alumina tube surface, modified macor design',linestyle='--')
plt.grid()
plt.xlabel('Position along beam pipe [mm]')
plt.ylabel('E-field [kV/mm]')
plt.legend()
plt.title('Fields along alumina tube surface, busbar & SC at HV')
plt.ylim([-2,2])


plt.figure(figsize=(14, 6))
plt.plot(Eabs_along_x_macor_chamfer[:,0],Eabs_along_x_macor_chamfer[:,1]/scale,label='With chamfer on metal support')
plt.plot(Eabs_along_x_macor_nochamfer[:,0],Eabs_along_x_macor_nochamfer[:,1]/scale,label='No chamfer on metal support')
plt.legend()
plt.xlabel('Position along x [mm]')
plt.ylabel('E-field [kV/mm]')
plt.grid()
plt.show()




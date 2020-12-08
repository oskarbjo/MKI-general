import numpy as np
from matplotlib import pyplot as plt

path = r"E:\CST\MKIcool\HV CONDITIONING DEBUGGING\Pavlina model Efield results\pavlina_mod_efield2.csv"
data = np.loadtxt(path,delimiter=',',unpack=True)


plt.figure()
plt.plot(data[0,:],data[1,:]/1e3)
# plt.plot(data[0,:],data[2,:]/1e3)
# plt.plot(data[0,:],data[3,:]/1e3)
# plt.plot(data[0,:],data[4,:]/1e3)
# plt.plot(data[0,:],data[5,:]/1e3)
plt.plot(data[0,:],data[6,:]/1e3)
plt.xlim([0,180])
plt.xlabel('Transverse position (radius = 28.1mm, upstream edge of macor support) [mm]')
plt.ylabel('Transverse position [kV/mm]')
plt.legend([
            'Original V2',
#             'V2 + bottom macor offset',
#             'V2 + bottom macor offset, moved screws',
#             'V2, macor end cap',
#             'V2, removed bottom macor support',
            'V2, removed bottom macor support + centered bolts'
            ])
plt.grid()
plt.show()
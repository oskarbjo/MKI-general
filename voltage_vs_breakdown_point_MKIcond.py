

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import


cond2019_Vmeas = np.array([35.64,
37.73,
35.76,
44.51,
45.64,
45.17,
45.08,
43.95,
43.31,
45.39,
46.44,
44.7,
44.58,
44.97,
46,
44.54,
44.67])

cond2019_breakdownPoint = np.array([0,
8,
11,
18,
131,
13,
40,
101,
86,
87,
116,
79,
12,
109,
96,
93,
74])


cond2020_precovid_Vmeas = np.array([47.6,
                          46.95,
                          47.55,
                          45.02,
                          43.06,
                          44.35,
                          47.67,
                          49.92,
                          51.61])

cond2020_precovid_breakdownPoint = np.array([144, 14, 149, 113, 111, 66, 93, 107, 161])

cond2020_postcovid_Vmeas = np.array([52.71,54.13, 50.05, 55.96, 55.57, 46.67, 53.65, 49.57, 50.41, 52.12, 52.71, 56.12, 55.98, 55.29, 52.36, 54.46, 55.83, 54.88, 54.74, 54.13, 51.08])

cond2020_postcovid_breakdownPoint = np.array([152, 110, 126, 11, 113, 47, 100, 130, 129, 54])



cond2019_Vmeas_HVtoGND = cond2019_Vmeas[[0,1,2,3]]
cond2019_breakdownPoint_HVtoGND = cond2019_breakdownPoint[[0,1,2,3]]
cond2020_precovid_Vmeas_HVtoGND = cond2020_precovid_Vmeas[[1,8]]
cond2020_precovid_breakdownPoint_HVtoGND = cond2020_precovid_breakdownPoint[[1,8]]
cond2020_postcovid_Vmeas_HVtoGND = cond2020_postcovid_Vmeas[0]
cond2020_postcovid_breakdownPoint_HVtoGND = cond2020_postcovid_breakdownPoint[0]

# plt.figure()
# plt.scatter(cond2019_breakdownPoint,cond2019_Vmeas,marker='o', label='2019 breakdowns, ' + str(len(cond2019_Vmeas)) + ' total')
# plt.scatter(cond2020_precovid_breakdownPoint,cond2020_precovid_Vmeas,marker='v',label='2020 pre covid breakdowns, ' + str(len(cond2020_precovid_Vmeas)) + ' total')
# plt.scatter(cond2020_postcovid_breakdownPoint,cond2020_postcovid_Vmeas,marker='v',label='2020 post covid breakdowns, ' + str(len(cond2020_postcovid_Vmeas)) + ' total')
# plt.xlabel('Point of breakdown, time from input [ns]')
# plt.ylabel('Vmeas [kV]')
# plt.title('MKI cool (MKIMA08-T11) breakdowns')
# plt.xlim([0, 180])
# plt.ylim([36,60])
# plt.grid()
# plt.legend()


plt.figure()
plt.scatter(np.arange(0,len(cond2019_Vmeas)),cond2019_Vmeas, label='2019 breakdowns' )
plt.scatter(np.arange(len(cond2019_Vmeas),len(cond2019_Vmeas)+len(cond2020_precovid_Vmeas)),cond2020_precovid_Vmeas, label='2020 pre covid breakdowns')
plt.scatter(np.arange(len(cond2019_Vmeas)+len(cond2020_precovid_Vmeas),len(cond2019_Vmeas)+len(cond2020_precovid_Vmeas)+len(cond2020_postcovid_Vmeas)),cond2020_postcovid_Vmeas, label='2020 post covid breakdowns')
plt.plot([0,46],[56.1,56.1],linestyle='--',linewidth=2,color='red')
plt.xlabel('Breakdown number')
plt.ylabel('Vmeas [kV]')
plt.xlim([0,46])
plt.ylim([35, 60])
plt.legend()
plt.grid()

plt.figure()
plt.scatter(cond2019_breakdownPoint_HVtoGND,cond2019_Vmeas_HVtoGND, label='2019 breakdowns')
plt.scatter(cond2020_precovid_breakdownPoint_HVtoGND,cond2020_precovid_Vmeas_HVtoGND, label='2020 pre covid breakdowns')
plt.scatter(cond2020_postcovid_breakdownPoint_HVtoGND,cond2020_postcovid_Vmeas_HVtoGND, label='2020 post covid breakdowns')
plt.xlabel('Breakdown time from input [ns]')
plt.ylabel('Vmeas [kV]')
# plt.xlim([0,40])
plt.ylim([35, 60])
plt.legend()
plt.grid()



plt.show()
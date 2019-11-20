import numpy as np
import matplotlib.pyplot as plt



CPU_DW_ref_path=r"\\cern.ch\dfs\Users\o\objorkqv\Documents\My Music\REF_RawWaveform_MKI.867.IPOC.CPU.DW_06.11.19@13h52m02s.csv"
CPU_DW_ref = f=np.loadtxt(CPU_DW_ref_path,delimiter=',',skiprows=4,unpack=True,usecols=np.arange(0,2))
CPU_UP_ref_path=r"\\cern.ch\dfs\Users\o\objorkqv\Documents\My Music\REF_RawWaveform_MKI.867.IPOC.CPU.UP_06.11.19@13h52m02s.csv"
CPU_UP_ref = f=np.loadtxt(CPU_UP_ref_path,delimiter=',',skiprows=4,unpack=True,usecols=np.arange(0,2))
IM_ref_path=r"\\cern.ch\dfs\Users\o\objorkqv\Documents\My Music\REF_RawWaveform_MKI.867.IPOC.IM_06.11.19@13h52m02s.csv"
IM_ref = f=np.loadtxt(IM_ref_path,delimiter=',',skiprows=4,unpack=True,usecols=np.arange(0,2))



CPU_DW_1_path=r"\\cern.ch\dfs\Users\o\objorkqv\Documents\My Music\RawWaveform_MKI.867.IPOC.CPU.DW_30.10.19@05h04m23s.csv"
CPU_DW_1 = f=np.loadtxt(CPU_DW_1_path,delimiter=',',skiprows=4,unpack=True,usecols=np.arange(0,2))
CPU_UP_1_path=r"\\cern.ch\dfs\Users\o\objorkqv\Documents\My Music\RawWaveform_MKI.867.IPOC.CPU.UP_30.10.19@05h04m23s.csv"
CPU_UP_1 = f=np.loadtxt(CPU_UP_1_path,delimiter=',',skiprows=4,unpack=True,usecols=np.arange(0,2))
IM_1_path=r"\\cern.ch\dfs\Users\o\objorkqv\Documents\My Music\RawWaveform_MKI.867.IPOC.IM_30.10.19@05h04m23s.csv"
IM_1 = f=np.loadtxt(IM_1_path,delimiter=',',skiprows=4,unpack=True,usecols=np.arange(0,2))

CPU_DW_2_path=r"\\cern.ch\dfs\Users\o\objorkqv\Documents\My Music\RawWaveform_MKI.867.IPOC.CPU.DW_05.11.19@05h19m56s.csv"
CPU_DW_2 = f=np.loadtxt(CPU_DW_2_path,delimiter=',',skiprows=4,unpack=True,usecols=np.arange(0,2))
CPU_UP_2_path=r"\\cern.ch\dfs\Users\o\objorkqv\Documents\My Music\RawWaveform_MKI.867.IPOC.CPU.UP_05.11.19@05h19m56s.csv"
CPU_UP_2 = f=np.loadtxt(CPU_UP_2_path,delimiter=',',skiprows=4,unpack=True,usecols=np.arange(0,2))
IM_2_path=r"\\cern.ch\dfs\Users\o\objorkqv\Documents\My Music\RawWaveform_MKI.867.IPOC.IM_05.11.19@05h19m56s.csv"
IM_2 = f=np.loadtxt(IM_2_path,delimiter=',',skiprows=4,unpack=True,usecols=np.arange(0,2))

CPU_DW_3_path=r"\\cern.ch\dfs\Users\o\objorkqv\Documents\My Music\RawWaveform_MKI.867.IPOC.CPU.DW_05.11.19@11h18m07s.csv"
CPU_DW_3 = f=np.loadtxt(CPU_DW_3_path,delimiter=',',skiprows=4,unpack=True,usecols=np.arange(0,2))
CPU_UP_3_path=r"\\cern.ch\dfs\Users\o\objorkqv\Documents\My Music\RawWaveform_MKI.867.IPOC.CPU.UP_05.11.19@11h18m07s.csv"
CPU_UP_3 = f=np.loadtxt(CPU_UP_3_path,delimiter=',',skiprows=4,unpack=True,usecols=np.arange(0,2))
IM_3_path=r"\\cern.ch\dfs\Users\o\objorkqv\Documents\My Music\RawWaveform_MKI.867.IPOC.IM_05.11.19@11h18m07s.csv"
IM_3 = f=np.loadtxt(IM_3_path,delimiter=',',skiprows=4,unpack=True,usecols=np.arange(0,2))

CPU_DW_4_path=r"\\cern.ch\dfs\Users\o\objorkqv\Documents\My Music\RawWaveform_MKI.867.IPOC.CPU.DW_05.11.19@21h06m42s.csv"
CPU_DW_4 = f=np.loadtxt(CPU_DW_4_path,delimiter=',',skiprows=4,unpack=True,usecols=np.arange(0,2))
CPU_UP_4_path=r"\\cern.ch\dfs\Users\o\objorkqv\Documents\My Music\RawWaveform_MKI.867.IPOC.CPU.UP_05.11.19@21h06m42s.csv"
CPU_UP_4 = f=np.loadtxt(CPU_UP_4_path,delimiter=',',skiprows=4,unpack=True,usecols=np.arange(0,2))
IM_4_path=r"\\cern.ch\dfs\Users\o\objorkqv\Documents\My Music\RawWaveform_MKI.867.IPOC.IM_05.11.19@21h06m42s.csv"
IM_4 = f=np.loadtxt(IM_4_path,delimiter=',',skiprows=4,unpack=True,usecols=np.arange(0,2))

CPU_DW_5_path=r"\\cern.ch\dfs\Users\o\objorkqv\Documents\My Music\RawWaveform_MKI.867.IPOC.CPU.DW_06.11.19@13h52m16s.csv"
CPU_DW_5 = f=np.loadtxt(CPU_DW_5_path,delimiter=',',skiprows=4,unpack=True,usecols=np.arange(0,2))
CPU_UP_5_path=r"\\cern.ch\dfs\Users\o\objorkqv\Documents\My Music\RawWaveform_MKI.867.IPOC.CPU.UP_06.11.19@13h52m16s.csv"
CPU_UP_5 = f=np.loadtxt(CPU_UP_5_path,delimiter=',',skiprows=4,unpack=True,usecols=np.arange(0,2))
IM_5_path=r"\\cern.ch\dfs\Users\o\objorkqv\Documents\My Music\RawWaveform_MKI.867.IPOC.IM_06.11.19@13h52m16s.csv"
IM_5 = f=np.loadtxt(IM_5_path,delimiter=',',skiprows=4,unpack=True,usecols=np.arange(0,2))

CPU_DW_6_path=r"\\cern.ch\dfs\Users\o\objorkqv\Documents\My Music\2019-11-07\RawWaveform_MKI.867.IPOC.CPU.DW_07.11.19@19h16m42s.csv"
CPU_DW_6 = f=np.loadtxt(CPU_DW_6_path,delimiter=',',skiprows=4,unpack=True,usecols=np.arange(0,2))
CPU_UP_6_path=r"\\cern.ch\dfs\Users\o\objorkqv\Documents\My Music\2019-11-07\RawWaveform_MKI.867.IPOC.CPU.UP_07.11.19@19h16m42s.csv"
CPU_UP_6 = f=np.loadtxt(CPU_UP_6_path,delimiter=',',skiprows=4,unpack=True,usecols=np.arange(0,2))
IM_6_path=r"\\cern.ch\dfs\Users\o\objorkqv\Documents\My Music\2019-11-07\RawWaveform_MKI.867.IPOC.IM_07.11.19@19h16m42s.csv"
IM_6 = f=np.loadtxt(IM_6_path,delimiter=',',skiprows=4,unpack=True,usecols=np.arange(0,2))



plt.figure()
p1=plt.plot(CPU_DW_1[0,:],CPU_DW_1[1,:],color='blue')
plt.plot(CPU_UP_1[0,:],CPU_UP_1[1,:],color='red', label='_nolegend_')
plt.plot(IM_1[0,:],IM_1[1,:],color='green', label='_nolegend_')
p2=plt.plot(CPU_DW_ref[0,:],CPU_DW_ref[1,:],color='blue',linestyle='--')
plt.plot(CPU_UP_ref[0,:],CPU_UP_ref[1,:],color='red',linestyle='--', label='_nolegend_')
plt.plot(IM_ref[0,:],IM_ref[1,:],color='green',linestyle='--', label='_nolegend_')
plt.xlim([51,55])
plt.legend(['Breakdown','Reference'])
plt.grid()
plt.title('30 October 05:04:23')


plt.figure()
p1=plt.plot(CPU_DW_2[0,:],CPU_DW_2[1,:],color='blue')
plt.plot(CPU_UP_2[0,:],CPU_UP_2[1,:],color='red', label='_nolegend_')
plt.plot(IM_2[0,:],IM_2[1,:],color='green', label='_nolegend_')
p2=plt.plot(CPU_DW_ref[0,:],CPU_DW_ref[1,:],color='blue',linestyle='--')
plt.plot(CPU_UP_ref[0,:],CPU_UP_ref[1,:],color='red',linestyle='--', label='_nolegend_')
plt.plot(IM_ref[0,:],IM_ref[1,:],color='green',linestyle='--', label='_nolegend_')
plt.xlim([51,55])
plt.legend(['Breakdown','Reference'])
plt.grid()
plt.title('5 November 05:19:56')

plt.figure()
p1=plt.plot(CPU_DW_3[0,:],CPU_DW_3[1,:],color='blue')
plt.plot(CPU_UP_3[0,:],CPU_UP_3[1,:],color='red', label='_nolegend_')
plt.plot(IM_3[0,:],IM_3[1,:],color='green', label='_nolegend_')
p2=plt.plot(CPU_DW_ref[0,:],CPU_DW_ref[1,:],color='blue',linestyle='--')
plt.plot(CPU_UP_ref[0,:],CPU_UP_ref[1,:],color='red',linestyle='--', label='_nolegend_')
plt.plot(IM_ref[0,:],IM_ref[1,:],color='green',linestyle='--', label='_nolegend_')
plt.xlim([51,55])
plt.legend(['Breakdown','Reference'])
plt.grid()
plt.title('5 November 11:18:07')

plt.figure()
p1=plt.plot(CPU_DW_4[0,:],CPU_DW_4[1,:],color='blue')
plt.plot(CPU_UP_4[0,:],CPU_UP_4[1,:],color='red', label='_nolegend_')
plt.plot(IM_4[0,:],IM_4[1,:],color='green', label='_nolegend_')
p2=plt.plot(CPU_DW_ref[0,:],CPU_DW_ref[1,:],color='blue',linestyle='--')
plt.plot(CPU_UP_ref[0,:],CPU_UP_ref[1,:],color='red',linestyle='--', label='_nolegend_')
plt.plot(IM_ref[0,:],IM_ref[1,:],color='green',linestyle='--', label='_nolegend_')
plt.xlim([51,55])
plt.legend(['Breakdown','Reference'])
plt.grid()
plt.title('5 November 21:06:42')

plt.figure()
p1=plt.plot(CPU_DW_5[0,:],CPU_DW_5[1,:],color='blue')
plt.plot(CPU_UP_5[0,:],CPU_UP_5[1,:],color='red', label='_nolegend_')
plt.plot(IM_5[0,:],IM_5[1,:],color='green', label='_nolegend_')
p2=plt.plot(CPU_DW_ref[0,:],CPU_DW_ref[1,:],color='blue',linestyle='--')
plt.plot(CPU_UP_ref[0,:],CPU_UP_ref[1,:],color='red',linestyle='--', label='_nolegend_')
plt.plot(IM_ref[0,:],IM_ref[1,:],color='green',linestyle='--', label='_nolegend_')
plt.xlim([51,55])
plt.legend(['Breakdown','Reference'])
plt.grid()
plt.title('6 November 13:52:02')


plt.figure()
p1=plt.plot(CPU_DW_6[0,:],CPU_DW_6[1,:],color='blue')
plt.plot(CPU_UP_6[0,:],CPU_UP_6[1,:],color='red', label='_nolegend_')
plt.plot(IM_6[0,:],IM_6[1,:],color='green', label='_nolegend_')
p2=plt.plot(CPU_DW_ref[0,:],CPU_DW_ref[1,:],color='blue',linestyle='--')
plt.plot(CPU_UP_ref[0,:],CPU_UP_ref[1,:],color='red',linestyle='--', label='_nolegend_')
plt.plot(IM_ref[0,:],IM_ref[1,:],color='green',linestyle='--', label='_nolegend_')
plt.xlim([51,55])
plt.legend(['Breakdown','Reference'])
plt.grid()
plt.title('7 November 19:16:42')


plt.show()



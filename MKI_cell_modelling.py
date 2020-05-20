import numpy as np
import matplotlib.pyplot as plt
import signal_toolbox


path1 = r"E:\CST\MKIcool\Full cell model\full wave\full cell\with beam screen\S21.txt"
s21_fullwave = np.loadtxt(path1,skiprows=2)

path12 = r"E:\CST\MKIcool\Full cell model\full wave\full cell\with beam screen\S21_boundaries_further.txt"
s21_fullwave_2 = np.loadtxt(path12,skiprows=2)

path2 = r"E:\CST\MKIcool\Full cell model\Circuit equivalent\S21.txt"
s21_circuitmodel = np.loadtxt(path2,skiprows=2)

path3 = r"E:\CST\MKIcool\Full cell model\Circuit equivalent\S21_further_boundaries.txt"
s21_circuitmodel_2 = np.loadtxt(path3,skiprows=2)

path4 = r"E:\CST\MKIcool\Full cell model\full wave\full cell\with beam screen 5cells\S21_5cells_fullwave.txt"
s21_FW_5cells = np.loadtxt(path4,skiprows=2)

path5 = r"E:\CST\MKIcool\Full cell model\Circuit equivalent\S21_5cells_CE.txt"
s21_CE_5cells = np.loadtxt(path5,skiprows=2)


path6 = r"E:\CST\MKIcool\Full cell model\full wave\full cell\with beam screen 5cells\S21_5cells_mid_cell.txt"
s21_5cells_mid_FW = np.loadtxt(path6,skiprows=2)

path7 = r"E:\CST\MKIcool\Full cell model\full wave\full cell\with beam screen 5cells\S21_5cells_end_cell.txt"
s21_5cells_end_FW = np.loadtxt(path7,skiprows=2)

path8 = r"E:\CST\MKIcool\Full cell model\Circuit equivalent\S21_5cells_mid_cell.txt"
s21_5cells_mid_CE = np.loadtxt(path8,skiprows=2)

path9 = r"E:\CST\MKIcool\Full cell model\Circuit equivalent\S21_5cells_end_cell_ver2.txt"
s21_5cells_end_CE = np.loadtxt(path9,skiprows=2)

path10 = r"E:\CST\MKIcool\Full cell model\Circuit equivalent\S21_2cells.txt"
s21_2cells_CE = np.loadtxt(path10,skiprows=2)

path11 = r"E:\CST\MKIcool\Full cell model\full wave\full cell\2cells end boundaries\S21_2cells_fullwave.txt"
s21_2cells_FW = np.loadtxt(path11,skiprows=2)


path12 = r"E:\CST\MKIcool\Full cell model\full wave\full cell\2cells end boundaries\MKI_circuit_equivalent_end_cells_thru_2cells.s2p"
S_2cells_FW = signal_toolbox.SNPfile(path12)

path13 = r"E:\CST\MKIcool\Full cell model\Circuit equivalent\MKI_circuit_equivalent_schematic_2CELLS.s2p"
S_2cells_CE = signal_toolbox.SNPfile(path13)

path14 = r"E:\CST\MKIcool\Full cell model\full wave\full cell\mid cell 5cells\MKI_circuit_equivalent_MID_CELL_5cells.s2p"
S_5cells_mid_FW = signal_toolbox.SNPfile(path14)

path15 = r"E:\CST\MKIcool\Full cell model\Circuit equivalent\MKI_circuit_equivalent_schematic_5CELLS_MID.s2p"
S_5cells_mid_CE = signal_toolbox.SNPfile(path15)

path16 = r"E:\CST\MKIcool\Full cell model\full wave\full cell\end cell 5 cells\MKI_circuit_equivalent_END_CELL_5cells_1_1.s2p"
S_5cells_end_FW = signal_toolbox.SNPfile(path16)

path17 = r"E:\CST\MKIcool\Full cell model\Circuit equivalent\MKI_circuit_equivalent_schematic_5CELLS_END.s2p"
S_5cells_end_CE = signal_toolbox.SNPfile(path17)


# plt.figure()
# plt.plot(s21_fullwave[:,0],s21_fullwave[:,1],'k')
# plt.plot(1e3*s21_circuitmodel[:,0],s21_circuitmodel[:,1],'b')
# plt.plot(s21_fullwave_2[:,0],s21_fullwave_2[:,1],'k',linestyle='--')
# plt.plot(1e3*s21_circuitmodel_2[:,0],s21_circuitmodel_2[:,1],'b',linestyle='--')
# # plt.plot(1e3*s21_circuitmodel_series_resistor[:,0],s21_circuitmodel_series_resistor[:,1])
# plt.grid(color='k', linestyle=':')
# plt.xlim([np.min(s21_fullwave[:,0]),np.max(s21_fullwave[:,0])])
# plt.ylim([-45, 15])
# plt.xlabel('Frequency [MHz]')
# plt.ylabel('$S_{21}$ [dB]')
# plt.legend(['Full wave simulation, tight PEC boundary','Circuit equivalent 1','Full wave simulation, far PEC boundary','Circuit equivalent 2'],loc='upper right')
# 
# 
# plt.figure()
# plt.plot(s21_FW_5cells[:,0],s21_FW_5cells[:,1],'k')
# plt.plot(1e3*s21_CE_5cells[:,0],s21_CE_5cells[:,1],'b')
# # plt.plot(1e3*s21_circuitmodel_series_resistor[:,0],s21_circuitmodel_series_resistor[:,1])
# plt.grid(color='k', linestyle=':')
# plt.xlim([np.min(s21_fullwave[:,0]),np.max(s21_fullwave[:,0])])
# plt.ylim([-45, 15])
# plt.xlabel('Frequency [MHz]')
# plt.ylabel('$S_{21}$ [dB]')
# plt.legend(['5 cells, full wave simulation','5 cells, circuit equivalent'],loc='upper right')



plt.figure()
plt.plot(s21_5cells_mid_FW[:,0],s21_5cells_mid_FW[:,1],'k',label='Mid cell, full wave')
plt.plot(1e3*s21_5cells_mid_CE[:,0],s21_5cells_mid_CE[:,1],'b',label='Mid cell, cirquit equivalent')
plt.grid(color='k', linestyle=':')
plt.xlim([np.min(s21_fullwave[:,0]),np.max(s21_fullwave[:,0])])
plt.ylim([-55, 15])
plt.xlabel('Frequency [MHz]')
plt.ylabel('$S_{21}$ [dB]')
plt.legend()


plt.figure()
plt.plot(s21_5cells_end_FW[:,0],s21_5cells_end_FW[:,1],'k',linestyle='--',label='End cell, full wave')
plt.plot(1e3*s21_5cells_end_CE[:,0],s21_5cells_end_CE[:,1],'b',linestyle='--',label='End cell, cirquit equivalent')
plt.grid(color='k', linestyle=':')
plt.xlim([np.min(s21_fullwave[:,0]),np.max(s21_fullwave[:,0])])
plt.ylim([-55, 15])
plt.xlabel('Frequency [MHz]')
plt.ylabel('$S_{21}$ [dB]')
plt.legend()


plt.figure()
plt.plot(s21_2cells_FW[:,0],s21_2cells_FW[:,1],'k',linestyle='--',label='2 cells, full wave')
plt.plot(1e3*s21_2cells_CE[:,0],s21_2cells_CE[:,1],'b',linestyle='--',label='2 cells, cirquit equivalent')
plt.grid(color='k', linestyle=':')
plt.xlim([np.min(s21_fullwave[:,0]),np.max(s21_fullwave[:,0])])
plt.ylim([-65, 15])
plt.xlabel('Frequency [MHz]')
plt.ylabel('$S_{21}$ [dB]')
plt.legend()


# PLOTS WITH SNP FILES:
plt.figure()
plt.plot(np.divide(S_2cells_FW.freq,1e6),S_2cells_FW.S21db,'k',linestyle='-',label='2 cells, full wave')
plt.plot(np.divide(S_2cells_CE.freq,1e6),S_2cells_CE.S21db,'b',linestyle='-',label='2 cells, cirquit equivalent')
plt.grid(color='k', linestyle=':')
plt.xlim([np.min(np.divide(S_2cells_FW.freq,1e6)),np.max(np.divide(S_2cells_FW.freq,1e6))])
plt.ylim([-65, 15])
plt.xlabel('Frequency [MHz]')
plt.ylabel('$S_{21}$ [dB]')
plt.legend()


plt.figure()
plt.plot(np.divide(S_2cells_FW.freq,1e6),S_2cells_FW.S21angle,'k',linestyle='-',label='2 cells, full wave')
plt.plot(np.divide(S_2cells_CE.freq,1e6),S_2cells_CE.S21angle,'b',linestyle='-',label='2 cells, cirquit equivalent')
plt.grid(color='k', linestyle=':')
plt.xlim([np.min(np.divide(S_2cells_FW.freq,1e6)),np.max(np.divide(S_2cells_FW.freq,1e6))])
# plt.ylim([-65, 15])
plt.xlabel('Frequency [MHz]')
plt.ylabel('$S_{21} phase$ [degrees]')
plt.legend()


plt.figure()
plt.plot(np.divide(S_5cells_mid_FW.freq,1e6),S_5cells_mid_FW.S21db,'k',linestyle='-',label='5 cells, mid cell excitation, full wave')
plt.plot(np.divide(S_5cells_mid_CE.freq,1e6),S_5cells_mid_CE.S21db,'b',linestyle='-',label='5 cells, mid cell excitation, cirquit equivalent')
plt.grid(color='k', linestyle=':')
plt.xlim([np.min(np.divide(S_5cells_mid_FW.freq,1e6)),np.max(np.divide(S_5cells_mid_FW.freq,1e6))])
plt.ylim([-65, 15])
plt.xlabel('Frequency [MHz]')
plt.ylabel('$S_{21}$ [dB]')
plt.legend()

plt.figure()
plt.plot(np.divide(S_5cells_mid_FW.freq,1e6),S_5cells_mid_FW.S21angle,'k',linestyle='-',label='5 cells, mid cell excitation, full wave')
plt.plot(np.divide(S_5cells_mid_CE.freq,1e6),S_5cells_mid_CE.S21angle,'b',linestyle='-',label='5 cells, mid cell excitation, cirquit equivalent')
plt.grid(color='k', linestyle=':')
plt.xlim([np.min(np.divide(S_2cells_FW.freq,1e6)),np.max(np.divide(S_2cells_FW.freq,1e6))])
# plt.ylim([-65, 15])
plt.xlabel('Frequency [MHz]')
plt.ylabel('$S_{21} phase$ [degrees]')
plt.legend()


plt.figure()
plt.plot(np.divide(S_5cells_end_FW.freq,1e6),S_5cells_end_FW.S21db,'k',linestyle='-',label='5 cells, end cell excitation, full wave')
plt.plot(np.divide(S_5cells_end_CE.freq,1e6),S_5cells_end_CE.S21db,'b',linestyle='-',label='5 cells, end cell excitation, cirquit equivalent')
plt.grid(color='k', linestyle=':')
plt.xlim([np.min(np.divide(S_5cells_end_FW.freq,1e6)),np.max(np.divide(S_5cells_end_FW.freq,1e6))])
plt.ylim([-65, 15])
plt.xlabel('Frequency [MHz]')
plt.ylabel('$S_{21}$ [dB]')
plt.legend()

plt.figure()
plt.plot(np.divide(S_5cells_end_FW.freq,1e6),S_5cells_end_FW.S21angle,'k',linestyle='-',label='5 cells, end cell excitation, full wave')
plt.plot(np.divide(S_5cells_end_CE.freq,1e6),S_5cells_end_CE.S21angle,'b',linestyle='-',label='5 cells, end cell excitation, cirquit equivalent')
plt.grid(color='k', linestyle=':')
plt.xlim([np.min(np.divide(S_2cells_FW.freq,1e6)),np.max(np.divide(S_2cells_FW.freq,1e6))])
# plt.ylim([-65, 15])
plt.xlabel('Frequency [MHz]')
plt.ylabel('$S_{21} phase$ [degrees]')
plt.legend()

plt.show()



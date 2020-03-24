import numpy as np
import matplotlib.pyplot as plt


path1 = r"E:\CST\MKIcool\Full cell model\full wave\full cell\with beam screen\S21.txt"
s21_fullwave = np.loadtxt(path1,skiprows=2)

path2 = r"E:\CST\MKIcool\Full cell model\Circuit equivalent\S21.txt"
s21_circuitmodel = np.loadtxt(path2,skiprows=2)

path2 = r"E:\CST\MKIcool\Full cell model\Circuit equivalent\S21_series_resistor.txt"
s21_circuitmodel_series_resistor = np.loadtxt(path2,skiprows=2)

plt.figure()
plt.plot(s21_fullwave[:,0],s21_fullwave[:,1],'k')
plt.plot(1e3*s21_circuitmodel[:,0],s21_circuitmodel[:,1],'b')
# plt.plot(1e3*s21_circuitmodel_series_resistor[:,0],s21_circuitmodel_series_resistor[:,1])
plt.grid(color='k', linestyle=':')
plt.xlim([np.min(s21_fullwave[:,0]),np.max(s21_fullwave[:,0])])
plt.xlabel('Frequency [MHz]')
plt.ylabel('$S_{21}$ [dB]')
plt.legend(['Full wave simulation','Circuit equivalent','Second resistor'])
plt.show()
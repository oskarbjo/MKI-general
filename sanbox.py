import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
import signal_toolbox

# data1 = np.loadtxt(R"C:\Users\objorkqv\cernbox\Documents\Python\MKI workspace\MKI general\data\MKIinput.txt",delimiter=',')
data1=np.loadtxt(r"\\cern.ch\dfs\Users\o\objorkqv\Documents\My Music\2019-11-11_2000ns_ref_waveform\RawWaveform_MKI.867.IPOC.CPU.UP_11.11.19@04h00m00s.csv",skiprows=4,delimiter=',')
data1[:,0]=data1[:,0]/1e6

f = np.linspace(-100,20e6,10001)
jw = 1j*2*np.pi*f
R0 = 5
R1 = 5
C1 = 40e-12
C2 = 0.4e-12
C3 = 2100e-12 + 60e-12
R2 = 50
R3 = 1e6


# t = np.linspace(0,20e-6,10001)
# func = np.sin(1e6*2*np.pi*t)
# data1 = np.transpose([t,func])



Z1 = R1 / (jw*C1*R1 + 1)
Z2 = (R2 + R3) / (jw*C3*(R2 + R3) + 1)
Z3 = Z2 + 1/(jw*C2)
Z4 = Z3*Z1 / (Z3 +  Z1)

D0 = Z4 / (Z4 + R0)
D1 = Z2 / (1/(jw*C2) + Z2)
D2 = R3 / (R2 + R3)

F = 2 * D0 * D1 * D2
F = 1/F
# F = F*0 - 0.5

FSIG = np.array([f,F])

# plt.figure()
# plt.plot(f,20*np.log10(np.abs(F)))
# 
# plt.show()

def main(): 
#     pickupSignal = signal_toolbox.Signal(data1[:,0],data1[:,1],1)
#     convolution = signal_toolbox.FDconvolution(FSIG,pickupSignal.FDSIG,len(pickupSignal.t))
#     
#     y_ifft = np.fft.irfft(pickupSignal.sig_fft)
#     
#     plt.figure()
#     plt.plot(convolution.t,convolution.TDsig/np.max(convolution.TDsig))
#     plt.plot(pickupSignal.t,pickupSignal.signal/np.max(pickupSignal.signal))
# #     plt.plot(convolution.t,convolution.TDsig/np.max(convolution.TDsig))
#     plt.grid()
#     
#     
#     plt.figure()
#     plt.plot(FSIG[0,:],20*np.log10(np.abs(FSIG[1,:])))
#     plt.plot(pickupSignal.freq,20*np.log10(np.abs(pickupSignal.sig_fft)))
#     plt.plot(convolution.f1,20*np.log10(np.abs(convolution.mult)))
# #     plt.plot(S.freq,S.S21db)
# 
#     plt.figure()
#     plt.plot(convolution.f1,20*np.log10(np.abs(convolution.mult)/len(convolution.mult)))
# 
# 
#     plt.show()


    plt.figure()
    plt.plot([0,1,2],[2,3,4],'ko')
    plt.title('$\Delta$ title')
    plt.legend(['$Z_{||}$'])
    plt.show()
    
    
if __name__ == "__main__":
    main()
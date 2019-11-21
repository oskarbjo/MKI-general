import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
import signal_toolbox
data1 = np.loadtxt(R"C:\Users\objorkqv\cernbox\Documents\Python\MKI workspace\MKI general\data\MKIinput.txt",delimiter=',')

f = np.linspace(-0.000001,20e6,10001)
jw = 1j*2*np.pi*f
R0 = 5
R1 = 5
C1 = 40e-12
C2 = 0.4e-12
C3 = 2100e-12 + 60e-12
R2 = 50
R3 = 1e6

Z1 = R1 / (jw*C1*R1 + 1)
Z2 = (R2 + R3) / (jw*C3*(R2 + R3) + 1)
Z3 = Z2 + 1/(jw*C2)
Z4 = Z3*Z1 / (Z3 +  Z1)

D0 = Z4 / (Z4 + R0)
D1 = Z2 / (1/(jw*C2) + Z2)
D2 = R3 / (R2 + R3)

F = 2 * D0 * D1 * D2 * np.sqrt(R0/R3)

FSIG = np.array([f,F])

# plt.figure()
# plt.plot(f,20*np.log10(np.abs(F)))
# 
# plt.show()

def main(): 
    pickupSignal = signal_toolbox.Signal(data1[:,0],data1[:,1],1)
    convolution = signal_toolbox.FDconvolution(FSIG,pickupSignal.FDSIG)
    
    plt.figure()
    plt.plot(convolution.t,convolution.TDsig)
#     plt.plot(convolution.t,convolution.TDsig/np.max(convolution.TDsig))
    plt.plot(pickupSignal.t,pickupSignal.signal)
    plt.figure()
    plt.plot(FSIG[0,:],20*np.log10(np.abs(FSIG[1,:])))
    plt.plot(pickupSignal.freq,20*np.log10(np.abs(pickupSignal.sig_fft)))
    plt.plot(convolution.f1,20*np.log10(np.abs(convolution.mult)))
#     plt.plot(S.freq,S.S21db)

    plt.figure()
    plt.plot(convolution.f1,20*np.log10(np.abs(convolution.mult)/len(convolution.mult)))


    plt.show()
    
    
if __name__ == "__main__":
    main()
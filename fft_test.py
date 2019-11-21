import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
import signal_toolbox
data1 = np.loadtxt(R"C:\Users\objorkqv\cernbox\Documents\Python\MKI workspace\MKI general\data\MKIinput.txt",delimiter=',')


t = np.linspace(0,20e-6,10001)
func = np.sin(1e6*2*np.pi*t)
data1 = np.transpose([t,func])




def main(): 
    pickupSignal = signal_toolbox.Signal(data1[:,0],data1[:,1],1)
    
    y = np.fft.irfft(pickupSignal.sig_fft)
    plt.figure()
    plt.grid()
    plt.plot(pickupSignal.t,pickupSignal.signal)
    plt.plot(pickupSignal.t,y,linestyle='--')
    

    
    plt.show()
    
    
if __name__ == "__main__":
    main()
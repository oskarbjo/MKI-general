import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
import signal_toolbox

# data1=np.loadtxt(r"\\cern.ch\dfs\Users\o\objorkqv\Documents\My Music\2019-11-11_2000ns_ref_waveform\RawWaveform_MKI.867.IPOC.CPU.UP_11.11.19@04h00m00s.csv",skiprows=4,delimiter=',')
# data1[:,0]=data1[:,0]/1e6

# t = np.linspace(0,20e-6,10001)
# w = np.pi*2*1e6
# func = 1*np.sin(w*t)
# data1 = np.transpose([t,func])

data1 = np.loadtxt(R"C:\Users\objorkqv\cernbox\Documents\Python\MKI workspace\MKI general\data\MKIinput.txt",delimiter=',')
# pickup_sparam_path = r"E:\CST\MKIcool\pickup model\circuit model\MKI_pickup_circuit_model.s2p"
# pickup_sparam_path = r"E:\CST\MKIcool\MKIcool_redrawn\Propagation through cells\Frequency domain\simulated\FD 1 sparam model\MKI_propagation_freq_domain_sparam.s2p"

data2_re = np.loadtxt(r"E:\CST\MKIcool\pickup model\circuit model\S21_correct_terminations_REAL.txt",skiprows=2)
data2_im = np.loadtxt(r"E:\CST\MKIcool\pickup model\circuit model\S21_correct_terminations_IMAG.txt",skiprows=2)

data2_freq = data2_re[:,0]*1e6
data2_compl = (data2_re[:,1]+1j*data2_im[:,1])
# data2_compl = 1/data2_compl
S21 = np.asarray([data2_freq,data2_compl])
# S21[1,0:10] = 0



def main(): 
    pickupSignal = signal_toolbox.Signal(data1[:,0],data1[:,1],1)
#     S=signal_toolbox.SNPfile(pickup_sparam_path)
    convolution = signal_toolbox.FDconvolution(S21,pickupSignal.FDSIG)
    
    plt.figure()
    plt.plot(convolution.t,convolution.TDsig)
#     plt.plot(convolution.t,convolution.TDsig/np.max(convolution.TDsig))
    plt.plot(pickupSignal.t,pickupSignal.signal)
    plt.figure()
    plt.plot(S21[0,:],20*np.log10(np.abs(S21[1,:])))
    plt.plot(pickupSignal.freq,20*np.log10(np.abs(pickupSignal.sig_fft)))
    plt.plot(convolution.f1,20*np.log10(np.abs(convolution.mult)))
#     plt.plot(S.freq,S.S21db)

    plt.figure()
    plt.plot(convolution.f1,20*np.log10(np.abs(convolution.mult)/len(convolution.mult)))


    plt.show()
    
    
if __name__ == "__main__":
    main()
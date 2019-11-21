### Loads a touchstone S2P file into np arrays



import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate


class SNPfile:
    def __init__(self,filePath):
        self.S11lin = []
        self.S21lin = []
        self.S12lin = []
        self.S22lin = []
        self.freq = []
        self.S11db = []
        self.S21db = []
        self.S12db = []
        self.S22db = []
        self.S11angle = []
        self.S21angle = []
        self.S12angle = []
        self.S22angle = []
        self.S21complex = []
        path = filePath
        self.extractSParamData(filePath)
        self.getComplexParam()
        self.FDSIGS21 = np.asarray([self.freq,self.S21complex])
        
    def extractSParamData(self,filePath):
        file=open(filePath,'r')
        lines=file.readlines()
        for i in range(0,len(lines)):
            data = self.separateParameters(lines[i])
            data=data[0].split()
            try:
                self.freq = self.freq + [np.double(data[0])*self.freq_prefix]
                self.S11lin = self.S11lin + [np.double(data[1])]
                self.S21lin = self.S21lin + [np.double(data[3])]
                self.S12lin = self.S12lin + [np.double(data[5])]
                self.S22lin = self.S22lin + [np.double(data[7])]
                self.S11db = self.S11db + [20*np.log10(np.double(data[1]))]
                self.S21db = self.S21db + [20*np.log10(np.double(data[3]))]
                self.S12db = self.S12db + [20*np.log10(np.double(data[5]))]
                self.S22db = self.S22db + [20*np.log10(np.double(data[7]))]
                self.S11angle = self.S11angle + [np.double(data[2])]
                self.S21angle = self.S21angle + [np.double(data[4])]
                self.S12angle = self.S12angle + [np.double(data[6])]
                self.S22angle = self.S22angle + [np.double(data[8])]
            except:
                if data[0]=='#':
                    if data[1].find('GHz')==0:
                        self.freq_prefix = 1e9
                    if data[1].find('MHz')==0:
                        self.freq_prefix = 1e6
                print('Removing SNP header')
        
    def getComplexParam(self):
        for i in range(0,len(self.S21lin)):
            im=np.array([0+1j])
            im=im[0]
            self.S21complex = self.S21complex + [self.S21lin[i]*(np.cos(np.pi*self.S21angle[i]/180)+np.sin(np.pi*self.S21angle[i]/180)*im)]
        
    def separateParameters(self,line):
        line=line.strip('\n')
        line=line.split('\t')
        return line
    
    def plotParam(self,Sparam):
        plt.figure()
        plt.plot(self.freq,Sparam)
        plt.show()
    
    def dBtoLin(self,dBdata):
        linData = np.power(10,dBdata/20)
        return linData
        
    def getImpulseResponse(self):
        self.s21_impulse = np.fft.irfft(self.S21complex)
        dt = 1/(1e6*self.freq[-1])
        self.s21_t = np.linspace(0,(len(self.s21_impulse)-1)*dt,len(self.s21_impulse))
    
#     def writeSNPtoFile(self):
    
      
class Signal:
    #This class takes a signal (time & data) and its time prefix and calculates an equidistant 
    #sampling of the same signal as well as a single sided fft
    def __init__(self,t,sig,timePrefix):
        
        self.timePrefix = timePrefix
        self.t = t*self.timePrefix
        self.signal = sig
        self.setTimeRefToZero() #Set t0 = 0
        
        if not self.hasUniformSampling():
            self.uniformSampling()
        
        self.zeropad()
        self.getSpectrum()
        
        
        self.TDSIG = np.asarray([self.t,self.signal])
        self.FDSIG = np.asarray([self.freq,self.sig_fft])
        
        
    def setTimeRefToZero(self):
        self.t = self.t - self.t[0]
        
         
    def hasUniformSampling(self):
        dt = self.t[1:]-self.t[0:-1]
        if np.sum(dt-dt[0]) < 1e-15:
            uniformSampling = True
            self.dt = dt[0]
        else:
            uniformSampling = False
        return uniformSampling
        
    def uniformSampling(self):
        #Resamples signal to have equidistant samples
        signal_temp = interpolate.interp1d(self.t,self.signal)
        Nsamples = 10001 #Choose number of samples in new set
        newTime = np.linspace(self.t[0],self.t[-1],Nsamples)
        signal_interp = signal_temp(newTime)
        self.oldt = self.t
        self.oldsig = self.signal
        self.t = newTime
        self.signal = signal_interp
        self.dt = newTime[1]-newTime[0]

    def getSpectrum(self):
        self.sig_fft = np.fft.rfft(self.signal)
        fs = 1/self.dt
        self.freq = np.linspace(0,0.5/self.dt,len(self.sig_fft))
        
    def zeropad(self):
        #Adds (2^N-1)*len(self.t) zeros to signal
        N = 5
        for i in range(0,N):
            self.t = np.append(self.t,self.t+self.t[-1]+self.t[1])
            self.signal = np.append(self.signal,np.zeros(len(self.signal)))


class FDconvolution:
    
    def __init__(self,FDSIG1,FDSIG2,length):
        self.inputLength = length
        self.f1 = FDSIG1[0,:]
        self.f2 = FDSIG2[0,:]
        self.S1 = FDSIG1[1,:]
        self.S2 = FDSIG2[1,:]
        self.cropFrequencyRange()
        self.resample()
        self.multiply()
        self.invfft()

    def cropFrequencyRange(self): 
        # Crops frequencies of the longer data set if the two 
        # frequency ranges do not span over the same intervals
        if self.f1[-1] > self.f2[-1]:
            itemindex = np.where(self.f1>self.f2[-1])
            self.f1 = self.f1[0:itemindex[0][0]-1]
            self.S1 = self.S1[0:itemindex[0][0]-1]
        elif self.f2[-1] > self.f1[-1]:
            itemindex = np.where(self.f2>self.f1[-1])
            self.f2 = self.f2[0:itemindex[0][0]-1]
            self.S2 = self.S2[0:itemindex[0][0]-1]
            
    def resample(self):
        #Resamples frequency domain curve with lower resolution
        if (len(self.f1)/self.f1[-1] > len(self.f2)/self.f2[-1]):
            S2_temp = interpolate.interp1d(self.f2,self.S2)
            self.S2 = S2_temp(self.f1)
            self.f2 = self.f1
        else:
            S1_temp = interpolate.interp1d(self.f1,self.S1)
            self.S1 = S1_temp(self.f2)
            self.f1 = self.f2

    def multiply(self):
        self.mult = self.S1 * self.S2

    def invfft(self):
        TDsig = np.fft.irfft(self.mult)
        scaling = len(TDsig)/self.inputLength
        self.TDsig = TDsig * scaling
        dt = np.real(1/(2*self.f1[-1]))
        self.t = np.arange(0,dt*(len(self.TDsig)),dt)        

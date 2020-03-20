import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from itertools import groupby

class winCCData():
    
    def __init__(self,path):
        self.filePath = path
        self.timeStamps = []
        self.timeSeconds = []
        self.vacuum = []
        self.Vref = []
        self.Vmeas = []
        self.Npulses = []
        self.pulseLength = []
        self.timeHours = []
        self.extractData()
        self.unfoldPulseCount()
        
    def extractData(self):
        data=np.loadtxt(self.filePath,skiprows=1,dtype='str', unpack=True, encoding="utf16")
        for i in range(0,len(data[0,:])):
            self.timeStamps.append(data[0,i] + ' ' + data[1,i])
            self.timeSeconds.append(np.double(i/2))
            self.vacuum.append(np.double(data[2,i]))
            self.Vref.append(np.double(data[8,i]))
            self.Vmeas.append(np.double(data[5,i]))
            self.pulseLength.append(np.double(data[11,i]))
            self.Npulses.append(np.double(data[14,i]))
        self.timeHours = np.divide(self.timeSeconds,3600)
    
    def unfoldPulseCount(self):
        
        self.Npulses = self.Npulses - self.Npulses[0]
        N=len(self.Npulses)
        C = 0
        for i in range(0,N-1):
            if self.Npulses[i+1] < self.Npulses[i]:
                C = C + self.Npulses[i] - self.Npulses[i+1] + 1
                self.Npulses[i+1:] = self.Npulses[i+1:] + C
            print(i)
        
        
        
#         self.uniquePulses = [k for k,g in groupby(self.Npulses) if k!=0]
#         self.uniquePulseTimearrayHours = np.linspace(0,np.max(self.timeHours),len(self.uniquePulses))
#         self.NuniquePulses = np.arange(0,np.max(self.uniquePulses))
        
    def plotwinCCdata(self):
        figure, axis_1 = plt.subplots(num=None, figsize=(11, 6), dpi=140, facecolor='w', edgecolor='k')
        p1,=axis_1.semilogy(self.timeHours,self.vacuum,color='blue',label='Pressure')
        plt.ylabel('Pressure [Bar]')
        plt.xlabel('Time [Hours]')
        plt.xlim([0,np.max(self.timeHours)])
#         plt.ylim([1e-11, 1e-5])
        axis_2 = axis_1.twinx()
        p2,=axis_2.plot(self.timeHours,self.Vref,color='green',label='Vref')
        p3,=axis_2.plot(self.timeHours,self.Vmeas,color='red',label='Vmeas')
        plt.ylabel('Voltage [kV]')
        plt.ylim([25, 60])
        axis_3 = axis_1.twinx()
        axis_3.spines["right"].set_position(("axes", 1.051))
        p4,=axis_3.plot(self.timeHours,self.Npulses,label='Npulses')
        lines = [p1, p2, p3, p4]
        axis_1.legend(lines, [l.get_label() for l in lines],loc="upper left")
        ax2 = axis_1.twiny()
        ax2.set_xticks(self.timeHours[0::40000])
        ax2.set_xticklabels(self.timeStamps[0::40000])
        plt.xlim([0,np.max(self.timeHours)])
        
    def vacuumExpFit(self):
        t1=103772
        t2=t1+41
        Td=t2-t1
        d1, d2 = curve_fit(exponential_func, np.arange(0,Td), self.vacuum[t1:t2])
        curveFit = exponential_func(np.arange(-1,Td),*d1)
        plt.figure()
        plt.plot(np.arange(0,Td),self.vacuum[t1:t2])
        plt.plot(np.arange(-1,Td),curveFit)
        plt.grid()
        
def exponential_func(x, a, b, c):
    return a*np.exp(-b*x)+c


def main():  

    ###################### Plot winCC data: ######################
    # File path of exported winCC data (has to be tab delimited!)
    winccPath = r"G:\Departments\TE\Groups\ABT\Sections\PPE\Users\objorkqv\winCC export\2020-03-15_2020-03-18.csv"
    winCC = winCCData(winccPath)
    winCC.plotwinCCdata()
#      winCC.vacuumExpFit()
    plt.show()

if __name__ == "__main__":
    main()
    
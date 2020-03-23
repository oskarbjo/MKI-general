import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from itertools import groupby
from os import listdir
from os.path import isfile, join

class winCCData():
    
    def __init__(self,path,timeStamp1,timeStamp2):
        self.t1 = timeStamp1
        self.t2 = timeStamp2
        self.filePath = path
        self.timeStamps = []
        self.timeSeconds = np.double([0])
        self.vacuum = []
        self.Vref = []
        self.Vmeas = []
        self.Npulses = []
        self.pulseLength = []
        self.timeHours = []
        self.extractData()
        self.unfoldPulseCount()
        self.timeSeconds = self.timeSeconds[1:]
        self.getDemandedDates()
        self.timeHours = np.divide(self.timeSeconds,3600)
        
    def extractData(self):
        fileNames= [f for f in listdir(self.filePath) if isfile(join(self.filePath, f))] #find files in path
        for file in fileNames: #Iterate through found files
            data=np.loadtxt(self.filePath + file,skiprows=1,dtype='str', unpack=True, encoding="utf16") #Load data - if there is an encoding issue, try 'utf8'
            
            #Initialize temporary variables
            timeStamps = []
            timeSeconds = []
            vacuum = []
            Vref = []
            Vmeas = []
            Npulses = []
            pulseLength = []
            timeHours = []
            
            for i in range(0,len(data[0,:])):
                timeStamps.append(data[0,i] + ' ' + data[1,i])
                timeSeconds.append(np.double(i/2))
                vacuum.append(np.double(data[2,i]))
                Vref.append(np.double(data[8,i]))
                Vmeas.append(np.double(data[5,i]))
                pulseLength.append(np.double(data[11,i]))
                Npulses.append(np.double(data[14,i]))
                print(i)
    
            self.timeStamps = self.timeStamps + timeStamps
            timeSeconds=np.add(timeSeconds,self.timeSeconds[-1])
            self.timeSeconds = np.append(self.timeSeconds,timeSeconds)
            self.vacuum = self.vacuum + vacuum
            self.Vref = self.Vref + Vref
            self.Vmeas = self.Vmeas + Vmeas
            self.Npulses = self.Npulses + Npulses
            self.pulseLength = self.pulseLength + pulseLength
            
    def unfoldPulseCount(self):
        
        self.Npulses = self.Npulses - self.Npulses[0]
        N=len(self.Npulses)
        C = 0
        for i in range(0,N-1):
            if self.Npulses[i+1] < self.Npulses[i]:
                C = self.Npulses[i] - self.Npulses[i+1] + 1
                self.Npulses[i+1:] = self.Npulses[i+1:] + C
            print(i)
        
    
    def getDemandedDates(self):
        ind1 = [i for i, s in enumerate(self.timeStamps) if self.t1 in s][0]
        ind2 = [i for i, s in enumerate(self.timeStamps) if self.t2 in s][0]
        self.timeStamps = self.timeStamps[ind1:ind2]
        self.timeSeconds = self.timeSeconds[ind1:ind2]
        self.vacuum = self.vacuum[ind1:ind2]
        self.Vref = self.Vref[ind1:ind2]
        self.Vmeas = self.Vmeas[ind1:ind2]
        self.Npulses = self.Npulses[ind1:ind2]
        self.pulseLength = self.pulseLength[ind1:ind2]
        
        
    def plotwinCCdata(self):
        plotDateEveryN = 120000
        figure, axis_1 = plt.subplots(num=None, figsize=(11, 6), dpi=140, facecolor='w', edgecolor='k')
        p1,=axis_1.semilogy(self.timeHours,self.vacuum,color='blue',label='Pressure')
        plt.ylim([1e-11,1e-4])
        plt.ylabel('Pressure [Bar]')
        plt.xlabel('Time [Hours]')
        plt.xlim([np.min(self.timeHours),np.max(self.timeHours)])
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
        ax2.set_xticks(self.timeHours[0::plotDateEveryN])
        ax2.set_xticklabels(self.timeStamps[0::plotDateEveryN])
        plt.xlim([np.min(self.timeHours),np.max(self.timeHours)])
        
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
    # File path of exported winCC data (has to be tab delimited .csv!)
    winccPath = r"G:\Departments\TE\Groups\ABT\Sections\PPE\Users\objorkqv\winCC export/"
    #Time stamps (be mindful that the data set needs to contain the selected time stamps)
    timeStamp1 = '20/02/2020 07:00:00' #Start timestamp, must have format '20/02/2020 11:08:14'
    timeStamp2 = '18/03/2020 06:59:00' #End timestamp, must have format '20/02/2020 11:08:14'
    winCC = winCCData(winccPath,timeStamp1,timeStamp2)
    winCC.plotwinCCdata()
#      winCC.vacuumExpFit()
    plt.show()

if __name__ == "__main__":
    main()
    
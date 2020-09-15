import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from itertools import groupby
from os import listdir
from os.path import isfile, join
from datetime import datetime
#%matplotlib notebook
print('*** Running Script ***')

class winCCData():
    
    def __init__(self,path):
        self.filePath = path
        self.timeStamps = []
        self.timeStampsShort = []
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
        self.timeHours = np.divide(self.timeSeconds,3600)
        
    def extractData(self):
        fileNames= [f for f in listdir(self.filePath) if isfile(join(self.filePath, f))] #find files in path
        for file in fileNames: #Iterate through found files
            try:
                data=np.loadtxt(self.filePath + file,skiprows=1,dtype=np.unicode, unpack=True, encoding="utf16") #Load data - if there is an encoding issue, try 'utf8'
            except:
                print('There was an encoding error - probably because there are other files than the WinCC data in the directory. \nIf the WinCC data has been saved correctly, this is not a problem')
            #Initialize temporary variables
            timeStamps = []
            timeStampsShort = []
            timeSeconds = []
            vacuum = []
            Vref = []
            Vmeas = []
            Npulses = []
            pulseLength = []
            timeHours = []
            
            for i in range(0,len(data[0,:])):
                timeStamps.append(data[0,i] + ' ' + data[1,i])
                timeStampsShort.append(data[0,i][0:5] + ' ' + data[1,i][0:8])
                timeSeconds.append(np.double(i/2))
                vacuum.append(np.double(data[2,i]))
                Vref.append(np.double(data[8,i]))
                Vmeas.append(np.double(data[5,i]))
                pulseLength.append(np.double(data[11,i]))
                Npulses.append(np.double(data[14,i]))
            print('File ' + file + ' read')
    
            self.timeStamps = self.timeStamps + timeStamps
            self.timeStampsShort = self.timeStampsShort + timeStampsShort
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
        print('Counter curve unfolded')
        
    
    def getDemandedDates(self,timeStamp1,timeStamp2,pulseCounterOffset,totalTimeOffsetHours):
        #Filters out data for the requested dates
        self.totalTimeOffset = totalTimeOffsetHours
        self.pulseCounterOffset = pulseCounterOffset
        self.t1 = timeStamp1
        self.t2 = timeStamp2
        ind1 = [i for i, s in enumerate(self.timeStamps) if self.t1 in s][0]
        ind2 = [i for i, s in enumerate(self.timeStamps) if self.t2 in s][0]
        self.timeStampsPlot = self.timeStampsShort[ind1:ind2]
        self.timeSecondsPlot = self.timeSeconds[ind1:ind2]
        self.vacuumPlot = self.vacuum[ind1:ind2]
        self.VrefPlot = self.Vref[ind1:ind2]
        self.VmeasPlot = self.Vmeas[ind1:ind2]
        self.NpulsesPlot = self.Npulses[ind1:ind2] + pulseCounterOffset
        self.pulseLengthPlot = self.pulseLength[ind1:ind2]
        self.timeHoursPlot = np.divide(self.timeSecondsPlot,3600) + totalTimeOffsetHours
        self.VrefFinal = np.round(self.VrefPlot[-1],4)
        self.VmeasFinal = np.round(self.VmeasPlot[-1],4)
        self.NpulsesFinal = self.NpulsesPlot[-1]
        
    def plotwinCCdata(self,plotDateEveryN,vacuumMin,vacuumMax, Plotfilename):
        figure, axis_1 = plt.subplots(num=None, figsize=(11, 6), dpi=140, facecolor='w', edgecolor='k')
        p1,=axis_1.semilogy(self.timeHoursPlot,self.vacuumPlot,color='blue',label='Pressure')
        plt.ylim([vacuumMin,vacuumMax])
        plt.ylabel('Pressure [Bar]')
        plt.xlabel('Time [Hours]')
        plt.xlim([np.min(self.timeHoursPlot),np.max(self.timeHoursPlot)])
#         plt.ylim([1e-11, 1e-5])
        axis_2 = axis_1.twinx()
        p2,=axis_2.plot(self.timeHoursPlot,self.VrefPlot,color='green',label='Vref (final = ' + str(self.VrefFinal) + ' kV)')
        p3,=axis_2.plot(self.timeHoursPlot,self.VmeasPlot,color='red',label='Vmeas (final = ' + str(self.VmeasFinal) + ' kV)')
        plt.ylabel('Voltage [kV]')
        plt.ylim([25, 60])
        axis_3 = axis_1.twinx()
        axis_3.spines["right"].set_position(("axes", 1.051))
        p4,=axis_3.plot(self.timeHoursPlot,self.NpulsesPlot,label='Npulses (final = ' + str(self.NpulsesFinal) + ')')
        lines = [p1, p2, p3, p4]
        axis_1.legend(lines, [l.get_label() for l in lines],loc="upper left")
        ax2 = axis_1.twiny()
        ax2.set_xticks(self.timeHoursPlot[0::plotDateEveryN])
        ax2.set_xticklabels(self.timeStampsPlot[0::plotDateEveryN],rotation=90)
        ax2.tick_params(labelsize=5)
        plt.xlim([np.min(self.timeHoursPlot),np.max(self.timeHoursPlot)])
        plt.savefig(Plotfilename, bbox_inches='tight', dpi=200)
        print('Plot Saved As: ',Plotfilename)
#         print('Total pulse count = ',self.NpulsesFinal, 'using an offset of ', str(self.pulseCounterOffset), ' pulses') # last element of list
#         print('Total run time = ', self.timeHoursPlot[-1], 'hours, using an offset of ', str(self.totalTimeOffset), ' hours')
        print('Last demanded voltage = ',self.VrefFinal,' kV') # last element of list
        print('Last measured voltage = ',self.VmeasFinal,' kV') # last element of list
        
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
        
    def findSparks(self,weakSparkLimit,strongSparkLimit):
        #Finds rising edges for the specified vacuum limits
        vacuumAsArray = np.array(self.vacuumPlot)
        self.allSparkIndices = np.flatnonzero((vacuumAsArray [:-1] < weakSparkLimit) & (vacuumAsArray [1:] > weakSparkLimit))+1
        strongSparkIndices = np.flatnonzero((vacuumAsArray [:-1] < strongSparkLimit) & (vacuumAsArray [1:] > strongSparkLimit))+1
        ind_temp = []
        for i in strongSparkIndices:
            ind_temp.append(np.where(self.allSparkIndices == i))
#         weakSparkIndices = list(set(self.allSparkIndices)^set(strongSparkIndices)) #Remove sparks that are counted twice
        weakSparkIndices = np.delete(self.allSparkIndices,ind_temp)
        numberStrongSparks = len(strongSparkIndices)
        numberWeakSparks = len(weakSparkIndices)
        
        
        # Prep all the text output to save:
        out00 = 'Time range plotted: ' + str(self.timeStampsPlot[0]) + ' - ' + str(self.timeStampsPlot[-1]) + '\n'
        out0 = 'Weak spark limit: ' + str(weakSparkLimit) + '\nStrong spark limit: ' + str(strongSparkLimit) + '\n'
        out1 = 'Number of strong sparks: ' + str(numberStrongSparks) + '\n'
        out2 = 'Number of weak sparks: ' + str(numberWeakSparks) + '\n'
        out21 = 'Run time: ' + str(self.timeHoursPlot[-1]) + ' hours (offset = ' + str(self.totalTimeOffset) + ')\nTotal number of pulses: ' + str(self.NpulsesFinal) + ' (offset = ' + str(self.pulseCounterOffset) +')\n'
        out3 = '\n --------- Strong sparks: --------- \n'
        for i in range(0,numberStrongSparks):
            out3 = out3 + 'Timestamp: ' + str(self.timeStamps[strongSparkIndices[i]]) + ', pressure: ' + str(np.format_float_scientific(self.vacuum[strongSparkIndices[i]])) + '\n'
        out4 = '\n --------- Weak sparks: --------- \n'
        for i in range(0,numberWeakSparks):
            out4 = out4 + 'Timestamp: ' + str(self.timeStamps[weakSparkIndices[i]]) + ', pressure: ' + str(np.format_float_scientific(self.vacuum[weakSparkIndices[i]])) + '\n'
        
        out = out00 + out0 + out1 + out2 + out21 + out3 + out4
        
        #Print and write to file:
        print(out)
        file = open(self.filePath + 'sparks.txt','w')
        file.write(out)
        print('Spark data saved in ' + str(self.filePath) + '/sparks.txt')
        
    
    def findMisAlignedSparks(self):
        # Finds the time delays from counter incrementation to sparking
        
        #Get a list of time stamps at sparking
        a=map(self.timeStamps.__getitem__,self.allSparkIndices)
        self.allSparkTimeStamps = list(a)
        #Get the pulse counter values at the sparks
        pulseCounterAtSpark=self.Npulses[self.allSparkIndices]
        
        #Find the delay between pulse incrementation and sparking
        self.pulseCounterStepsPrecedingSpark_index = []
        for i in range(0,len(pulseCounterAtSpark)):
            p = self.allSparkIndices[i]
            while self.Npulses[p] == self.Npulses[self.allSparkIndices[i]]:
                p = p=p-1
            self.pulseCounterStepsPrecedingSpark_index.append(p+1)
            
        b=map(self.timeStamps.__getitem__,self.pulseCounterStepsPrecedingSpark_index)
        self.pulseCounterStepsBeforeSpark_timeStamps = list(b)    
        
        #Printing out all recorded dates for sparks and preceding pulse counter steps (for debugging):
        print('Pulse counter steps before sparks, timestamps: ' + str(self.pulseCounterStepsBeforeSpark_timeStamps))
        print('Sparks timestamps: ' + str(self.allSparkTimeStamps))
        
        self.counterDateTimeObject = []
        self.sparkDateTimeObject = []
        self.sparkDelays = []
        for i in range(0,len(self.pulseCounterStepsBeforeSpark_timeStamps)):
            #Reformating for datetime object
            counter_timeStamp_temp = self.pulseCounterStepsBeforeSpark_timeStamps[i]
            spark_timeStamp_temp = self.allSparkTimeStamps[i]
            counter_timeStamp_temp=counter_timeStamp_temp[6:10]+'-'+ counter_timeStamp_temp[3:5] + '-' + counter_timeStamp_temp[0:2] + ' ' + counter_timeStamp_temp[11:]
            spark_timeStamp_temp=spark_timeStamp_temp[6:10]+'-'+ spark_timeStamp_temp[3:5] + '-' + spark_timeStamp_temp[0:2] + ' ' + spark_timeStamp_temp[11:]
            counter_dateTime = datetime.fromisoformat(counter_timeStamp_temp)
            spark_dateTime = datetime.fromisoformat(spark_timeStamp_temp)
            sparkDelays_dateTime = (spark_dateTime-counter_dateTime)
            self.sparkDelays.append(sparkDelays_dateTime.seconds)
            self.counterDateTimeObject.append(counter_dateTime)
            self.sparkDateTimeObject.append(spark_dateTime.isoformat())
        
        figure, ax1 = plt.subplots(num=None, figsize=(11, 6), dpi=140, facecolor='w', edgecolor='k')
        plt.stem(self.sparkDelays)
        plt.xlim([0, len(self.sparkDelays)-1])
        plt.ylim([0, 20])
        plt.grid()
        plt.xlabel('Spark number')
        plt.ylabel('Delay from pulse counter incrementation to spark [seconds]')
        ax = ax1.twiny()
        ax.set_xticks(np.arange(0,len(self.sparkDelays)))
        ax.set_xticklabels(self.allSparkTimeStamps,rotation=90)
        ax.tick_params(labelsize=5)
        figure.tight_layout()
        
        
def exponential_func(x, a, b, c):
    return a*np.exp(-b*x)+c



###################### Plot winCC data #######################

# USER INPUTS:

# File path of exported winCC data (has to be tab delimited .csv!)
# The files will be read in alphabetical order so it is important that they are named correctly
# Previously we have used the convention: 2020-05-19_2020-05-22.csv etc.
winccPath = r"\\cern.ch\dfs\Departments\TE\Groups\ABT\Users\B\BJORKQVIST_Oskar\winCC export\Export conditioning MKI cool post covid/"
# Time stamps (be mindful that the data set needs to contain the selected time stamps):
timeStamp1 = '19/05/2020 07:00:00' #Start timestamp, must have format '20/02/2020 11:08:14'
timeStamp2 = '28/05/2020 06:59:00' #End timestamp, must have format '20/02/2020 11:08:14'
Plotfilename = 'WinCC_Plot_20022020-18032020.png' # Name of plot export
dateTickEveryNseconds = 50000      #Plot a date tick every 0.5*N seconds
vacuumMin = 1e-11 #Vacuum lower limit for plot
vacuumMax = 1e-6  #Vacuum upper limit for plot
weakSparkLimit = 5.0e-9 #Weak spark vacuum limit
strongSparkLimit = 3e-8 #Strong spark vacuum limit
pulseCounterOffset =  0 # If the user wants to manually add pulses to the pulse counter
totalTimeOffsetHours = 0 #If the user wants to manually add time (in hours) to the time counter

# Run the class file that fetches and plots the data:
winCC = winCCData(winccPath)        
winCC.getDemandedDates(timeStamp1,timeStamp2,pulseCounterOffset,totalTimeOffsetHours)
winCC.findSparks(weakSparkLimit,strongSparkLimit)
winCC.findMisAlignedSparks()
winCC.plotwinCCdata(dateTickEveryNseconds,vacuumMin,vacuumMax,Plotfilename)
#      winCC.vacuumExpFit()
plt.show()
print('*** Done ***')




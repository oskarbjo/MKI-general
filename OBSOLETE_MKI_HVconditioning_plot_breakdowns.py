import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile, join
from scipy.optimize import curve_fit

#Save CPU_DW, CPU_UP and IM breakdown data sets from IPOC explorer to a single folder (no other files should be present)
#Save CPU_DW, CPU_UP and IM reference data sets from IPOC explorer to another, separate, single folder (no other files should be present)
#Copy these folder paths to variable 'filePath' & 'refFilePath' in main function and run

class BreakDown:
    
    def __init__(self,filePath):
        self.threshold = 2 #Rising/falling edge threshold for CPUs
        self.thresholdTMR = 2 #Rising/falling edge threshold for TMR
        self.path = filePath 
        self.fileNames, self.ind, self.timeStamp=self.getFileNames()
#         self.CPU_DW,self.CPU_UP,self.IM = self.getMagnetData(self.fileNames, self.ind)
        self.CPU_DW,self.CPU_UP,self.IM,self.TMR = self.getMagnetData(self.fileNames, self.ind)
#         self.TMR = self.getTMR()
        self.timeDelays()
        
    def getFileNames(self):
        #Finds the file names corresponding to the three data sets (CPU_UP, CPU_DW, IM)
        fileNames= [f for f in listdir(self.path) if isfile(join(self.path, f))]
        j=0
        CPU_DW_ind = None
        CPU_UP_ind = None
        IM_ind = None
        TMR_ind = None        
        for i in fileNames:
            if (i.find('.IPOC.CPU.DW')+1):
                CPU_DW_ind = j
            if (i.find('.IPOC.CPU.UP')+1):
                CPU_UP_ind = j
            if (i.find('.IPOC.IM')+1):
                IM_ind = j
            if (i.find('IPOC.TMR')+1):
                TMR_ind = j
            j=j+1
        ind = [CPU_DW_ind, CPU_UP_ind, IM_ind, TMR_ind]
        timeStamp = fileNames[0][-22:-4]
        return fileNames,ind,timeStamp
        
    def getMagnetData(self,fileNames,ind):
        #Extracts the data sets from the files
        CPU_DW_path = self.path+fileNames[ind[0]]
        CPU_UP_path = self.path+fileNames[ind[1]]
        IM_path = self.path+fileNames[ind[2]]
        try:
            TMR_path = self.path + fileNames[ind[3]]
        except:
            TMR_path = ''
        CPU_DW = np.loadtxt(CPU_DW_path,delimiter=',',skiprows=4,unpack=True,usecols=np.arange(0,2))
        CPU_UP = np.loadtxt(CPU_UP_path,delimiter=',',skiprows=4,unpack=True,usecols=np.arange(0,2))
        IM = np.loadtxt(IM_path,delimiter=',',skiprows=4,unpack=True,usecols=np.arange(0,2))
        try:
            TMR = np.loadtxt(TMR_path,delimiter=',',skiprows=4,unpack=True,usecols=np.arange(0,2))
            TMR[1,:] = TMR[1,:]*4
        except:
            print('Could not load TMR data')
            TMR = [0,0]
        return CPU_DW,CPU_UP,IM,TMR
    
    def timeDelays(self):
        #Calculates the time delays between the up/down pickup to help trace where breakdowns occur
        self.risingTimeDelayTMR = 0
        self.fallingTimeDelayTMR = 0
        try:
            #Rising edges:
            self.t0_rising_ind=next(x[0] for x in enumerate(self.CPU_UP[1,:]) if x[1] > self.threshold)
            self.t1_rising_ind=next(x[0] for x in enumerate(self.CPU_DW[1,:]) if x[1] > self.threshold)
            self.risingTimeDelay = self.CPU_DW[0,self.t1_rising_ind]-self.CPU_UP[0,self.t0_rising_ind]
            try:
                self.t1_rising_ind_TMR=next(x[0] for x in enumerate(self.TMR[1,:]) if x[1] > self.thresholdTMR)
                self.risingTimeDelayTMR = self.TMR[0,self.t1_rising_ind_TMR]-self.CPU_UP[0,self.t0_rising_ind]                
            except:
                print('No TMR data available, can not calculate rising edges')
            #Falling edges:
            self.t0_falling_ind=next(x[0] for x in enumerate(self.CPU_UP[1,self.t0_rising_ind:]) if x[1] < self.threshold) + self.t0_rising_ind
            self.t1_falling_ind=next(x[0] for x in enumerate(self.CPU_DW[1,self.t1_rising_ind:]) if x[1] < self.threshold) + self.t1_rising_ind
            self.fallingTimeDelay = self.CPU_DW[0,self.t1_falling_ind]-self.CPU_UP[0,self.t0_falling_ind]
            try:
                self.t1_falling_ind_TMR=next(x[0] for x in enumerate(self.TMR[1,self.t1_rising_ind_TMR:]) if x[1] < self.thresholdTMR) + self.t1_rising_ind_TMR
                self.fallingTimeDelayTMR = self.TMR[0,self.t1_falling_ind_TMR]-self.CPU_UP[0,self.t0_falling_ind]
            except:
                print('No TMR data available, can not calculate falling edges')
        except:
            print('Rising and/or falling edges could not be found')
        
def plotData(BD,BD_ref):
    
    #Plot traces:
    refScale=1 #scale factor for reference signals
#     plt.figure(num=None, figsize=(10, 6), dpi=140, facecolor='w', edgecolor='k')
    fig,ax=plt.subplots(num=None, figsize=(10, 6), dpi=140, facecolor='w', edgecolor='k')
    p1=plt.plot(BD.CPU_DW[0,:],BD.CPU_DW[1,:],color='blue')
    plt.plot(BD.CPU_UP[0,:],BD.CPU_UP[1,:],color='red')
    plt.plot(BD.IM[0,:],BD.IM[1,:],color='green')
    p2=plt.plot(BD_ref.CPU_DW[0,:],refScale*BD_ref.CPU_DW[1,:],color='blue',linestyle='--')
    plt.plot(BD_ref.CPU_UP[0,:],refScale*BD_ref.CPU_UP[1,:],color='red',linestyle='--')
    plt.plot(BD_ref.IM[0,:],refScale*BD_ref.IM[1,:],color='green',linestyle='--')
    plt.xlim([56,61])
    plt.xlabel('Time [us]')
    plt.legend(['CPU DOWN (Breakdown)','CPU UP (Breakdown)', 'Current (Breakdown)', 'CPU DOWN (Reference)','CPU UP (Reference)', 'Current (Reference)'])
    plt.grid()
    plt.title(BD.timeStamp)
    
    #Plot markers showing where time measurements are made on rising/falling edges
    plt.plot([BD.CPU_UP[0,BD.t0_rising_ind], BD.CPU_DW[0,BD.t1_rising_ind]],[BD.threshold, BD.threshold],color='black',linestyle='dotted')
    plt.plot([BD.CPU_UP[0,BD.t0_falling_ind], BD.CPU_DW[0,BD.t1_falling_ind]],[BD.threshold, BD.threshold],color='black',linestyle='dotted')
    
    #Textbox for time delays between upstream/downstream
    textstr = '\n'.join((
    'Rising time delay Reference/Breakdown: ' + str("{0:.3f}".format(BD_ref.risingTimeDelay)) + '/' + str("{0:.3f}".format(BD.risingTimeDelay) + ' [us]'),
    'Falling time delay Reference/Breakdown: '+ str("{0:.3f}".format(BD_ref.fallingTimeDelay)) + '/' + str("{0:.3f}".format(BD.fallingTimeDelay) + ' [us]'),
    'Time from input to point of breakdown: ' + str("{0:.3f}".format(BD.risingTimeDelay/2 - BD.fallingTimeDelay/2)) + ' [us]'))
    
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    ax.text(0.05, 0.15, textstr, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=props)
    
    #TMR and CPU plot
    try:
        fig,ax=plt.subplots(num=None, figsize=(10, 6), dpi=140, facecolor='w', edgecolor='k')
        p1=plt.plot(BD.TMR[0,:],BD.TMR[1,:],color='blue')
        plt.plot(BD.CPU_UP[0,:],BD.CPU_UP[1,:],color='red')
        plt.plot(BD.IM[0,:],BD.IM[1,:],color='green')
        p2=plt.plot(BD_ref.TMR[0,:],BD_ref.TMR[1,:],color='blue',linestyle='--')
        plt.plot(BD_ref.CPU_UP[0,:],BD_ref.CPU_UP[1,:],color='red',linestyle='--')
        plt.plot(BD_ref.IM[0,:],BD_ref.IM[1,:],color='green',linestyle='--')
        plt.xlim([56,61])
        plt.grid()
        plt.legend(['TMR (Breakdown)','CPU UP (Breakdown)', 'Current (Breakdown)', 'TMR (Reference)','CPU UP (Reference)', 'Current (Reference)'])
        textstr = '\n'.join((
        'Rising time delay Reference/Breakdown: ' + str("{0:.3f}".format(BD_ref.risingTimeDelayTMR)) + '/' + str("{0:.3f}".format(BD.risingTimeDelayTMR) + ' [us]'),
        'Falling time delay Reference/Breakdown: '+ str("{0:.3f}".format(BD_ref.fallingTimeDelayTMR)) + '/' + str("{0:.3f}".format(BD.fallingTimeDelayTMR) + ' [us]'),
        'Time from input to point of breakdown: ' + str("{0:.3f}".format(BD.risingTimeDelayTMR/2 - BD.fallingTimeDelayTMR/2)) + ' [us]'))
        
        props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
        ax.text(0.05, 0.15, textstr, transform=ax.transAxes, fontsize=14,
            verticalalignment='top', bbox=props)
    except:
        print('No TMR plot made')

def plotConsecutiveWaveforms():
    # Function for plotting multiple exported waveforms (CPU_UP)
    path0 = r'\\cern.ch\dfs\Users\o\objorkqv\Documents\My Music\2020-05-27\one_waveform_per_hour/'

    BD_array = []
    for i in range(1,17):
        BD_array.append(BreakDown(path0 + 'h' + str(i) + '/'))
    
    fig,ax=plt.subplots(num=None, figsize=(10, 6), dpi=140, facecolor='w', edgecolor='k')
    
    for i in range(0,len(BD_array)):
        plt.plot(BD_array[i].CPU_UP[0,:],BD_array[i].CPU_UP[1,:])
    
    textstr = '\n'.join(('First waveform timestamp: ' + BD_array[0].timeStamp + ', Vmax = ' + str(np.max(BD_array[0].CPU_UP[1,:])),
                        'Last waveform timestamp: ' + BD_array[-1].timeStamp + ', Vmax = ' + str(np.max(BD_array[-1].CPU_UP[1,:]))))
    
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    ax.text(0.05, 0.15, textstr, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=props)
            
    plt.xlim([56,61])
    plt.ylim([-1.5,5.5])

def main():  
    
    
    plotConsecutiveWaveforms()
    ####################### Plot waveforms: #######################
    #Filepath of three breakdown data sets (CPU_DW, CPU_UP & IM):
    filePath = r'\\cern.ch\dfs\Users\o\objorkqv\Documents\My Music\2020-05-27\bd2'+'/' 
    BD = BreakDown(filePath)
    #Filepath of three reference data sets (CPU_DW, CPU_UP & IM):
    refFilePath = r'\\cern.ch\dfs\Users\o\objorkqv\Documents\My Music\2020-05-27\ref2'+'/'
    BD_ref = BreakDown(refFilePath)
      
    print('Rising timedelay: ' + str(BD.risingTimeDelay) + 'us, (' + str(BD.CPU_UP[0,BD.t0_rising_ind]) + '; ' + str(BD.CPU_DW[0,BD.t1_rising_ind]) + ')')
    print('Falling timedelay: ' + str(BD.fallingTimeDelay) + 'us, (' + str(BD.CPU_UP[0,BD.t0_falling_ind]) + '; ' + str(BD.CPU_DW[0,BD.t1_falling_ind]) + ')')
      
    plotData(BD,BD_ref)


    plt.show()

if __name__ == "__main__":
    main()
    
    
    

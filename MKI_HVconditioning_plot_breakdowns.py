import numpy as np
import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile, join

#Save CPU_DW, CPU_UP and IM breakdown data sets from IPOC explorer to a single folder (no other files should be present)
#Save CPU_DW, CPU_UP and IM reference data sets from IPOC explorer to another, separate, single folder (no other files should be present)
#Copy these folder paths to variable 'filePath' & 'refFilePath' in main function and run

class BreakDown:
    
    def __init__(self,filePath):
        self.threshold = 2 #Rising/falling edge threshold
        self.path = filePath
        self.fileNames, self.ind, self.timeStamp=self.getFileNames()
        self.CPU_DW,self.CPU_UP,self.IM = self.getMagnetData(self.fileNames, self.ind)
        self.timeDelays()
        
    def getFileNames(self):
        #Finds the file names corresponding to the three data sets (CPU_UP, CPU_DW, IM)
        fileNames= [f for f in listdir(self.path) if isfile(join(self.path, f))]
        j=0
        for i in fileNames:
            if (i.find('.IPOC.CPU.DW')+1):
                CPU_DW_ind = j
            if (i.find('.IPOC.CPU.UP')+1):
                CPU_UP_ind = j
            if (i.find('.IPOC.IM')+1):
                IM_ind = j
            j=j+1
        ind = [CPU_DW_ind, CPU_UP_ind, IM_ind]
        timeStamp = fileNames[0][-22:-4]
        return fileNames,ind,timeStamp
        
    def getMagnetData(self,fileNames,ind):
        #Extracts the data sets from the files
        CPU_DW_path = self.path+fileNames[ind[0]]
        CPU_UP_path = self.path+fileNames[ind[1]]
        IM_path = self.path+fileNames[ind[2]]
        CPU_DW = f=np.loadtxt(CPU_DW_path,delimiter=',',skiprows=4,unpack=True,usecols=np.arange(0,2))
        CPU_UP = f=np.loadtxt(CPU_UP_path,delimiter=',',skiprows=4,unpack=True,usecols=np.arange(0,2))
        IM = f=np.loadtxt(IM_path,delimiter=',',skiprows=4,unpack=True,usecols=np.arange(0,2))
        
        return CPU_DW,CPU_UP,IM
    
    def timeDelays(self):
        #Calculates the time delays between the up/down pickup to help trace where breakdowns occur
        try:
            #Rising edges:
            self.t0_rising_ind=next(x[0] for x in enumerate(self.CPU_UP[1,:]) if x[1] > self.threshold)
            self.t1_rising_ind=next(x[0] for x in enumerate(self.CPU_DW[1,:]) if x[1] > self.threshold)
            self.risingTimeDelay = self.CPU_DW[0,self.t1_rising_ind]-self.CPU_UP[0,self.t0_rising_ind]
            #Falling edges:
            self.t0_falling_ind=next(x[0] for x in enumerate(self.CPU_UP[1,self.t0_rising_ind:]) if x[1] < self.threshold) + self.t0_rising_ind
            self.t1_falling_ind=next(x[0] for x in enumerate(self.CPU_DW[1,self.t1_rising_ind:]) if x[1] < self.threshold) + self.t1_rising_ind
            self.fallingTimeDelay = self.CPU_DW[0,self.t1_falling_ind]-self.CPU_UP[0,self.t0_falling_ind]

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
    plt.xlim([51,56])
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
    
    plt.show()




def main():  
    #Filepath of three breakdown data sets (CPU_DW, CPU_UP & IM):
    filePath = r'\\cern.ch\dfs\Users\o\objorkqv\Documents\My Music\2020-02-24\bd'+'/' 
    BD = BreakDown(filePath)
    #Filepath of three reference data sets (CPU_DW, CPU_UP & IM):
    refFilePath = r'\\cern.ch\dfs\Users\o\objorkqv\Documents\My Music\2020-02-24\ref'+'/'
    BD_ref = BreakDown(refFilePath)
    
    print('Rising timedelay: ' + str(BD.risingTimeDelay) + 'us, (' + str(BD.CPU_UP[0,BD.t0_rising_ind]) + '; ' + str(BD.CPU_DW[0,BD.t1_rising_ind]) + ')')
    print('Falling timedelay: ' + str(BD.fallingTimeDelay) + 'us, (' + str(BD.CPU_UP[0,BD.t0_falling_ind]) + '; ' + str(BD.CPU_DW[0,BD.t1_falling_ind]) + ')')
    
    
    plotData(BD,BD_ref)


if __name__ == "__main__":
    main()
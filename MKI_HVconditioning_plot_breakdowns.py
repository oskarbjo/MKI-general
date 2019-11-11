import numpy as np
import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile, join

#Save CPU_DW, CPU_UP and IM breakdown data sets from IPOC explorer to a single folder (no other files should be present)
#Save CPU_DW, CPU_UP and IM reference data sets from IPOC explorer to another, separate, single folder (no other files should be present)
#Copy these folder paths to variable 'filePath' & 'refFilePath' in main function and run

class BreakDown:
    
    def __init__(self,filePath):
        self.path = filePath
        self.fileNames, self.ind, self.timeStamp=self.getFileNames()
        self.CPU_DW,self.CPU_UP,self.IM = self.getMagnetData(self.fileNames, self.ind)
        
        
    def getFileNames(self):
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
        CPU_DW_path = self.path+fileNames[ind[0]]
        CPU_UP_path = self.path+fileNames[ind[1]]
        IM_path = self.path+fileNames[ind[2]]
        CPU_DW = f=np.loadtxt(CPU_DW_path,delimiter=',',skiprows=4,unpack=True,usecols=np.arange(0,2))
        CPU_UP = f=np.loadtxt(CPU_UP_path,delimiter=',',skiprows=4,unpack=True,usecols=np.arange(0,2))
        IM = f=np.loadtxt(IM_path,delimiter=',',skiprows=4,unpack=True,usecols=np.arange(0,2))
        
        return CPU_DW,CPU_UP,IM
    
def plotData(BD,BD_ref):
    plt.figure()
    p1=plt.plot(BD.CPU_DW[0,:],BD.CPU_DW[1,:],color='blue')
    plt.plot(BD.CPU_UP[0,:],BD.CPU_UP[1,:],color='red', label='_nolegend_')
    plt.plot(BD.IM[0,:],BD.IM[1,:],color='green', label='_nolegend_')
    p2=plt.plot(BD_ref.CPU_DW[0,:],BD_ref.CPU_DW[1,:],color='blue',linestyle='--')
    plt.plot(BD_ref.CPU_UP[0,:],BD_ref.CPU_UP[1,:],color='red',linestyle='--', label='_nolegend_')
    plt.plot(BD_ref.IM[0,:],BD_ref.IM[1,:],color='green',linestyle='--', label='_nolegend_')
    plt.xlim([51,56])
    plt.xlabel('Time [us]')
    plt.legend(['Breakdown','Reference'])
    plt.grid()
    plt.title(BD.timeStamp)
    plt.show()


def main():  
    #Filepath of three breakdown data sets (CPU_DW, CPU_UP & IM):
    filePath = r'\\cern.ch\dfs\Users\o\objorkqv\Documents\My Music\2019-11-10'+'/' 
    BD = BreakDown(filePath)
    #Filepath of three reference data sets (CPU_DW, CPU_UP & IM):
    refFilePath = r'\\cern.ch\dfs\Users\o\objorkqv\Documents\My Music\2019-11-11_2000ns_ref_waveform'+'/'
    BD_ref = BreakDown(refFilePath)
    plotData(BD,BD_ref)
    
    
if __name__ == "__main__":
    main()


import numpy as np


def getNumberofPulses():
    
    ############ USER INPUT: ##############
    stepMin = 0.01e3      # V
    stepMax = 0.3e3       # V
    Ustart = 47.0e3      # V
    Umax = 57.1e3         # V
    multiplier = 531.2    # V
    exponent = 6.28e-5
    Npulse_per_step = 2
    RmpPulseMax = 0
    #######################################
    numberOfPulses=0
    PFNvoltage = Ustart
    while(PFNvoltage < Umax):
        numberOfPulses = numberOfPulses+Npulse_per_step
        DeltaPFNvoltage = multiplier * np.exp(-exponent * PFNvoltage)
        if DeltaPFNvoltage > stepMax:
            DeltaPFNvoltage = stepMax
        if DeltaPFNvoltage < stepMin:
            DeltaPFNvoltage = stepMin
        PFNvoltage = PFNvoltage + DeltaPFNvoltage
    numberOfPulses = numberOfPulses + RmpPulseMax
    
    return numberOfPulses


def NACOND_code(Umax,multiplier,exponent,Npulse_per_step): 
    P_RmpVMax = Umax
    P_LogRampMultip = multiplier
    P_LogRampExp = exponent
    P_RmpPulseOriginalValue = Npulse_per_step
    P_RmpPulseMax = 0
    compt = 0
    Utest = 0
    while Utest <= P_RmpVMax:
        compt = compt + 1
        Utest = Utest + ((P_LogRampMultip*np.exp((-1)*P_LogRampExp*Utest*1000))/1000)
#         print(Utest)
        
    retour = (compt)*P_RmpPulseOriginalValue+P_RmpPulseMax
    
    return retour



def main():
    
    
    numberOfPulses = getNumberofPulses()
    print('Number of pulses during ramp: ' + str(numberOfPulses))


if __name__ == "__main__":
    main()
    
    
    
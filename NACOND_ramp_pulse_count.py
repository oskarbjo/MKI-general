

import numpy as np


def getNumberofPulses(stepMin,stepMax,Ustart,Umax,multiplier,exponent,Npulse_per_step):
    
    j=0
    PFNvoltage = Ustart
    while(PFNvoltage < Umax):
        j = j+Npulse_per_step
        DeltaPFNvoltage = multiplier * np.exp(-exponent * PFNvoltage)
        if DeltaPFNvoltage > stepMax:
            DeltaPFNvoltage = stepMax
        if DeltaPFNvoltage < stepMin:
            DeltaPFNvoltage = stepMin
        PFNvoltage = PFNvoltage + DeltaPFNvoltage
    
    return j

def main():
    
    #USER INPUT:
    stepMin = 0.01e3      # V
    stepMax = 0.3e3       # V
    Ustart = 47.00e3      # V
    Umax = 57.2e3         # V
    multiplier = 531.2    # V
    exponent = 6.28e-5
    Npulse_per_step = 2
    
    numberOfPulses = getNumberofPulses(stepMin,stepMax,Ustart,Umax,multiplier,exponent,Npulse_per_step)
    print('Number of pulses during ramp: ' + str(numberOfPulses))

if __name__ == "__main__":
    main()
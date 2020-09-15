import numpy as np
import matplotlib.pyplot as plt


def plotSimulationResults():
    path=r"E:\Ansys\Lorena MKI bakeout\bakeout_sim_data.csv"
    data=np.loadtxt(path,skiprows=0,dtype='str', delimiter=',', unpack=True, encoding="utf8")
    data=np.double(data)
    plt.figure()
    plt.plot(data[0,:]/3600,data[3,:],label='Tank')
    plt.plot(data[0,:]/3600,data[1,:],label='Yoke 1')
    plt.plot(data[0,:]/3600,data[5,:],label='Yoke 5')
    plt.plot(data[0,:]/3600,data[2,:],label='Damper ferrite')
    plt.plot(data[0,:]/3600,data[4,:],label='GND side plate')
    plt.legend()
    plt.xlabel('Time [hours]')
    plt.ylabel('Temperature [C]')
    plt.grid()
    plt.show()
    print('')

def tempRamp():
    T1=np.arange(25,300,5)
    t1=np.round(np.linspace(0,60*60*(len(T1)-1),len(T1)))
    
    
    t2=np.round(np.linspace(t1[-1],t1[-1]+72*60*60,72))
    T2=np.ones_like(t2)*300
    
    T3=np.arange(295,145,-5)
    t3=np.round(np.linspace(t2[-1]+3600,t2[-1]+3600+60*60*(len(T3)-1),len(T3)))
    
    
    t4=np.round(np.linspace(t3[-1],t3[-1]+30*60*60,30))
    T4=np.ones_like(t4)*150
    
    T5=np.arange(145,20,-5)
    t5=np.round(np.linspace(t4[-1]+3600,t4[-1]+3600+60*60*(len(T5)-1),len(T5)))
    
    t = []
    t=np.append(t,t1)
    t=np.append(t,t2)
    t=np.append(t,t3)
    t=np.append(t,t4)
    t=np.append(t,t5)
    
    T = []
    T=np.append(T,T1)
    T=np.append(T,T2)
    T=np.append(T,T3)
    T=np.append(T,T4)
    T=np.append(T,T5)
    
    
    plt.figure()
    plt.plot(t,T)
    
    
    for i in t:
        print(i)
    
    
    plt.show()
    
plotSimulationResults()
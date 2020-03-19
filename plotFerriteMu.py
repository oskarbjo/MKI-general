import numpy as np
from os import listdir
from os.path import isfile, join
import matplotlib.pyplot as plt

path = r"C:\Users\objorkqv\cernbox\Documents\Measurements\Ferrite aga measurements\CMD5005_csv.csv"
data25C = np.loadtxt(path,delimiter=',',unpack=True,usecols=[0,1,2],skiprows=1)
data50C = np.loadtxt(path,delimiter=',',unpack=True,usecols=[11,12,13],skiprows=1)
data75C = np.loadtxt(path,delimiter=',',unpack=True,usecols=[16,17,18],skiprows=1)
data100C = np.loadtxt(path,delimiter=',',unpack=True,usecols=[21,22,23],skiprows=1)

plt.figure()
plt.semilogx(data25C[0,:],data25C[2,:])
plt.semilogx(data50C[0,:],data50C[2,:])
plt.semilogx(data75C[0,:],data75C[2,:])
plt.semilogx(data100C[0,:],data100C[2,:])
plt.legend(['25 C','50 C','75 C','100 C'])
plt.show()
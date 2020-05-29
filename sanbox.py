import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
import signal_toolbox



def main(): 
    x = [4.20044,
        4.26636,
        4.33838,
        4.40002,
        4.41101,
        4.42444,
        4.50378,
        4.57947,
        4.66003,
        4.66003,
        4.76807,
        4.7821,
        4.80164,
        4.81018,
        4.82788,
        4.83704]
    y = [42.79,
        43.39,
        44.14,
        44.74,
        44.89,
        45,
        45.75,
        45.6,
        47.25,
        48,
        48.34,
        48.47,
        48.59,
        48.72,
        48.84,
        48.97]
    plt.figure()
    plt.plot(x,y)
    plt.grid()
    plt.show()
    
if __name__ == "__main__":
    main()
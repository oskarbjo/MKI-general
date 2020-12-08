import numpy as np
from matplotlib import pyplot as plt

airgap = [1.5, 1.75, 2.0, 2.25, 2.5]
Efield = np.divide([1.613529e4, 1.425146e4, 1.2783671e4, 1.1608709e4, 1.0647100e4],1e3)

step = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]
stepField1p5 = [16135,23743,30390,38721,42051,44804]
stepField2p0 = [12783, 20566, 24274, 28320, 30816, 34873]


plt.figure()
plt.plot(airgap,Efield)
plt.ylabel('Field [kV/mm]')
plt.xlabel('Air gap size [mm]')
plt.grid()

plt.figure()
plt.plot(step,stepField1p5)
plt.plot(step,stepField2p0)
plt.ylabel('Peak field [kV/mm]')
plt.xlabel('HV bus bar step [mm]')
plt.legend(['1.5 mm nominal','2.0 mm nominal'])
plt.grid()

plt.show()


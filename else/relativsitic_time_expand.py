import numpy as np
import matplotlib.pyplot as plt

ratio=np.linspace(-1,1,1000)  #坐标系速度比光速

tt=1/np.sqrt(1-ratio**2)  #时间速度关系

plt.figure()

ax=plt.subplot(111)
ax.plot(ratio,tt)

ax.set_xlabel('u/c',fontsize=20)
ax.set_ylabel('t/t0',fontsize=20)
ax.set_title('the relation between time expand and velocity',fontsize=20)

ax.tick_params(labelsize=20)

ax.text(0,2,'c is the velocity of light, t0 is the eigentime',fontsize=20)

plt.show()

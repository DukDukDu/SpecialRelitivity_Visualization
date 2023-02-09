#相对论速度质量关系

import numpy as np
import matplotlib.pyplot as plt

ratio=np.linspace(0,1,1000)  #比值为物体速度v/c

mm=1/np.sqrt(1-ratio**2)  #mm为物体质量与静止质量比值

plt.figure()

ax=plt.subplot(111)

ax.plot(ratio,mm,'--')  #绘制速度质量关系曲线

x0=[1 for i in np.arange(0,20,0.001)]  #绘制切线
ax.plot(x0,np.arange(0,20,0.001),'-.')

ax.set_xlabel('v/c',fontsize=20)
ax.set_ylabel('m/m0',fontsize=20)
ax.set_title('the relation between mass and velocity',fontsize=20)

ax.tick_params(labelsize=20)

ax.text(0.1,1,'c is the velocity of light, and m0 is rest mass',fontsize=20)
ax.text(1,15,'tangent line',fontsize=20)

plt.show()

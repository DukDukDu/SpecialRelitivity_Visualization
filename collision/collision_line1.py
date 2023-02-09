#两个质量相同的小球，一个小球静止，一个小球以v碰向另一个小球发生完全非弹性碰撞

import matplotlib.pyplot as plt
import numpy as np

ratio=np.linspace(0,1,1000)  #比值为v/c

Vc=ratio/(1+np.sqrt(1-ratio**2)) #碰撞后的速度

#碰撞后速度的绘制

plt.figure()

ax1=plt.subplot(121)

ax1.plot(ratio,Vc)
ax1.set_ylabel('V/c',fontsize=25)
ax1.set_xlabel('v/c',fontsize=25)
ax1.set_title('velocity after collision',fontsize=25)
ax1.tick_params(labelsize=20)

Mm=np.sqrt(2*(1+1/np.sqrt(1-ratio**2)))  #碰撞后的静止质量

ax2=plt.subplot(122)

ax2.plot(ratio,Mm)
ax2.set_ylabel('$M_0/m_0$',fontsize=25)
ax2.set_xlabel('v/c',fontsize=25)
ax2.set_title('mass after collision',fontsize=25)
ax2.tick_params(labelsize=20)

T_before=1/np.sqrt(1-ratio**2)-1  #碰撞前动能
T_after=1/np.sqrt(1-ratio**2)+1-Mm  #碰撞后动能

deltaT=Mm-2  #损失的动能

deltaE=Mm-2 #增加的静止能量

#动能相关图像的描绘

plt.figure() 
ax=plt.subplot(111)

ax.plot(ratio,T_before,'--',lw=2,label='$ET/E_0 before collision$')
ax.plot(ratio,T_after,'-.',lw=2,label='$ET/E_0 after collision$')
ax.plot(ratio,deltaT,':',lw=2,label='$delta ET/E_0$')
ax.plot(ratio,deltaE,'+',lw=1,label='$delta E_0/E_0$')

ax.set_xlabel('v/c',fontsize=25)
ax.set_ylabel('$E_0$',fontsize=25)

ax.legend(loc='upper left',frameon=True,fontsize=20)

ax.text(0.1,10.0,'$E_0=m_0c^2$',fontsize=20)

ax.tick_params(labelsize=20)
plt.show()

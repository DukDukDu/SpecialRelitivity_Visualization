#相对论动量 速度 能量关系

import numpy as np
import matplotlib.pyplot as plt

ratio1=np.linspace(0,1,1000)  #ratio1代表v/c

E_r=1/np.sqrt(1-ratio1**2)  #能量与速度的关系

plt.figure()

ax=plt.subplot(121)

ax.plot(ratio1,E_r,'-.')  #绘制能量速度关系

ax.set_xlabel('v/c',fontsize=20)
ax.set_ylabel('$E/(m0*c^2)$',fontsize=20)
ax.set_title('the relation between energy and velocity',fontsize=20)
ax.text(0.1,2,'c is the velocity of light,m0 is the mass',fontsize=20)

ax.tick_params(labelsize=20)

ratio2=np.linspace(0,5,1000)  #ratio2代表 p/(m0*c)

E_E=np.sqrt(1+ratio2**2)  #能量与动量的关系

axp=plt.subplot(122)

axp.plot(ratio2,E_E,'--',label='$E/(m0*c^2)$')  #绘制能量与动量关系
axp.plot(ratio2,ratio2,'-.',label='m0=0')

axp.set_xlabel('$p/(m0*c) or p$',fontsize=20)
axp.set_ylabel('$E/(m0*c^2) or E/c$',fontsize=20)
axp.set_title('the raltion between energy and momentum',fontsize=20)

axp.tick_params(labelsize=20)

axp.legend(loc='upper left',frameon=True,fontsize=20)

plt.show()

#粒子衰变问题的相对论研究

import numpy as np
import matplotlib.pyplot as plt
from pylab import *

ratiom10=np.linspace(0,1,1000)

#定义衰变能量函数

def F(ratiom10,ratiom20):
    cond=[False if (i>1-ratiom20) else True for i in ratiom10]  #分段条件
    y=cond*(1+ratiom10**2-ratiom20**2)/2+ratiom10*(ratiom10>1-ratiom20)
    return y

plt.figure()
ax1=plt.subplot(131)  #静止粒子衰变后的能量与静止质量的关系

ax1.plot(ratiom10,F(ratiom10,0),'-.',label='m20/m0=0')
ax1.plot(ratiom10,F(ratiom10,0.25),'-.',label='m20/m0=0.25')
ax1.plot(ratiom10,F(ratiom10,0.5),'-.',label='m20/m0=0.5')
ax1.plot(ratiom10,F(ratiom10,0.75),'-.',label='m20/m0=0.75')
ax1.plot(ratiom10,F(ratiom10,1),'-.',label='m20/m0=1')

ax1.legend(loc='upper left',frameon=True,fontsize=20)

ax1.annotate('boundary line',xy=(0.3,0.2),xytext=(0.4,0.1),arrowprops=dict(facecolor='black',shrink=0.05))  #指示箭头的添加

ax1.set_xlabel('m10/m0',fontsize=25)
ax1.set_ylabel('$E1/(m0*c^2)$',fontsize=25)
ax1.set_title('the relation between energy\nafter decay and rest mass',fontsize=25)
ax1.tick_params(labelsize=20)

#定义衰变后的动量函数

def P(ratiom10,ratiom20):
    p=np.sqrt(((1+ratiom10)**2-ratiom20**2)*((1-ratiom10)**2-ratiom20**2))
    return p

ax2=plt.subplot(132)  #静止粒子衰变后的动量与静止质量的关系

ax2.plot(ratiom10,P(ratiom10,0),'-.',label='m20/m=0')
ax2.plot(ratiom10,P(ratiom10,0.25),'-.',label='m20/m0=0.25')
ax2.plot(ratiom10,P(ratiom10,0.5),'-.',label='m20/m0=0.5')
ax2.plot(ratiom10,P(ratiom10,0.75),'-.',label='m20/m0=0.75')
ax2.plot(ratiom10,P(ratiom10,1),'-.',label='m20/m0=1')

ax2.legend(loc='upper right',frameon=True,fontsize=20)

ax2.set_xlabel('m10/m0',fontsize=25)
ax2.set_ylabel('$p1/(m0*c)$',fontsize=25)
ax2.set_title('the relation between momentum\nafter decay and rest mass',fontsize=25)
ax2.tick_params(labelsize=20)

#定义衰变后的动量函数

def V(ratiom10,ratiom20):
    up=sqrt(((1+ratiom10)**2-ratiom20**2)*((1-ratiom10)**2-ratiom20**2))
    down=1+ratiom10**2-ratiom20**2
    v=up/down
    return v

ax3=plt.subplot(133)  #静止粒子衰变后的速度与静止质量的关系

ax3.plot(ratiom10,V(ratiom10,0),'-.',label='m20/m=0')
ax3.plot(ratiom10,V(ratiom10,0.25),'-.',label='m20/m0=0.25')
ax3.plot(ratiom10,V(ratiom10,0.5),'-.',label='m20/m0=0.5')
ax3.plot(ratiom10,V(ratiom10,0.75),'-.',label='m20/m0=0.75')
ax3.plot(ratiom10,V(ratiom10,1),'-.',label='m20/m0=1')

ax3.legend(loc='upper right',frameon=True,fontsize=20)

ax3.set_xlabel('m10/m0',fontsize=25)
ax3.set_ylabel('v1/c',fontsize=25)
ax3.set_title('the relation between velocity\nafter decay and rest mass',fontsize=25)
ax3.tick_params(labelsize=20)

plt.show()

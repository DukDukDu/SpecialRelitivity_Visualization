import numpy as np
import matplotlib.pyplot as plt

ratio=np.linspace(-1,1,1000)  #比例代表坐标系速度u/c

ll=np.sqrt(1-ratio**2)  #ll为测量长度与本征长度的比值

plt.figure()

ax=plt.subplot(111)  #绘制长度收缩曲线
ax.plot(ratio,ll,'--')
x0=[-1 for i in np.arange(0,1,0.001)]
ax.plot(x0,np.arange(0,1,0.001),'-.')


ax.set_xlabel('u/c',fontsize=20)
ax.set_ylabel('l/l0',fontsize=20)
ax.set_title('length shrink',fontsize=20)

ax.tick_params(labelsize=20)

ax.text(0,0.5,'c is the velocity of light, l0 is the eigenlength',fontsize=20)
ax.text(-1,1,'tangent line',fontsize=20)

plt.show()

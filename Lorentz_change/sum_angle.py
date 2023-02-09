#绘制不同坐标系间速度变换三角形的內角和

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
import matplotlib.animation as animation

ratio10=np.linspace(-1,1,1000)  #比值为坐标系约化速度u/c

ratio20=np.linspace(-1,1,1000)  #比值为一个坐标系中的物体约化速度v/c

ratio1,ratio2=np.meshgrid(ratio10,ratio20)

alpha=np.arctan(1/(ratio1/(ratio2*np.sqrt(1-ratio1**2))))  #变换角alpha

beta=np.arctan(1/(ratio2/(ratio1*np.sqrt(1-ratio2**2))))  #变换角beta

angle=alpha+beta+np.pi/2  #变换三角形內角和

fig=plt.figure()

ax=plt.subplot(111,projection='3d')

surf=ax.plot_surface(ratio1,ratio2,angle,cmap=cm.coolwarm,linewidth=2,antialiased=False)  #绘制內角和曲面

ax.set_xlabel('u/c',fontsize=20)
ax.set_ylabel('v/c',fontsize=20)
ax.set_zlabel('sum of angle',fontsize=20)

ax.set_title('sum of the angle',fontsize=20)

def rotate(angle):
    ax.view_init(azim=angle)

rot_animation=animation.FuncAnimation(fig=fig,func=rotate,frames=np.arange(0,3600+2,8),interval=50,repeat=True,blit=False)  #绘制动画

fig.colorbar(surf,shrink=0.5,aspect=3)

plt.show()

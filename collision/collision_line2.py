#两个质量相同的小球分别以v1,v2速度运动然后发生相对论完全非弹性碰撞

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
import matplotlib.animation as animation
from matplotlib.widgets import Slider

beta11=np.linspace(-1,1,1000)  #设置v1/c的范围
beta21=np.linspace(-1,1,1000)  #设置v2/c的范围

beta1,beta2=np.meshgrid(beta11,beta21)

Vc=(beta1/np.sqrt(1-beta1**2)+beta2/np.sqrt(1-beta2**2))/(1/np.sqrt(1-beta1**2)+1/np.sqrt(1-beta2**2))  #推导出的末态速度

fig=plt.figure()
ax1=plt.subplot(111,projection='3d')
ax1.plot_surface(beta1,beta2,Vc)  #绘制三维速度平面

ax1.set_xlabel('v1/c',fontsize=20)
ax1.set_ylabel('v2/c',fontsize=20)
ax1.set_zlabel('v/c',fontsize=20)
ax1.set_title('velocity after collision',fontsize=25)

def rotate1(angle):
      ax1.view_init(angle)
      
rot_animation1=animation.FuncAnimation(fig=fig,func=rotate1,frames=np.arange(0,3600+2,8),interval=50,repeat=True,blit=False)  #添加动画

ax1.contourf(beta1,beta2,Vc,zdir='x',offset=-1,cmap=cm.coolwarm)  #作出投影，更加直观看出速度变化

Mm=np.sqrt((np.sqrt((1+beta1)/(1-beta1))+np.sqrt((1+beta2)/(1-beta2)))*(np.sqrt((1-beta1)/(1+beta1))+np.sqrt((1-beta2)/(1+beta2))))  #推导出的末态静止质量

fig2=plt.figure()
ax2=plt.subplot(111,projection='3d')
ax2.plot_surface(beta1,beta2,Mm)  #绘制三维静止质量平面

ax2.set_xlabel('v1/c',fontsize=20)
ax2.set_ylabel('v2/c',fontsize=20)
ax2.set_zlabel('$M_0/m_0$',fontsize=20)
ax2.set_title('mass after collision',fontsize=25)  


ax2.contourf(beta1,beta2,Mm,zdir='x',offset=-1,cmap=cm.coolwarm)  #作出投影，更加直观看出质量变化

def rotate2(angle):
      ax2.view_init(angle)
      
rot_animation2=animation.FuncAnimation(fig=fig2,func=rotate2,frames=np.arange(0,3600+2,8),interval=50,repeat=True,blit=False)  #添加动画

#绘制Slider图像

#碰撞后速度函数的定义
def spv(betas):
    ratios=np.linspace(-1,1,1000)
    Vvs=(ratios/np.sqrt(1-ratios**2)+betas/np.sqrt(1-betas**2))/(1/np.sqrt(1-ratios**2)+1/np.sqrt(1-betas**2))
    return ratios,Vvs

figs=plt.figure()

axs=plt.subplot(111)

ratios,Vs=spv(0)

l,=plt.plot(ratios,Vs)

axcolor='lightgoldenrodyellow'

oms=plt.axes([0.25,0.15,0.65,0.03],facecolor=axcolor)

soms=Slider(oms,r'$v_2/c$',-1,1,valinit=0)

def update(val):
    s=soms.val
    ratios,Vs=spv(s)
    l.set_ydata(Vs)
    l.set_xdata(ratios)
    figs.canvas.draw_idle()

soms.on_changed(update)  #Slider绘制

axs.set_xlabel('$v_1/c$')
axs.set_ylabel('$v/c$')

#碰撞后静止质量函数的定义
def spv2(betas):
    ratio2s=np.linspace(-1,1,1000)
    Mms=np.sqrt((np.sqrt((1+ratio2s)/(1-ratio2s))+np.sqrt((1+betas)/(1-betas)))*(np.sqrt((1-ratio2s)/(1+ratio2s))+np.sqrt((1-betas)/(1+betas))))
    return ratio2s,Mms

fig2s=plt.figure()

ax2s=plt.subplot(111)

ratio2s,Ms=spv2(0)

l2,=plt.plot(ratio2s,Ms)

om2s=plt.axes([0.25,0.15,0.65,0.03],facecolor=axcolor)

som2s=Slider(om2s,r'$v_2/c$',-1,1,valinit=0)


def update2(val):
    s2=som2s.val
    ratio2s,Ms=spv2(s2)
    l2.set_ydata(Ms)
    l2.set_xdata(ratio2s)
    fig2s.canvas.draw_idle()

som2s.on_changed(update2)  #Slider绘制

ax2s.set_ylabel('$M_0/m_0$')
ax2s.set_xlabel('$v_1/c$')

plt.show()

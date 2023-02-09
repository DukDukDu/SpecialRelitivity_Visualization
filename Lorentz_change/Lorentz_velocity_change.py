import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as axes3d
import matplotlib.animation as animation
from matplotlib import cm
from pylab import *

#设置参数

c=3*1e8
u_0=np.arange(-1*c,1*c,c*0.01)
u=u_0/c
v_0=np.arange(-1*c,1*c,c*0.01)
v=v_0/c
U,V=np.meshgrid(u,v)

fig1=plt.figure() 

ax1=plt.subplot(131,projection='3d')  #绘制X分量速度的变换曲面
ax1.plot_surface(U,V,(V-U)/(1-V*U))  

ax1.set_xlabel('$u/c$')
ax1.set_ylabel('$v_x/c$')
ax1.set_zlabel('$v_xs/c$')
ax1.set(title='Lorentz velocity change--Vx')

def rotate1(angle):
    ax1.view_init(azim=angle)

rot_animation1=animation.FuncAnimation(fig=fig1,func=rotate1,frames=np.arange(0,3600+2,8),interval=50,repeat=True,blit=False)  #添加动画

y_theta_0=0*np.sqrt(1-U**2)/(1-V*U)  #Y分量

ax2=plt.subplot(132,projection='3d')  #取特殊情况Vz=0,theta=0时Y分量的速度变换曲面
ax2.plot_surface(U,V,y_theta_0)

ax2.set_xlabel('$u/c$')
ax2.set_ylabel('$v_x/c$')
ax2.set_zlabel('$v_ys/c$')
ax2.set(title='Lorentz velocity change--Vy(with theta=0)')

def rotate2(angle):
    ax2.view_init(azim=angle)

rot_animation2=animation.FuncAnimation(fig=fig1,func=rotate2,frames=np.arange(0,3600+2,8),interval=50,repeat=True,blit=False)  #添加动画


y_theta_90=V*np.sqrt(1-U**2)/(1-U/c)  #Y分量

ax3=plt.subplot(133,projection='3d')  #取特殊情况Vz=0,theta=90时Y分量的速度变换曲面
ax3.plot_surface(U,V,y_theta_90)

ax3.set_xlabel('$u/c$')
ax3.set_ylabel('$v_x/c$')
ax3.set_zlabel('$v_ys/c$')
ax3.set(title='Lorentz velocity change--Vy(with theta=90)')

def rotate3(angle):
    ax3.view_init(azim=angle)

rot_animation3=animation.FuncAnimation(fig=fig1,func=rotate3,frames=np.arange(0,3600+2,8),interval=50,repeat=True,blit=False)  #添加动画


fig2=plt.figure()

VV1=np.sqrt(1-(1-V*V)*(1-U*U)/(1-V*U)**2)  #速度大小

ax4=plt.subplot(121,projection='3d')  #取特殊情况z=0,theta=0时速度变换曲面
ax4.plot_surface(U,V,VV1)

ax4.set_xlabel('$u/c$')
ax4.set_ylabel('$v_x/c$')
ax4.set_zlabel('$v_s/c$')
ax4.set(title='Lorentz velocity change--V(with theta=0)')

def rotate4(angle):
    ax4.view_init(angle)

rot_animation4=animation.FuncAnimation(fig=fig2,func=rotate4,frames=np.arange(0,3600+2,8),interval=50,repeat=True,blit=False)  #添加动画

VV2=np.sqrt(1-(1-V*V)*(1-U*U)/1) #速度大小

ax5=plt.subplot(122,projection='3d')  #取特殊情况Vz=0,theta=90时速度变换曲面
ax5.plot_surface(U,V,VV2)

ax5.set_xlabel('$u/c$')
ax5.set_ylabel('$v_x/c$')
ax5.set_zlabel('$v_s/c$')
ax5.set(title='Lorentz velocity change--V(with theta=90)')

def rotate5(angle):
    ax5.view_init(angle)

rot_animation5=animation.FuncAnimation(fig=fig2,func=rotate5,frames=np.arange(0,3600+2,8),interval=50,repeat=True,blit=False)  #添加动画


thetas=np.arctan((V*np.sqrt(1-U**2))/-U)  #方向角的大小，选取特殊情况theta=90,Vz=0

fig3=plt.figure()  #方向角的变化曲面绘制

ax6=plt.subplot(111,projection='3d')

ax6.plot_surface(U,V,thetas)

ax6.set_xlabel('$u/c$')
ax6.set_ylabel('$v/c$')
ax6.set(title='direction angle(with theta=90)')

def rotate6(angle):
    ax6.view_init(angle)

rot_animation6=animation.FuncAnimation(fig=fig3,func=rotate6,frames=np.arange(0,3600+2,8),interval=50,repeat=True,blit=False)  #添加动画

plt.show()

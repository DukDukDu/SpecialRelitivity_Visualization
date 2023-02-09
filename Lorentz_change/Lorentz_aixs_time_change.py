import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as axes3d
import matplotlib.animation as animation

#设置参数

c=3*1e8
t0=20.
u1=0.1*c
u2=0.9*c
x=np.arange(0,2*c*t0,c*t0*0.005)
x_01=x/(c*t0)
t=np.arange(0,2*t0,0.1)
t_01=t/t0
x_0,t_0=np.meshgrid(x_01,t_01)

fig1=plt.figure()  #洛伦兹空间变换平面

def rotate(angle):
    ax1.view_init(azim=angle)

plt.suptitle('Lorentz axis change')

ax1=plt.subplot(121,projection='3d')
ax1.plot_surface(t_0,x_0,(x_0-t_0*u1/c)/np.sqrt(1-(u1/c)**2))  #坐标系以0.1倍光速运动时的情况

ax1.set_xlabel('$t/t_0$')
ax1.set_ylabel('$x/(c*t_0)$')
ax1.set_zlabel('$x_S/(c*t_0)$')
ax1.set(title='$u=0.1*c$')

rotate_animation=animation.FuncAnimation(fig=fig1,func=rotate,frames=np.arange(0,3600+2,8),interval=50,repeat=True,blit=False)


def rotate2(angle):
    ax2.view_init(azim=angle)

ax2=plt.subplot(122,projection='3d')
ax2.plot_surface(t_0,x_0,(x_0-t_0*u2/c)/np.sqrt(1-(u2/c)**2))  #坐标系以0.9倍光速运动时的的情况

ax2.set_xlabel('$t/t_0$')
ax2.set_ylabel('$x/(c*t_0)$')
ax2.set_zlabel('$x_S/(c*t_0)$')
ax2.set(title='$u=0.9*c$')

rotate_animation2=animation.FuncAnimation(fig=fig1,func=rotate2,frames=np.arange(0,3600+2,8),interval=50,repeat=True,blit=False)  #添加动画


fig2=plt.figure()  #洛伦兹时间变换平面

plt.suptitle('Lorentz time change')

ax3=plt.subplot(121,projection='3d')
ax3.plot_surface(t_0,x_0,(t_0-x_0*u1/c)/np.sqrt(1-(u1/c)**2))  #坐标系以0.1倍光速运动时的情况

ax3.set_xlabel('$t/t_0$')
ax3.set_ylabel('$x/(c*t_0)$')
ax3.set_zlabel('$t_s/t0$')
ax3.set(title='$u=0.1*c$')

def rotate3(angle):
    ax3.view_init(azim=angle)

rotate_animation3=animation.FuncAnimation(fig=fig2,func=rotate3,frames=np.arange(0,3600+2,8),interval=50,repeat=True,blit=False)  #添加动画


ax4=plt.subplot(122,projection='3d')
ax4.plot_surface(t_0,x_0,(t_0-x_0*u2/c)/np.sqrt(1-(u2/c)**2))  #坐标系以0.9倍光速运动时的的情况

ax4.set_xlabel('$t/t_0$')
ax4.set_ylabel('$x/(c*t_0)$')
ax4.set_zlabel('$t_s/t0$')
ax4.set(title='$u=0.9*c$')

def rotate4(angle):
    ax4.view_init(azim=angle)

rotate_animation4=animation.FuncAnimation(fig=fig2,func=rotate4,frames=np.arange(0,3600+2,8),interval=50,repeat=True,blit=False)  #添加动画


plt.show()

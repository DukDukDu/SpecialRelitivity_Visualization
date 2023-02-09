from matplotlib import pyplot as plt
from numpy import linspace
from matplotlib import font_manager as fm
from matplotlib import figure

m0=9.11e-31 #电子的质量
e=1.6e-19 #元电荷的电荷量
c=3e8 #光速
e0=m0*c**2
e0=e0/e/1e6 #单位换算
T=linspace(0,6,400)

u=9*(1-e0**2/(T+e0)**2) #u是相对论体系下电子速度的平方
u0=2*T/e0*9 #经典力学体系下电子速度的平方

figure,ax=plt.subplots()
plt.ylim((0,10))

plt.annotate('$v^2=2T/m0$',xy=(0.2,8),xytext=(1.,10),arrowprops=dict(facecolor='black',shrink=0.05),fontsize=20)  #指示箭头

ax.plot(T,u,label="Relativistic system")

ax.plot(T,u0,label="Classical mechanical system")

y0=[9 for i in T]  #渐近线
ax.plot(T,y0,'--')

ax.plot(2.123,8.55,'go',label="experimental data") #实验数据
ax.plot(0.487,6.71,'go')
ax.plot(0.049,1.48,'go')
ax.plot(0.185,4.20,'go')

ax.set_xlabel('T/MeV',fontsize=20)
ax.set_ylabel('$v^2/(10^(16)m^2s^(-2))$',fontsize=20)
ax.set_title('Bertozzi experiment',fontsize=20)

ax.text(3,9.3,'tangent line',fontsize=20)

ax.tick_params(labelsize=20)

ax.legend(loc='lower right',frameon=True,fontsize=20)

plt.show()






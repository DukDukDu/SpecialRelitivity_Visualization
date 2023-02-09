#相对论条件下两球的完全非弹性碰撞，两球均有初速度

from vpython import *    
import numpy as np

s1=canvas(width=1200,height=400,background=color.white,center=vector(1,0,0) ,align="left") 
s1.camera.pos=vector(0,1,1) #设置摄像机位置
s1.camera.axis=vector(0,-1,-1)  #设置摄像机方位

ball1=sphere(pos=vector(0,0,0),radius=0.05,color=color.red) 
ball2=sphere(pos=vector(1,0,0),radius=0.05,color=color.blue)  

#定义曲线显示窗口
g1=graph(width=400,height=300,xtitle="时间/s",ytitle="速度/m/s" ,align="left"  )  
v1curve=gcurve(color=color.red,graph=g1,label="v1 ")  #定义ball1速度曲线
v2curve=gcurve(color=color.blue,graph=g1,label="v2 ")  #定义ball2速度曲线

#定义动能显示窗口
g2=graph(width=400,height=300,xtitle="时间/s",ytitle="动能/J"  ,align="left" )  
EK1curve=gcurve(color=color.red,graph=g2,label="EK1 ")  #定义ball1动能曲线
EK2curve=gcurve(color=color.blue,graph=g2,label="EK2 ")  #定义ball2动能曲线
EKcurve=gcurve(color=color.black,graph=g2,label="EK ")  #定义总动能曲线

#定义动量曲线显示窗口
g3=graph(width=400,height=300,xtitle="时间/s",ytitle="动量/kg*m/s"  ,align="left" )  
P1curve=gcurve(color=color.red,graph=g3,label="P1 ")  #定义ball1动量曲线
P2curve=gcurve(color=color.blue,graph=g3,label="P2 ")  #定义ball2动量曲线
Pcurve=gcurve(color=color.black,graph=g3,label="P ")  #定义总动量曲线

#参数设置
m1=1 
m2=1 

v1=2e8 
v2=1e8
c=3e8  

t=0  
dt=1e-11

beta1=v1/c
beta2=v2/c

Beta1=np.sqrt((1+beta1)/(1-beta1))
Beta2=np.sqrt((1+beta2)/(1-beta2))
Beta3=np.sqrt((1-beta1)/(1+beta2))
Beta4=np.sqrt((1-beta2)/(1+beta2))
M=m1*np.sqrt((Beta1+Beta2)*(Beta3+Beta4))

ratio1d=1/np.sqrt(1-(v1/c)**2)
ratio2d=1/np.sqrt(1-(v2/c)**2)

v1xd=c*((v1/c)*ratio1d+(v2/c)*ratio2d)/(ratio1d+ratio2d)

while ball1.pos.x>=-2 and ball2.pos.x<=3:  
    
    rate(1000)      
    
    ball1.pos.x=ball1.pos.x+v1*dt  
    ball2.pos.x=ball2.pos.x+v2*dt  

    #计算碰撞后的速度、动能、动量

    if (ball2.pos.x-ball1.pos.x)<=0.1 and v2==1e8:   
       
       ratio1=1/np.sqrt(1-(v1/c)**2)
       ratio2=1/np.sqrt(1-(v2/c)**2)
       v1x=c*((v1/c)*ratio1+(v2/c)*ratio2)/(ratio1+ratio2)
       v1=v1x
       v2=v1x
       
    #动能
    EK1=(m1/np.sqrt(1-(v1/c)**2)-m1)*c**2
    EK2=(m2/np.sqrt(1-(v2/c)**2)-m2)*c**2
    EK_tot=EK1+EK2
    EK=EK_tot
    
    #动量
    P1=np.sqrt((m1**2/(1-(v1/c)**2)-m1**2)*c**2)
    P2=np.sqrt((m2**2/(1-(v2/c)**2)-m2**2)*c**2)
    P=np.sqrt((M**2/(1-(v1xd/c)**2)-M**2)*c**2)
    
    if (ball2.pos.x-ball1.pos.x)<=0.1:   
       
       EK=(M/np.sqrt(1-(v1x/c)**2)-M)*c**2
      
    
    #速度绘制
    v1curve.plot(t,v1)  
    v2curve.plot(t,v2)  
    
    #动能绘制 
    EK1curve.plot(t,EK1)  
    EK2curve.plot(t,EK2)  
    EKcurve.plot(t,EK) 
    
    #动量绘制
    P1curve.plot(t,P1)  
    P2curve.plot(t,P2)  
    Pcurve.plot(t,P) 

    t=t+dt 


print("v1=%.2f"%v1,"v2=%.2f"%v2)


#非相对论条件两球的完全非弹性碰撞，两球均有初速度

from vpython import *  

s1=canvas(width=1200,height=400,background=color.white,center=vector(1,0,0) ,align="left")  #定义画布
s1.camera.pos=vector(0,1,1) #设置摄像机位置
s1.camera.axis=vector(0,-1,-1)  #设置摄像机方位

ball1=sphere(pos=vector(0,0,0),radius=0.05,color=color.red)  #定义小球ball1
ball2=sphere(pos=vector(1,0,0),radius=0.05,color=color.blue)  #定义小球ball2

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

v1=2 
v2=1  

t=0 
dt=0.001  

while ball1.pos.x>=-2 and ball2.pos.x<=3:  
    
    rate(1000)   
    
    ball1.pos.x=ball1.pos.x+v1*dt
    ball2.pos.x=ball2.pos.x+v2*dt  
    #计算碰撞后的速度

    if (ball2.pos.x-ball1.pos.x)<=0.1:
       v1x=(m1*v1+m2*v2)/(m1+m2)
       v1=v1x
       v2=v1x
    
    #动能计算    
    EK1=0.5*m1*v1**2  
    EK2=0.5*m2*v2**2  
    EK=EK1+EK2  
    
    #动量计算
    P1=m1*v1  
    P2=m2*v2  
    P=P1+P2  
    
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


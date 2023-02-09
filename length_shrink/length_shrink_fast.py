
from vpython import *

scene.background=color.white  #设置画布背景为白色
scene.center=vector(0,1,0)  #设置画布中心

base = box(pos =vector(0,-1.5,0),size=vector(10,0.1,0.1),color = color.black) # 创建底座
car = box(size=vector(1,1,1), color = color.blue,make_trail=True) # 创建小车模型
scene.autoscale=0

c = 3e8 
car.pos = vector(0,0,0) 
car.v = vector(2.8e8, 0, 0) 

#计算长度收缩系数
length_shorten_Factors = (1 / (sqrt(1 - (car.v.x**2 / c**2))), 
      1 / (sqrt(1 - (car.v.y**2 / c**2))),
      1 / (sqrt(1 - (car.v.z**2 / c**2))))

#计算小车收缩后尺寸
car.size = vector(car.size.x / length_shorten_Factors[0], 
      car.size.y / length_shorten_Factors[1], 
      car.size.z / length_shorten_Factors[2]) 

t=0 # 设定开始时间
dt= 1e-11  # 设定时间步长

while  car.pos.x <=4.5 :  #用物体x方向最大坐标极限设定分析时间
 
    rate(1000)
    car.pos = car.pos + car.v*dt  #计算小车位置更新
    t = t + dt   #时间迭代
    
print(t)
print(car.size) 


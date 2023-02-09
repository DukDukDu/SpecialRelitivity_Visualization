# SpecialRelitivity_Visualization
#1. 项目概述

***
本项目以狭义相对论为主题开展了可视化的研究，主要研究方面有：

1.相对论基本原理
2.洛伦兹坐标速度变换
3.相对性（时间间隔相对性、空间间隔相对性）
4.光速极值原理与贝托齐实验
5.狭义相对论下具体物理问题的研究（相对论完全非弹性碰撞、静止粒子衰变）

本项目应用**Python3、VPython**进行可视化处理；

#2. 文件功能介绍
***
本项目共有Lorentz_change、length_shrink、light_vlocity、collision、particle_decay、else六个文件夹，其中collision中还有picture文件夹；

##2.1 Lorentz_change含有洛伦兹变换相关文件
***
***
**Lorentz_axis_time_change.py** 该文件绘制了洛伦兹时间坐标变换相关图像，具体图像请看论文及代码注释；
**Lorentz_velocity_change.py** 该文件绘制了速度变换相关图像，具体图像请看论文及代码注释；
**sum_angle.py** 该文件绘制了速度在不同坐标系下变换后三角形内角和的分布区面；
***

##2.2 length_shrink中含有长度收缩的相关文件
***
***
**length_no_shrink.py** 该文件使用VPython模拟出低速下小车运动情况，旨在说明低速下并无长度收缩效应
**length_shrink_fast.py** 该文件使用VPython模拟出高速运动下小车运动情况，表现出明显的长度收缩
**length_shrink_low.py** 该文件使用VPython模拟出不明显的长度收缩，用以和前两个文件作出对比
**relativistic_length_shrink.py** 该文件描绘出长度收缩曲线
***

##2.3 light_velocity中含有贝托齐实验的内容
***
***
**Bertozzi_v_limit.py** 该文件绘制出经典速度曲线与相对论速度曲线以及贝托齐实验数据点
***

##2.4 collision中包含碰撞速度、静止质量相关物理量的曲线以及曲面
***
***
**collision_line1.py** 该文件描绘出一球有初速度一球静止碰撞后的相关物理量
**collision_line2.py** 该文件描绘出两球均有初速度碰撞后的相关物理量
picture文件中包含动画模拟
**nonrelativistic_collision1.py nonrelativistic_collision2.py** 两文件均描绘出非相对论情况下碰撞的动画
**relativistic_collision1.py relativistic_collision2.py** 两文件均描绘出相对论情况下碰撞的动画
***

##2.5 particle_decay中含有衰变相关文件
***
***
**particle_decay.py** 该文件描绘出静止粒子衰变后相关物理量的曲线
***

##2.6 else中含有一些其他关系的相关曲线
***
***
**relativistic_energy_momentum.py** 该文件描绘出能量动量关系
**relativistic_mass.py** 该文件描绘出质量相关曲线
**relativistic_time_expand.py** 该文件描绘出时间膨胀曲线
***

#3.鸣谢
感谢论文中提及的所有参考书及各位老师们！

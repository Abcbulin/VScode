#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# 单电机
# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

# Motor(Port.A,positive_direction = Direction,gears)
# 1.点击所连端口
# 2.转动方向，顺逆时针，默认顺时针
# 3.与电机所连齿轮列表


# 定义一个电机对象
# 逆时针旋转，默认顺时针
# gears形参承接列表元素，表示连接的齿轮列表，齿轮比
# 假设现在是12尺寸下，角速度为w，这里转化为相同角速度下的36尺寸齿轮
motor1 = Motor(Port.A, positive_direction=Direction.COUNTERLOCKWISE, gears=[12,36])
# 重置初始角度，单位度
motor1.reset_angle(0)
# 输出当前角度
print(moter.angle())
# 每秒一圈，360°，电机开始旋转
motor1.run(360)
# 持续时间，单位毫秒
wait(1000)


# 电机运行时长
# 表示在给定的时间内，以恒定的速度（角速度）电机
run_time(speed, time, then=Stop, wati=Ture)
# 1.电机转速（角速度）
# 2.运行时长（毫秒）
# 3.停止后是否惯性滑行，制动或者保持速度（默认制动）
# 4.等待电机运行完成后再继续其他的程序，还是在运行途中继续其他程序，串行改并行，如果False，则电机可能不转

# 电机旋转角度（精准）
# 给定路程，以设定速度运动
run_angle(speed, rotation_angle, then=Stop, wati=Ture)
# rotation_angle 电机以多少速度（speed）转多少度

# then的参数
# Stop.COAST 阻力：低    保持惯性
# Stop.BRAKE 阻力：适中  主动制动（有误差）
# Stop.HOLD  阻力：高    保持在指定的角度

# 电机旋转到指定角度
# 给定目标值旋转到对应的角度，可通过设定参数（初始角度，目标角度）控制顺逆时针
run_target(speed, target_angle, then=Stop, wati=Ture)
# target_angle 旋转到的目标角度


# 电机停止
# 有惯性的停止
motor1.stop()
# 直接制动
motor1.break()
# 保持在指定的角度，会自控
motor1.hold()


# 案例
# 起始两个将两个电机初始角度设置为0，先手动调整电机A到一定角度，然后让B电机运行到相同角度
# 连接两个端口
motor1= Motor(Port.A)
motor2= Motor(Port.B)
# 设置初始值
motor1.reset_angle(0)
motor1.reset_angle(0)
# 手动调整度数
wait(5000)
tagAngle = motor2.angle()
# 
motor1.run_target(120,tagAngle)


# Write your program here.
ev3.speaker.beep()

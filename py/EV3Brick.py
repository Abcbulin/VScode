#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# 程序块

# 对象生成
ev3 = EV3Brick()

# 检查当前机器电量，单位mV
ev3.battery.voltage()
# 电流
battery.current()
# 返回屏幕尺寸,单位px
screen.width
screen.height
# 保存ec3屏幕截图到ev3主机里
screen.save('filename')
# 按键是否被按压,记录被按压的按键,Button.UP此类
button.pressed()
# 案例
a = 0
ls1 = []
while a<10:
    ls1.append(ev3.button.pressed())
# 状态灯,使用wait关闭
# 关灯
light.off()
# 开灯,参数为对应灯亮颜色
light.on(Color.RED)
# 屏幕
# 清空屏幕
screen.clear()
# 屏幕写字
screen.draw_text(xAxis,yAxis,text(Str),textColor(black),backgroundColor)
# 屏幕上显示设置的内容,end设置结束符号?
screen.print(context,end='')
# 设置字体
screen.set_font()
# 显示图片
screen.load_image(source)
# 绘图
screen.draw_image(xAxis,yAxis,source,transparent=None)
# 绘点 
screen.draw_pixel(xAxis,yAxis,color=Color(0,0,0,'BLACK'))
x=random.randdint(0,10)
y=random.randdint(0,10)
while x+y<5:
    ev3.screen.draw_pixel(x,y)
# 绘线
screen.draw_line(x1,y1,x2,y2,width=1,color=Color(0,0,0,'BLACK'))
# 绘制方块,顶点,r是直径,是否实心
screen.draw_box(x1,y1,x2,y2,,r=0,fill=False,color=Color(0,0,0,'BLACK'))
# 绘制圆,圆心,直径,是否填充
screen.draw_circle(x1,y1,r,fill=False,color=Color(0,0,0,'BLACK'))
# 鸣笛声,赫兹,时间
speaker.beep(frequency=500,duration=100)
# 音量调节(百分比),(提示音,音符,语音文件,语音合成)
speaker.set_volume(volume,which='_all')
# 播放音符,音符,节拍
speaker.play_notes(notes,tempo=(int))
# 播放音乐文件
speaker.play_file(file)
# 语音合成
speaker.say()
# 语言,男女声,语速,高低音
speaker.set_speech_option(language=None,voice=None,speed=None,pitch=None)
speaker.set_speech_option(language='de',voice='f1',speed=None,pitch=None)
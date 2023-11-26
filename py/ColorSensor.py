# 颜色传感器
# 掌握ColorSensor类和相关方法
# 侦测颜色
# 侦测环境光(亮度)
# 侦测反射光(强度)
# 侦测三原色(红绿蓝)


class ColorSensor(Port):
    # 端口数

color.ColorSensor(Port.A)

while True:
    # 返回侦测到的颜色,识别颜色
    print(color.color())
    # 返回环境光的强度,数值越大越亮
    ambient()
    # 侦测反射光强度，光打到机器上的亮度，白色数值越大，反之亦然
    reflection()
    # 返回侦测到的颜色rgb数值，单个数值范围0-100
    rgb()


# 案例
# 读色卡
ev3=Ev3Brick()
while True:
    if color.color() == Color.RED:
        ec3.speaker.say('red')
    elif color.color() == Color.BLUE:
        ec3.speaker.say('blue')
    else:
        ec3.speaker.say('none')
    wait(2000)
# 触碰传感器

class TouchSensor(Port):
    # 端口

touch TouchSensor(Port.A)

while True:
    # 检测是否发生碰撞，返回值为布尔类型
    print(touch.pressed())

ev3Db = DriveBase(motor1, motor2, 50, 100)
while not touch.pressed():
    go.drive(100,0)

go.straight(-200)
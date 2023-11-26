# 搭建超声波传感器
# 掌握UltraSonicSensor类和相关用法
# 侦测前方障碍物距离
# 侦察附近有没有正在工作的超声波传感器

# 端口
sonic=UltraSonicSensor(Port.A)

while True:
    # 距离障碍物的距离
    sonic.distance()
    # 静默模式
    sonic.distance(salient=False)
    # 侦测附近有无其他超声波传感器，返回值为布尔
    sonic.presence()

# 自动避障
# 小车运动过程中，遇到障碍回避
sonic=UltraSonicSensor(Port.S1)
motor1=Motor(Port.A)
motor2=Motor(Port.B)
go = DriveBase(motor1,motor2,50,100)
while sonic.distance>100:
    go.drive(50,0)
    
go.straight(-100)
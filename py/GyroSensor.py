# 陀螺仪传感器
# 搭建陀螺仪传感器
# 掌握GyroSensor类和相关方法  

class GyroSensor(port, positive_Direction.CLOCKWISE):
    # 1.陀螺仪连接的端口
    # 2.旋转方向

# 对应端口
gyro.GyroSensor(Port.S1)
# 查看角速度
speed()
# 查看偏移角度，以接线处为原点（和speed不能共用）
angle()
# 设置初始角度
reset_angle()


# 案例：使小车移动，在遇到障碍后能自我调整保持原来的状态运动
# 准备：双电机，组装
gyro.GyroSensor(Port.S1)
motor1=Motor(Port.A)
motor2=Motor(Port.B)
go = DriveBase(motor1,motor2,50,100)
star=gyro.angel()
while True:
    go.drive(100,star-gyro.angle())


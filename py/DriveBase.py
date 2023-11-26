# 掌握DriveBase类和相关方法（控制电机模块走直线或转弯）
# 测量电机旋转相关参数
# 实验及数值调整的方法


# 代表了一个机器人车辆,配有两个动力车轮和可选的车轮脚轮,在stop()之前,无法使用单电机
class DriveBase(left_motor, right_motor, wheel_diameter, axle_track):
    # 1.驱动左侧车轮马达
    # 2.驱动右侧车轮马达
    # 3.车轮最大直径
    # 4.两车轮中心点的间距,单位毫米
    # ......

motor1 = Motor(Port.A)
motor2 = Motor(Port.B)
ev3Db = DriveBase(motor1, motor2, 50, 100)
# 直线行驶一定的距离,单位毫米
ev3Db.straight(100)
# 得到行驶的距离
ev3Db.distance()
# 转弯, 转多少度
ev3Db.turn(angle)
# 速度配置
settings(straight_speed, straight_acceleration, turn_rate, turn_acceleration)
# 1.直线速度（上限）
# 2.直行加速度
# 3.转向速度（上限）
# 4.转向加速度 


# 保持开启，让机器人按照指定的移动速度和转向值前进，知道遇到stop()，或者被另一个drive()更新状态
drive(speed, turn_rate)
# 1.速度
# 2.转向值
# 举例
while motor1.angle()<300:
    ev3Db.drive(20, 0)
ev3Db.stop()


# 测量距离
# 记录移动多少距离
distance()
# 记录移动角度
angle()
# 返回机器人自身状态，包括距离，速度，角度，角速度
state()

# 将距离和角度数据归零
reset()

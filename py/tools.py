# 计数器和实验日志
# 计时
watch = StopWatch()
# 重置时间,重新开始
watch = resume()
# 返回目标时间
time()
# 暂停
pause()
# 归零,归零后要重新开启resume
reset()
# 等待
wait(1000)

# 日志
class DataLog(*headers,name='log',timestamp=Ture,extension='csv',append=False):
# 例子
data = DataLog('time','distance')
sonic = UltraSonicSensor(Post.S1)
watch.resume()
for i in range(10):
    a = sonic.distance()
    b = watch.time()
    # 写入日志
    data.log(b,a)
    wait(1000)

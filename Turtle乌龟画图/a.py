import turtle as t
import random
# 这个文件是用来画坐标的（辅助使用）
# 坐标
def zb(stop,step,r):
    """ stop结束位置
        step间隔
        r方向
    """
    t.speed(100)
    for i in range(0,stop,step):
        t.setheading(r)
        if r==180 or r==-90:    # 如果方向是180或者-90说明是负数坐标
            t.write(-i)
        else:
            t.write(i)
        t.fd(step)
    t.home()
def run():
    zb(301,50,0)
    zb(301,50,90)
    zb(301,50,180)
    zb(301,50,-90)
    

run()
# t.done()
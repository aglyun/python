# 格式化字符串
# 1、用%来代替，但是很麻烦
# 2、用{}来代替，字符串调用.format()方法即可
print("英雄名字:{} 血量:{} 蓝条:{}".format("青龙凯",4000,200))
import turtle as t
t.speed(10)
t.bgcolor("black")  # 背景黑色
t.color("yellow","yellow")
t.up()
t.goto(50, 70)
t.down()
# t.circle(50,720,5)  # 用circle画五角星
for i in range(5):
    t.left(720/5)
    t.forward(-100)

# 月亮
t.up()
t.goto(-150, 150)
t.down()
t.left(15)
t.circle(-100, 180)

t.up()
t.goto(-150, 150)
t.down()
t.left(15)

t.done()

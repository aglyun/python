# 时间相关

---

> 其实动画的效果都是屏幕在高速刷新然后呈现出来的画面。正常的频率是一秒钟24帧。帧数越大，画面就越流畅。

#### 帧率 \(fps\)

* pygame库中的 time 模块调用 Clock\(\) 类
* 使用 Clock对象 调用 tick\(\) 方法进行设置帧率
* 帧率放在循环体内

```python
clock = pygame.time.Clock()    # 创建了一个时钟
....

while True:
    clock.tick(60)    # 60帧，当然也可以更大，按实际情况写即可
```

* 使用get\_ticks\(\) 可以获取当前运行时间
* pygame.time.get\_ticks\(\)   &gt;&gt;&gt; 1000, 2343, 3232, 4241,5521.....可以说是秒数
* 可以使用它做一些其他事情，比如每隔一秒就绘制一张图片，实现动态图

```python
ticks = pygame.time.get_ticks() # 获取时间
```

#### 

#### 定时器

> 定时器可以说是每隔多长时间执行某些事情，配合用户事件使用

* pygame库的 time模块调用 set\_time\(\) 方法
* set\_time\(用户事件对象, 毫秒\)     1秒=1000毫秒

```python
# 假设有一个 boss的用户事件， 名称是 BOSS_EVENT
BOSS_EVENT = pygame.USEREVENT
# 创建一个定时器, 30秒后触发
pygame.time.set_time(BOSS_EVENT, 30000)

...
while True:
   e = pygame.event.get()    # 获取事件
   # 遍历事件
   for i in e:
      # 如果事件的类型等于这个boss的事件
      if i.type == BOSS_EVENT:
         # 这里写敌人出现的逻辑代码
         print("Boss出来咯！")
```




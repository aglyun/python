# 控制飞机移动

---

> 飞机已经成功的绘制出来了，那接下来获取飞机的控制权吧。

#### 键盘事件

* 要控制飞机，需要获取一个键盘的事件，当按下某个按键的时候，就让飞机向某个方向移动。

* 在英雄模型类中的 update\(\) 方法中写，然后在循环体中调用即可

**jingling.py **

```python
class Hero(Game):
    def __init__(self):
        ...

    def update(self):
        # 获取事件
        k = pygame.key.get_pressed()
        # 如果按下了a按键，就让它的x轴减去速度
        if k[pygame.K_a]:
            self.rect.x -= self.speed
        if k[pygame.K_d]:
            self.rect.x += self.speed    # 按下d键矩形的x轴就增大
        if k[pygame.K_w]:
            self.rect.y -= self.speed    # 按下w键矩形的y轴就减少
        if k[pygame.K_s]:
            self.rect.y += self.speed    # 按下s键矩形的y轴就增大
```

* 在主文件中使用 英雄对象调用 update\(\) 方法。

```python
while True:
    ... 
    hero.update()    # hero调用update()方法
```

![](/assets/imposdasrt.png)

》这样就可以通过w s a d 按键控制飞机的上下左右方向了。

但是有个问题就是它会超出屏幕，我们也可以控制它活动的范围。当然了，这个看自己的爱好，限制它超不超出屏幕全凭自己决心.

![](https://s3.bmp.ovh/imgs/2021/12/0640f013923ffaa2.gif)

#### 限制飞机的活动范围

**jingling.py**

* 定义一个屏幕的常量 SCREEN 作为全局使用

```python
SCREEN = pygame.Rect(0, 0, 512, 768)   # 屏幕常量，和你创建的屏幕大小一致即可
```

```python
class Hero(Game):
    def __init__(self):
        ...

    def update(self):
        # 获取事件
       ...
        # 控制范围
        if self.rect.y < 0:   # 如果飞机矩形的y轴小于0
            self.rect.y = 0   # 让它停留在y0的位置
        if self.rect.x < 0:   # x轴也一样
            self.rect.x = 0
        # 如果矩形的右边大于屏幕的宽度
        if self.rect.right > SCREEN.width:
            # 让矩形的右边位置等于屏幕的宽度
            # 类似于x = 512
            self.rect.right = SCREEN.width
        if self.rect.bottom > SCREEN.height:
            self.rect.bottom = SCREEN.height
```

》 这样飞机就不能超出屏幕了


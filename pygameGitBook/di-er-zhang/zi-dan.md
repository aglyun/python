# 子弹

> 飞机需要发射子弹击毁敌人，子弹和敌人一样，反复创建使用然后销毁。

#### 

#### 子弹模型类：

**jingling.py**

```python
class Bullet(Game):    # 继承Game类
    """ 子弹类 """
    def __init__(self, img, speed=30):
        super().__init__(img)
        self.speed = speed    # 速度，默认是30

    def update(self):
        # 子弹由于从下往上飞，所以它的y轴需要逐减
        self.rect.y -= self.speed
```

#### 

#### 当按下某个按键的时候，创建子弹，然后跟随飞机的移动

* 在飞机模型类中创建子弹组，用于存储子弹
* 在飞机模型类的 update\(\) 方法中写键盘事件，这里 当按下空格键就开始创建子弹

```python
class Hero(Game):
    """ 英雄类 """
    def __init__(self, img):
        ...
        # 创建子弹的组，用于存储子弹
        self.bullet_group = pygame.sprite.Group()

    def update(self):
        ...
        ...
        # 如果按下了空格键
        if k[pygame.K_SPACE]:
            # 移动子弹
            b = Bullet('images/bullet1.png', 30)    # 创建子弹对象
            self.bullet_group.add(b)    # 把子弹添加到子弹组中
            # 让子弹跟随飞机,也就是子弹矩形的中心点等于飞机的矩形中心点
            b.rect.center = self.rect.center
```

#### 

#### 绘制子弹

* 由于子弹组写在了 Hero 模型类中，所以需要 Hero 的对象进行调用

**main.py**

```python
...
...
while True:
    ...
    # 绘制子弹, hero 是飞机的对象，调用了 bullet_group 子弹组
    hero.bullet_group.draw(screen)
    hero.bullet_group.update()    # 调用子弹组的 update() 方法
```

#### 

#### 自动销毁

* 由于子弹和敌人一样，会重复生成，累计多了就会占用很大的内存，这时候我们需要对飞出屏幕外的子弹将它销毁。
* 给子弹模型类中的 update\(\) 方法添加 kill\(\) 方法

**jingling.py**

```python
...
def update(self):
    ...
    if self.rect.y < 0:
        # 子弹由于从下往上飞，所以它的y轴需要逐减
        self.kill()    # 子弹超出屏幕后自动销毁
```

![](https://ftp.bmp.ovh/imgs/2021/12/da54d4570c8fa020.gif)


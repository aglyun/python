# 英雄模型类

---

> 英雄模型类也是一个普通的类，前提是需要继承精灵类\(Game\)

**jingling.py**

```python
class Hero(Game):
    """ 英雄类 """
    def __init__(self, img):
        # 创建英雄前需要传入一张图片
        super().__init__(img)

    def update(self):
        pass
```

* 大致的模型已经写好了，接下来将它在主文件中绘制即可

#### 创建飞机，绘制到屏幕：

* 创建飞机

**main.py**

```python
# 导入jingling.py文件中的英雄模型类
from jingling import Hero

....
# 创建英雄对象
hero = Hero("images/me1.png")   # me1.png是飞机的素材，hero便是英雄模型类创建出来的对象

while True:
    ...
```

![](/assets/idsadmport.png)

》》 通过面向对象的方式创建了一个飞机，也可以说是一个“模子里刻出来的”。

#### 

#### 绘制飞机

* 绘制飞机之前，需要创建一个飞机组，方便后续进行碰撞事件的检测
* 创建飞机组

**main.py**

```python
# 创建飞机组
hero_group = pygame.sprite.Group()
# 添加飞机到组中
hero_group.add(hero)
```

* 绘制：在循环体内

```python
while True:
    ...
    hero_group.draw(screen)    # screen是你的屏幕对象
```

* 飞机出现在 y0x0坐标的位置上

![](/assets/imfdsport.png)


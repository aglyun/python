# sprite精灵模块

---

> 精灵其实说的是可以快速创建一些模型，更好的对它进行操作，减少代码量
>
> 创建精灵类的时候一般是写在一个新文件中，方便管理

* pygame库中的 sprite 模块

* 自定义一个类继承sprite模块中的 Sprite 的类

```python
class Game(pygame.sprite.Sprite):
   ...
```

* 例子

```python
class Game(pygame.sprite.Sprite):
    """ 这是一个精灵类 """
    def __init__(self,image,speed=2):    # 定义了两个形参，image和speed，说明实例化的时候需要传入这两个参数
        self.image = pygame.image.load(image)  # 加载图片
        self.rect =  self.image.get_rect()     # 获取矩形
        self.speed = speed    # 速度
        # 进行上级初始化
        super().__init__()
```

* 如果要对这个Game类进行操作，比如一些移动等可以把要实现的功能写在update\(\)方法中。

```python
def update(self):
    # 让图片矩形移动
    self.rect.y += 1
```

* 或者写一个控制前后左右的

```python
 def update(self):
    # 检查事件就可以使用了
    keys = pygame.key.get_pressed()   # 获取键盘事件
    pygame.event.pump()               # 自动执行事件
    if keys[pygame.K_a]:  # 判断是否按下a按键
        # 让矩形的x轴增加-5(向左边移动)   
        self.rect.x -= 5
    if keys[pygame.K_d]:
        # 让矩形的x轴增加5(向右边移动)
        self.rect.x += 5
    if keys[pygame.K_w]:
        # 让矩形的y轴增加-5(向上边移动)
        self.rect.top -= 5
    if keys[pygame.K_s]:    
        # 让矩形的y轴增加5(向下边移动)      
        self.rect.bottom += 5
```

* 写一个超出屏幕就删除的功能
* kill\(\)  方法，杀死矩形\(可以说是删除矩形\) 

```python
def update(self):
    # 如果矩形的y轴小于0的时候
    if self.rect.y < 0:
        self.kill()    # 删除矩形
```

#### 

#### 精灵模型类的使用

* 普通的类继承了Sprite可以说这个类是一个某某的模型类，比如

```python
class Hero(pygame.sprite.Sprite):  # 这是一个英雄模型类
class Boss(pygame.sprite.Sprite):  # 这是一个boss模型类
```

* 模型类就像是一个饺子模型，把面团放到这个模型里，合上一夹就能做出一个饺子。
* 我们的模型类也是一样，直接用面向对象的方法便可制造出一个“人物”

> 使用Boss模型类制造一个boss

```python
class Boss(pygame.sprite.Sprite):
    ...

# 创建boss
boss1 = Boss()
boss2 = Boss()
boss3 = Boss()   # 一共创建了三个boss
```

* 由于我们的模型类可以创建无数个实例，也就是说我们需要给它们一个组，把它们装起来。
* pygame库中的 sprite 模块，调用 Group\(\) 类即可创建一个组

```python
boss_group = pygame.sprite.Group()    # 创建了一个boss组，用于存储boss
```

* 把三个boss添加到组里面去\(使用 add\(\) 方法\)，然后再绘制到屏幕上

```python
boss_group.add(boss1, boss2, boss3)
```

* 使用 draw\(\) 绘制，需要传入一个屏幕的对象给它。屏幕对象是你自己创建的屏幕如，screen = pygame.display.set\__mode\(\(1400,600\)_\)

```python
boss_grouo.draw(screen)
```

> 绘制的时候放在循环体内，这样可以保证不间断

![](/assets/mxl.png)


# 敌人移动

> 敌人向下移动

**jingling.py**

```python
class Enemy(Game):
    ...
    def __init__(self, img):
        ...

    def update(self):
        # 敌人移动
        self.rect.y += self.speed
```

* 在main.py中调用 update\(\) 方法

```python
while True:
    ...
    # 敌人调用update() 方法
    enemy_group.update()    # 这里使用了敌人组来进行调用update()方法，和使用实例对象调用也是一样的
```

![](/assets/dsa.png)

#### 

#### 超出屏幕后删除敌人

> 敌人是每秒创建一个，随着时间的推移，生成的越来越多，这时候内存会占越来越多，直至电脑跑不动了。这时候需要一个销毁的事件。

* 还是在 敌人模型类的 update\(\) 方法中写
* kill\(\) 方法会删除当前的实例对象

```python
def update(self):
    ...
    # 如果敌人矩形的y轴大于屏幕的高度的时候
    if self.rect.y > SCREEN.height:
        self.kill()    # 调用销毁方法
```

> 在面向对象中，可以添加 \_\__del\_\_\(\) 方法检查是否已经成删除销毁_
>
> 这个写不写无所谓，主要是用来检查自己是否已经成功销毁创建的敌人，测试没问题就可以删除代码了。

```python
class Enmey(Game):
    """ 敌人模型类 """
    ...
    ...
    def __del__(self):
        print("敌人被删除了")
```



#### ![](/assets/isdfmport.png)




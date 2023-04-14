# 敌人出现

---

> 敌人出现可以使用到用户事件，每隔一段时间便创建一个敌人，基于敌人模型类，模型类可以反复使用，这就是为什么使用它的好处之处。

# 敌人用户事件

* 导入敌人模型类

**main.py**

```python
# 导入jingling.py文件中的英雄模型类,敌人模型类
from jingling import Hero, Enemy
```

* 创建必要的条件：敌人用户事件和敌人组

```python
...

# 创建敌人用户事件
Enemy_EVENT = pygame.USEREVENT
# 把敌人事件设置一个出现事件，1000毫秒代表1秒触发一次
pygame.time.set_timer(Enemy_EVENT, 1000)
# 创建敌人组
enemy_group = pygame.sprite.Group()

# 循环主体
While True:
    ....
```

![](/assets/impdsadort.png)

* 在循环的事件中，判断事件的类似是否等于敌人的用户事件即可

```python
while True:
    ...
    for i in e:
        ...
        # 如果事件的类型等于敌人用户事件，我们就创建敌人
        if i.type == Enemy_EVENT:
            e1 = Enemy('images/enemy1.png')    # 创建敌人实例
            enemy_group.add(e1)    # 把实例添加到组中

    # 在循环事件外绘制敌人组
    enemy_group.draw(screen)
```

![](/assets/dsadimport.png)

* 这样敌人每秒就出现在 y0x0 的位置上了，下节讲解敌人随机出现位置和飞机的初始位置。

![](/assets/impordet.png)




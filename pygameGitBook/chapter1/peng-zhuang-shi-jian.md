# 碰撞事件

---

> 碰撞事件依托于精灵组，这就是为什么先讲精灵组的原因。

#### 

#### groupcollide\(\) 方法

* pygame库中的 sprite 模块调用 groupcollide\(\) 方法，该方法接收四个参数
* groupcollide\(精灵组1, 精灵组2， 是否摧毁精灵组1，是否摧毁精灵组2\)

```python
# 假设我有两个精灵组，一个是子弹组，一个是boss组
bullet_g = pygame.sprite.Group()   # 子弹组
boss_g =pygame.sprite.Group()      # boss组

# 开始碰撞检测
#                          子弹组，boss组，是否摧毁子弹，是否摧毁boss
pygame.sprite.groupcollide(bullet_g, boss_g, True, True)  # 当子弹碰到boss，两个都会被摧毁(删除)

# 还可以这样
pygame.sprite.groupcollide(bullet_g, boss_g, False, True)   # 子弹碰到boss，boos会摧毁，子弹不会
```




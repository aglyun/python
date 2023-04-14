# 碰撞事件

---

> 游戏一切就绪，最后两个内容，碰撞事件以及积分系统。

#### 子弹销毁敌机

**main.py**

```python
while True:
`...
    # 子弹摧毁敌人
    pygame.sprite.groupcollide(hero.bullet_group, enemy_group, True, True)
    # 敌人摧毁我方飞机 
    is_end = pygame.sprite.groupcollide(hero_group, enemy_group, True, False)
    pygame.display.update()    # 刷新
```

》 这样每当子弹碰到敌人，或者敌人碰到飞机都会被摧毁。


# 控制帧率

---

> 由于没有设置帧率，它运动的速度是很快的，所以我们需要控制游戏的节奏，一般30~60帧即可。

* 创建时钟: 帧率需要放在循环体内

```python
# 创建时钟
clock = pygame.time.Clock()

while True:
    # 控制帧率
    clock.tick(60)
```

* 示图

![](/assets/impfsdfsdort.png)

》 这样一来，游戏的整体随我们控制了


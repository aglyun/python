# 游戏循环

---

#### \# 循环体

> **游戏开始是无限循环的执行，把主要的事件，绘制，都放在循环体里面，当跳出循环体的时候就意味着游戏结束**

* while True:     无限循环

```python
while True:
    代码块...
    代码块...
```

* 当初始化完成之后，便是游戏的循环部分

```python
import pygame
...
...
while True:
    screen.blit(bg, bg_rect)    # 绘制背景图
    pygame.display.update()     # 刷新屏幕
```

![](/assets/bg_test.png)

## 以上的代码便能让图像一直显示在屏幕上，但是无法关闭窗口怎么办？

## 下节来讲事件。




# 初始化游戏

---

> 初始化游戏，主要做的工作是把大致构架写好，比如屏幕的创建、背景音乐加载、背景图等

#### 初始化

* 新建文件：main.py
* 编写代码

**main.py**

```python
import pygame

pygame.init()    # 初始化游戏

# 创建屏幕，屏幕大小根据你的背景图大小创建
screen = pygame.display.set_mode((512, 768))    
# 背景图
bg1 = pygame.image.load('images/bg.png')
bg1_rect = bg1.get_rect()    # 获取它的矩形

# 循环主体
while True:
    screen.blit(bg1, bg1_rect)    # 绘制
    pygame.display.update()    # 刷新
```

> 运行结果会很卡，原因是需要进行事件操作，所以，大致游戏框架写完后需要一些点击事件。事件需要

```python
e = pygame.event.get()
    for i in e:
        if i.type == pygame.QUIT:
            pygame.quit() # 卸下所有pygame的模块
            sys.exit()    # 关闭程序
```

##### 整体代码是：

![](/assets/ztdm.png)


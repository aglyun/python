# 创建精灵类

---

> 新建一个文件，用来写精灵类，主要是为了简单明了，当然也可以写在同一个文件中，但是不建议，因为那样容易出错，造成视觉混淆，文件体积过大、不便维护。

* 新建文件： jingling.py

* 编写代码

**jingling.py**

```python
import pygame


class Game(pygame.sprite.Sprite):
    """ 精灵类 """
    def __init__(self, img, speed=2):
        # img： 需要传入一个图片
        # 速度默认为2
        super().__init__()    # 初始化这个类
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()    #获取图像的矩形
        self.speed = speed   # 速度等于传来的速度，默认是2
```




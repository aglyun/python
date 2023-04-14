# 初始工作

---

* 导包

```python
import pygame
```

* 也可以给这个包重新命名，关键词是 as ，新名字便能代替pygame执行工作

```python
import pygame as g
```

#### 

#### 初始化游戏

* 使用pygame库里面的init\(\)方法即可，放在最前面

```python
import pygame  # 导包

pygame.init()   # 初始化
```

#### 

#### 创建屏幕

* 所有的动画都会在屏幕上展现，也就是所有的动画都会绘制到屏幕上
* 使用 pygame库里面的 display 模块
* 调用 display 模块中的 set\_mode\(\) 方法，这个方法接收一个元组作为参数

```python
screen = pygame.display.set_mode((1400, 600))    # 创建了一个宽1400、高600像素的屏幕
```

#### 

#### 创建图片\(背景图\)

* pygame库中的 image 模块
* image模块调用 load\(\) 方法
* load\("图片的路径"\)
* 不支持动态图

```python
bg = pygame.image.load("bg.png")    # 导入了一张名为 bg.png 的图片
```

* 图像是无法直接移动的，我们只能移动它的矩形
* 图像对象调用 get\_rect\(\)  方法便能获取本张图像的矩形

```python
bg_rect = bg.get_rect()    # 获取了一个背景图的矩形,然后用一个变量存储
```

![](/assets/import.png)

> 如何把加载进来的图片在屏幕上显示呢？
>
> 使用屏幕的对象进行绘制即可。

#### 

#### 绘制图片到屏幕

* 屏幕对象调用 blit\(\) 方法将图像和图像矩形进行绑定
* blit\(图像, 图像矩形\)

```python
screen.blit(bg, bg_rect)
```

* 接下来进行刷新屏幕

```python
pygame.display.update()    # 刷新是必不可少，图像都是依靠刷新才能展现在屏幕上
```

> 像背景图，背景音乐，字体这些都可以在创建游戏之前就进行初始化

display模块的一些方法![](/assets/display_test.png)


# 矩形

---

> 矩形可以理解成一个装载图片的一个方框，因为图像不能直接移动，方框才能移动，所以只能装在方框里。

#### 

#### 创建矩形

* 使用pygame的 Rect\(\) 类创建
* Rect\(\)  接收四个参数，分别是x，y，宽，高，如: Rect\(0, 0, 1400, 600\)

```python
bg_rect = pygame.Rect(0, 0, 1400, 600)    # 在y轴0、x轴0的位置创建一个宽1400，高600的矩形
```

* 矩形的操作方式

| 属性 | 功能 | 示例 |
| :--- | :--- | :--- |
| x | 矩形的x轴 | bg\_rect.x = 100 |
| y | 矩形的y轴 | bg\_rect.y = 200 |
| width | 矩形的宽度 | bg\_rect.width = 100 |
| height | 矩形的高度 | bg\_rect.height = 100 |
| size | 矩形的大小，返回一个元组 | bg\_rect.size  返回&gt;&gt;&gt;  \(1400, 600\) |
| bottom | 矩形的底部位置 | bg\_rect.bottom |
| top | 顶部的位置 | bg\_rect.top |
| left | 左边发位置 | bg\_rect.left |
| right | 右边的位置 | bg\_rect.right |
| center | 中心位置 | bg\_rect.center |

#### 

#### 其他方法：

* 可以直接使用图片的对象来调用一个方法，这个方法可以自动创建一个矩形
* 图片对象.get\_rect\(\)   

```python
img_rect = 图片对象.get_rect()    # 获得一个矩形，里面已经拥有上面的所有熟悉
img_rect.x = 100                 # 让矩形的x轴移动100的位置
img_rect.bottom = 其他矩形.bottom # 让矩形的底部位置和某个矩形的底部位置一致
```




# 字体

---

> 字体作为一些提示或者游戏积分、生命值而显示在屏幕中是必不可少的，接下来看看如何操作他们

#### 

#### font模块

* pygame库中的 font 模块 调用 Font\(\) 类进行创建
* Font\(字体路径, 字体大小\)
* 使用字体对象调用 .render\(\) 方法进行渲染
* 绘制到屏幕上显示

```python
# 创建字体, windows系统的字体路径一般是在 C:/Windows/Fonts/
text = pygame.font.Font("C:/Windows/Fonts/simhei.ttf", 60)

# 渲染字体, True代表是否平滑，False的话是比较粗糙，"red"代表红色
text_obj = text.render("你要显示的文字", True, "red")

# 绘制到屏幕, 位置是Y轴=0， X轴=0
screen.blit(text_obj, (0, 0))
```




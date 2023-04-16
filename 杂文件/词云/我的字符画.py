from PIL import Image, ImageFilter

filename = ""
# 打开文件
def openfile(file):
    global filename
    # 这个函数接受一个文件
    img = Image.open(file)
    filename = img.filename    # 图片的名称
    w, h = img.size    # 获取图片的大小
    img = img.resize((w, h)).convert("RGB")    # 设置图片的宽高，顺便设置成灰度
    # 返回一张灰度图片
    return img
def effects(img, tx):
    # 这个函数实现各种特效, 需要传入一张灰度图片,和一种特效
    # 创建一个字典，存储对于的特效
    tx_zd = {
        "字符画": "zfh", "浮雕": ImageFilter.EMBOSS, "高斯模糊": ImageFilter.GaussianBlur,"普通模糊": ImageFilter.BLUR, "边缘增强": ImageFilter.EDGE_ENHANCE,
        "轮廓": ImageFilter.CONTOUR, "锐化": ImageFilter.SHARPEN,"平滑": ImageFilter.SMOOTH, "细节": ImageFilter.DETAIL}
    a = tx_zd.get(tx)   # 获取对应的特效英文名称,传给filter()函数
    if a != 'zfh':    # 之所以判断a不等于zfh，因为ImageFilter中没有zfh
        img = img.filter(a)  # 过滤图片，需要设置过滤成什么效果
        img.save("{}.jpg".format(tx))    # 保存图片
        return "{}.jpg".format(tx)    # 返回图片名称, 目的是在图形化中显示
    else:
        return huidu(img)    # 返回字符串特效

def huidu(img):
    # 这个函数是实现字符画功能
    w, h = img.size    # 获取图片的大小
    text = ""    # 字符串，用于存储字符
    # 过滤成字符画,for循环遍历图片的宽高
    for y in range(h):
        for x in range(w):
            gray = img.getpixel((x-1, y-1))   # getpixel()传入一个xy轴，得到该坐标对应图片上的颜色值
            text += setchar(gray)    # 灰度转换后
        text += '\n'
    f = open('字符画.txt', 'w')
    f.write(text)
    f.close()
    return text

def setchar(gray):
    # gray 是一个整数值，如 255,200,100等
    # 这个函数用来判断灰度值是否小于150，如果小于150就返回0
    return "0" if gray < 150 else "1"




from wordcloud import WordCloud     # 词云库
from PIL import Image    # 打开图片专用
import matplotlib.pyplot as pyt    # 生成图片专用
import numpy as np     # 把图片转成列表(数组)专用
import jieba    # 把文字转成词语


font_path = "C:/Windows/Fonts/simfang.ttf"    # 字体路径，写成全局变量
def text(text):
    """ 这个函数实现文字分词 """
    jieba_text = " ".join(jieba.lcut(text))  # 通过结巴工具分词
    return jieba_text
def open_img(img_path):
    """ 这个函数实现把图片转成python可以编辑的对象 """
    # 打开图片,并且使用numpy库转成矩阵
    img = Image.open(img_path)    # Image打开一张图片
    img_array = np.array(img)    # 返回一个图片矩阵
    return img_array
def img_to_wcloud(bg, jieba_text, img_array=None):
    """ 这个函数能把图片转成词云, 需要传入文本，图片矩阵，不传图片矩阵就是默认为None"""
    # 异常捕捉，因为img_array为None时，mask=img_array就会出错，出错后就执行except的代码
    try:
        w = WordCloud(font_path=font_path, background_color=bg, mask=img_array, repeat=True, contour_width=1, contour_color="white")
    except Exception:
        w = WordCloud(font_path=font_path, background_color=bg, repeat=True)
    w = w.generate(jieba_text)    # 生成带有分词的图片
    # 使用pyplot生成显示图片, 设置样式为双平线
    pyt.imshow(w, interpolation="bilinear")
    pyt.axis("off")     # 关闭坐标
    pyt.show()          # 显示图片
"""
WordCloud 常用参数说明：
font_path: 字体的路径
background_color: 背景颜色
mask: 设置背景形状（传入图片矩阵,就是numpy转换后的图片数据）
repeat: 设置是否重复显示分词
contour_width: 轮廓大小
contour_color: 轮廓大小
"""
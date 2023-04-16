from wordcloud import WordCloud
import jieba
from PIL import Image
import numpy
i = Image.open('灰度图片.png').convert("L")
i.save("灰度图片.png")
i = numpy.array(i)
s = " ".join(jieba.lcut("迪迦奥特曼"))

w = WordCloud(font_path="C:/Windows/Fonts/simfang.ttf", background_color="white",
          repeat=True, mask=i).generate(s)

w.to_file("文字云.png")
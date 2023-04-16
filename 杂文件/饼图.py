 #-*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

# 数据
data = {'Windows7':60.86,
        'Windows10':18.46,
        'Windows8':3.61,
        'Windows xp':10.3,
        'mac os':6.78,
        '其他':1.12}
data = pd.Series(data=data)   # 把字典数据转成series类型
e = [0,0.05,0,0,0,0]   # 设置饼图模块分割参数
# 设置饼图标题和百分号输出,阴影，分割0.05，百分比颜色白色
d = data.plot.pie(autopct="%.2f%%",shadow=True,explode=e,
                  textprops={"color":"white"})
# 再次绘制，显示外部标签
data.plot.pie(explode=e)
d.set_ylabel('')   # 把y轴设置为空
plt.show()


import easygui
import 词云 as cy

title = "词云图形化工具(纯净无广告)V1.0"
msg = """
欢迎使用小橘词云图形转换软件(纯净无广告)

使用说明：
   1. 提供两种模式：形状模式，默认模式
   2. 形状模式：需要导入一张图片
   3. 默认模式：不需要图片，直接生成文本
   
声明：版权归小橘老师所有，仅供学习交流使用。
-----------------------------------
如有问题联系我QQ: 1234567890
"""
# msgbox()是一个消息盒子,里面有msg参数(显示的信息)，title参数(显示的标题)，和按钮
easygui.msgbox(msg=msg, title=title, ok_button="我已了解")
button_lb = ['形状模式', "默认模式", "退出"]    # 一个列表，用来做选择
# buttonbox()是一个按钮盒子，也就是有很多按钮，当点击按钮的时候，会返回点击到的是什么字符串
a = easygui.buttonbox(msg="您接下来要做啥?", title=title, choices=button_lb)

if a != "退出":
    # 编写图片参数
    lb = ["黑色", "红色", "蓝色", "绿色", "白色", "紫色", "黄色"]   # 代表可选的背景颜色
    zd = {"黑色":"black", "红色":"red", "蓝色":"blue", "绿色":"green", "白色":"white", "紫色":"purple", "黄色":"yellow"}

    if a == "形状模式":  # 需要传入图片
        # choicebox() 选择盒子，也就是有很多选择，点击选中谁就会返回谁
        color = easygui.choicebox(msg="选择你喜欢的背景颜色", title=title, choices=lb)
        # textbox() 文本盒子，可以让用户输入文本，然后返回给text变量接收
        text = easygui.textbox(msg="输入文本", title=title)
        # fileopenbox() 文件打开盒子，顾名思义，可以打开一个文件，返回的是文件的绝对路径
        img_path = easygui.fileopenbox("选择一张图片", "打开文件")  # 得到一个图片的路径
        # 下面是通过自己写的“词云”模块调用打开图片函数和文本函数
        img_array = cy.open_img(img_path)    # 得到图片矩阵
        jieba_text = cy.text(text)   # 得到文本
        bg = zd.get(color)    # 获取背景颜色，放到img_to_wcloud()函数中
        cy.img_to_wcloud(bg=bg, jieba_text=jieba_text, img_array=img_array)    # 进行转换
    else:
        # 反之就是默认模式，这个模式不需要图片，只需要输入文字即可
        color = easygui.choicebox(msg="选择你喜欢的背景颜色", title=title, choices=lb)
        # 否则上传一个文本即可
        text = easygui.textbox(msg="输入文本", title=title)
        jieba_text = cy.text(text)   # 得到结巴分词
        bg = zd.get(color)    # 背景颜色
        cy.img_to_wcloud(bg=bg, jieba_text=jieba_text)    # 转换
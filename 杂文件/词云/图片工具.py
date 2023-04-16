import easygui
import 我的字符画 as myzfh
msg = """
欢迎使用小橘图形转换软件(纯净无广告)

使用说明：
   1. 导入图片
   2. 选择样式
   3. 生成图片
   
声明：版权归小橘老师所有，仅供学习交流使用。
-----------------------------------
如有问题联系我QQ: 1234567890
"""
title = "小橘图形软件"
easygui.msgbox(msg=msg, title=title)
button_lb = ['退出', '打开文件']
a = easygui.buttonbox(msg="您接下来要做啥?", title=title, choices=button_lb)
if a == "打开文件":
    f = easygui.fileopenbox("选择一张图片", "打开文件")
    xz = ['字符画', '浮雕', '高斯模糊', '普通模糊', '边缘增强', '轮廓',
          '锐化', '平滑', '细节']
    tx = easygui.choicebox(msg="选择一种你喜欢的特效？", title=title, choices=xz)

    # 开始调用文件
    img = myzfh.openfile(f)   # 打开文件
    zf = myzfh.effects(img, tx)    # 选择特效
    if tx == "字符画":  # 判断选的是否是字符画
        easygui.msgbox(msg=zf, title=title, ok_button="确定")
    else:
        easygui.buttonbox(msg="效果如下", title=title, image=zf, choices=['保存', '退出'])



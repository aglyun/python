import mkcloud
import pyttsx3

s = input('你说：')
a = ''           # 存储机器人2说的话
flag=False   # 标记
p = pyttsx3.init()    # 初始化语音包

while True:
    if flag:
        s1 = mkcloud.robot.chat(a)  
    else:
        s1 = mkcloud.robot.chat(s)
        
    print('机器人1说：', s1)
    # 说话
    pyttsx3.speak(s1)


    s2 = mkcloud.robot.chat(s1)
    print('机器人2说：', s2)
    pyttsx3.speak(s2)
    a = s2

    num = True   
  


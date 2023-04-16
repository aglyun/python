from pydub import AudioSegment

# 需要安装 ffmpeg才能运行
mp3 = "压迫感.mp3"
song = AudioSegment.from_mp3(mp3)   # 打开mp3文件
s = song[45*1000:58*1000]-3    # 剪辑开始时间*毫秒数：结束时间*毫秒数
print(s)

s.export("压迫感高潮.mp3")    # 导出剪辑好的音频


import pygame,os



class GameImg():
    def __init__(self, img, x, y, w, h):
        self.w = w
        self.h = h
        self.image = pygame.image.load(img).convert_alpha()
        self.image = pygame.transform.scale(self.image,(self.w,self.h))
        self.rect = self.image.get_rect()   # 获取尺寸
        self.rect.x = x
        self.rect.y = y




re1_path = os.path.join(os.path.dirname('__name__'), '1.png')
re2_path = os.path.join(os.path.dirname('__name__'), '2.png')
b1 = []
b2 = []
fk_xy = [0, 200, 400]
def fk():
    for k in range(3):
        for i in range(3):
            fk1 = GameImg(re1_path, fk_xy[i], k * 200 + 20, 200, 200)
            fk2 = GameImg(re2_path, fk_xy[i], k * 200, 200, 200)
            b1.append(fk1)
            b2.append(fk2)
    return b1, b2



def check_key(key,aj, y1=20,y2=0):
    anjian = 10
    # 传入一个key，和aj按钮矩形 y1白框当前y轴位置，y2黑框y的位置
    keys = pygame.key.get_pressed()
    # 获取黑色按键的框,比如空格键
    if keys[key]:
        aj.rect.y += anjian
        if aj.rect.y > y1:  # 这个是测试按钮1
            aj.rect.y = y1
    elif not keys[key]:
        # 松开空格键
        aj.rect.y -= anjian
        if aj.rect.y < y2:
            aj.rect.y = y2

x = 10
# 放大选到的州
def select_zhou(flag, zooms, big_image, map_rect, x=10, y=10):
    """
    :param flag: 代表选中的是什么州，州1 或者州2
    :param zooms: 放大列表的第一个值，默认是600,1800,5400
    :param big_image: 加载的第一张地图
    :param map_rect: 地图的矩形
    :param x: 地图矩形向x轴移动的速度
    :param y: 地图矩形向y轴移动的速度
    :return:
    """
    if flag =='州1':
        # print('我要被执行了---开始选州共9个')
        zooms[0] += 20
        map_image = pygame.transform.scale(big_image, (zooms[0], zooms[0])).convert()
        return map_image
    elif flag == '州2':
        zooms[0] += 20   # 这个是放大地图的
        # 应该在这里面搞，让他慢慢移动 过去
        map_image = pygame.transform.scale(big_image, (zooms[0], zooms[0])).convert()
        map_rect.x -= x
        if map_rect.x < -600:
            map_rect.x = -600
        return map_image
    elif flag == '州3':
        zooms[0] += 20   # 这个是放大地图的
        map_image = pygame.transform.scale(big_image, (zooms[0], zooms[0])).convert()
        # 应该在这里面搞，让他慢慢移动 过去
        map_rect.x -= x*2
        if map_rect.x < -1200:
            map_rect.x = -1200
        return map_image
    elif flag == '州4':
        zooms[0] += 20   # 这个是放大地图的
        map_image = pygame.transform.scale(big_image, (zooms[0], zooms[0])).convert()
        # 应该在这里面搞，让他慢慢移动 过去
        map_rect.y -= y
        # 原本是写600的，但是地图的y轴有20距离的差异，所以写成-580
        if map_rect.y < -580:
            map_rect.y = -580
        return map_image
    elif flag == '州5':
        zooms[0] += 20  # 这个是放大地图的
        map_image = pygame.transform.scale(big_image, (zooms[0], zooms[0])).convert()
        # 应该在这里面搞，让他慢慢移动 过去
        map_rect.y -= y
        map_rect.x -= x  # 需要变x轴
        # y轴不变，要变x轴
        if map_rect.y < -580:
            map_rect.y = -580
        if map_rect.x < -600:
            map_rect.x = -600
        return map_image
    elif flag == '州6':
        zooms[0] += 20  # 这个是放大地图的
        map_image = pygame.transform.scale(big_image, (zooms[0], zooms[0])).convert()
        # 应该在这里面搞，让他慢慢移动 过去
        map_rect.y -= y
        map_rect.x -= x*2  # 乘上2，加快速度
        # y轴不变，要变x轴
        if map_rect.y < -580:
            map_rect.y = -580
        if map_rect.x < -1200:
            map_rect.x = -1200
        return map_image
    elif flag == '州7':
        zooms[0] += 20  # 这个是放大地图的
        map_image = pygame.transform.scale(big_image, (zooms[0], zooms[0])).convert()
        # 应该在这里面搞，让他慢慢移动 过去
        map_rect.y -= y *2 # 加快速度
        # 改变y轴，移动到最后一排  1180或者1200
        if map_rect.y < -1180:
            map_rect.y = -1180
        return map_image
    elif flag == '州8':
        zooms[0] += 20  # 这个是放大地图的
        map_image = pygame.transform.scale(big_image, (zooms[0], zooms[0])).convert()
        # 应该在这里面搞，让他慢慢移动 过去
        map_rect.y -= y * 2  # 加快速度
        map_rect.x -= x  # 加快速度
        # 到最后一排的第二个，y不变需要变换x轴
        if map_rect.y < -1200:
            map_rect.y = -1200
        if map_rect.x < -600:
            map_rect.x = -600
        return map_image
    if flag == '州9':
        zooms[0] += 20  # 这个是放大地图的
        map_image = pygame.transform.scale(big_image, (zooms[0], zooms[0])).convert()
        # 应该在这里面搞，让他慢慢移动 过去
        map_rect.y -= y * 2  # 加快速度
        map_rect.x -= x * 2  # 加快速度
        # 到最后一排的第二个，y不变需要变换x轴
        if map_rect.y < -1200:
            map_rect.y = -1200
        if map_rect.x < -1200:
            map_rect.x = -1200
        return map_image


def select_city(city_name, zooms, big_image, map_rect, x_zhou1_9, y_zhou1_9, flag=None):
    zhi = {0:22, -580:44, -600:44, -1200:66,-1800:88, -2400:111, -3000:133, -3600:155, -4200:177, -4800:200}
    if city_name == '城1':
        zooms[1] += 200
        map_image = pygame.transform.scale(big_image, (zooms[1], zooms[1])).convert()
        map_rect.x -= zhi[x_zhou1_9[0]]
        map_rect.y -= zhi[y_zhou1_9[0]] + 20
        if map_rect.x <= x_zhou1_9[0]:   # 0
            map_rect.x = x_zhou1_9[0]
        if map_rect.y <= y_zhou1_9[0] + 20:   # 0
            map_rect.y = y_zhou1_9[0] + 20
        return map_image

    if city_name == '城2':
        zooms[1] += 200
        map_image = pygame.transform.scale(big_image, (zooms[1], zooms[1])).convert()
        # 移动矩形
        map_rect.x -= zhi[x_zhou1_9[1]]   # 此时，城2是-600的位置，-600对应速度44
        map_rect.y -= zhi[y_zhou1_9[0]] + 20
        if map_rect.x <= x_zhou1_9[1]:   # -600,
            map_rect.x = x_zhou1_9[1]
        if map_rect.y <= y_zhou1_9[0] + 20:   # 0
            map_rect.y = y_zhou1_9[0] + 20
        return map_image

    if city_name == '城3':
        zooms[1] += 200
        map_image = pygame.transform.scale(big_image, (zooms[1], zooms[1])).convert()
        # 移动矩形
        map_rect.x -= zhi[x_zhou1_9[2]]  # 此时，城3是-1200的位置，--1200对应速度66
        map_rect.y -= zhi[y_zhou1_9[0]] + 20
        if map_rect.x <= x_zhou1_9[2]:  # -1200
            map_rect.x = x_zhou1_9[2]
        if map_rect.y <= y_zhou1_9[0] + 20:  # 0
            map_rect.y = y_zhou1_9[0] + 20
        return map_image

    if city_name == '城4':
        zooms[1] += 200
        map_image = pygame.transform.scale(big_image, (zooms[1], zooms[1])).convert()
        # 移动矩形
        map_rect.x -= zhi[x_zhou1_9[0]]  # 此时，城4是0的位置，0对应速度22，y位置是-600，对应速度44
        map_rect.y -= zhi[y_zhou1_9[1]]
        if map_rect.x <= x_zhou1_9[0]:
            map_rect.x = x_zhou1_9[0]
        if map_rect.y <= y_zhou1_9[1] + 20:  # -600
            map_rect.y = y_zhou1_9[1] + 20
        return map_image

    if city_name == '城5':
        zooms[1] += 200
        map_image = pygame.transform.scale(big_image, (zooms[1], zooms[1])).convert()
        # 移动矩形
        map_rect.x -= zhi[x_zhou1_9[1]]  # 此时，城5是-600的位置，-600对应速度44，y位置是-600，对应速度44
        map_rect.y -= zhi[y_zhou1_9[1]]
        if map_rect.x <= x_zhou1_9[1]:  # -600
            map_rect.x = x_zhou1_9[1]
        if map_rect.y <= y_zhou1_9[1] + 20:  # -600
            map_rect.y = y_zhou1_9[1] + 20
        return map_image
    if city_name == '城6':
        zooms[1] += 200
        map_image = pygame.transform.scale(big_image, (zooms[1], zooms[1])).convert()
        # 移动矩形
        map_rect.x -= zhi[x_zhou1_9[2]]  # 此时，城6是-1200的位置，-1200对应速度66，y位置是-600，对应速度44
        map_rect.y -= zhi[y_zhou1_9[1]]
        if map_rect.x <= x_zhou1_9[2]:  # -600
            map_rect.x = x_zhou1_9[2]
        if map_rect.y <= y_zhou1_9[1] + 20:  # -600
            map_rect.y = y_zhou1_9[1] + 20
        return map_image
    # x_zhou1_9 = [0, -600, -1200, -1800, -2400, -3000, -3600, -4200, -4800]
    # y_zhou1_9 = [0, -580, -1200, -1800, -2400, -3000, -3600, -4200, -4800]
    # 0: 22, -580: 44, -600: 44, -1200: 66,
    # -1800: 88, -2400: 111, -3000: 133,
    # -3600: 155, -4200: 177, -4800: 200
    if city_name == '城7':
        zooms[1] += 200
        map_image = pygame.transform.scale(big_image, (zooms[1], zooms[1])).convert()
        map_rect.x -= zhi[x_zhou1_9[0]]  # 此时，城7是0的位置,对应速度22，y位置是-1200，对应速度66
        map_rect.y -= zhi[y_zhou1_9[2]]
        if map_rect.x <= x_zhou1_9[0]:  # 0
            map_rect.x = x_zhou1_9[0]
        if map_rect.y <= y_zhou1_9[2] + 20:  # -600
            map_rect.y = y_zhou1_9[2] + 20
        return map_image
    if city_name == '城8':
        zooms[1] += 200
        map_image = pygame.transform.scale(big_image, (zooms[1], zooms[1])).convert()
        map_rect.x -= zhi[x_zhou1_9[1]]  # 此时，城8是-600的位置,对应速度44，y位置是-1200，对应速度66
        map_rect.y -= zhi[y_zhou1_9[2]]
        if map_rect.x <= x_zhou1_9[1]:  # 0
            map_rect.x = x_zhou1_9[1]
        if map_rect.y <= y_zhou1_9[2] + 20:  # -600
            map_rect.y = y_zhou1_9[2] + 20
        return map_image
    if city_name == '城9':
        zooms[1] += 200
        map_image = pygame.transform.scale(big_image, (zooms[1], zooms[1])).convert()
        # 移动矩形
        map_rect.x -= zhi[x_zhou1_9[2]]  # 此时，城9是-1200的位置,对应速度66，y位置是-1200，对应速度66
        map_rect.y -= zhi[y_zhou1_9[2]]
        if map_rect.x <= x_zhou1_9[2]:  # 0
            map_rect.x = x_zhou1_9[2]
        if map_rect.y <= y_zhou1_9[2] + 20:  # -600
            map_rect.y = y_zhou1_9[2] + 20
        return map_image


def return_view(city_name, zooms, big_image, map_rect, x_zhou1_9, y_zhou1_9):
    zhi = {0:22, -580:44, -600:44, -1200:66,-1800:88, -2400:111, -3000:133, -3600:155, -4200:177, -4800:200}
    if city_name == '城1':
        zooms[1] -= 200
        map_image = pygame.transform.scale(big_image, (zooms[1], zooms[1])).convert()
        map_rect.x += zhi[x_zhou1_9[0]]
        map_rect.y += zhi[y_zhou1_9[0]] + 20
        if map_rect.x >= x_zhou1_9[0]:  # 0
            map_rect.x = x_zhou1_9[0]
        if map_rect.y >= y_zhou1_9[0] + 20:  # 0
            map_rect.y = y_zhou1_9[0] + 20
        return map_image

    if city_name == '城2':
        zooms[1] -= 200
        map_image = pygame.transform.scale(big_image, (zooms[1], zooms[1])).convert()
        # 移动矩形
        map_rect.x += zhi[x_zhou1_9[1]]   # 此时，城2是-600的位置，-600对应速度44
        map_rect.y += zhi[y_zhou1_9[0]] + 20
        if map_rect.x >= x_zhou1_9[1]:   # -600,
            map_rect.x = x_zhou1_9[1]
        if map_rect.y >= y_zhou1_9[0] + 20:   # 0
            map_rect.y = y_zhou1_9[0] + 20
        return map_image

def if_button(i, glob_view=None,flag=None):
    """
    :param i: 循环事件
    :param zooms: 有参数的列表
    :param flag: 州、城市标志
    :param glob_view: 视野
    :return:
    """
    # 需要判断9*9 81次，所以不可能写81次判断，需要用for循环来操作
    # K_1是49，K_2是50...K_9是57
    zd = {1:49, 2:50, 3:51, 4:52, 5:53, 6:54, 7:55, 8:56, 9:57}
    name = ''
    for k in range(1, 10):  # 城市
        # if i.type == pygame.KEYDOWN and i.key == pygame.K_1 and zooms[0] == 1820:
        if i.type == pygame.KEYDOWN and i.key == zd[k]:
            glob_view = '战斗'
            name= '%s-城%s'%(flag, k)
    return name


class WuJiang():
    def __init__(self, font, name, tongbing, wuli, zhili, color='black'):
        self.b = tongbing
        self.w = wuli
        self.z = zhili
        self.name = font.render(name, True, (color))
        self.tongbing = font.render(tongbing, True, ('black'))
        self.wuli = font.render(wuli, True, ('black'))
        self.zhili = font.render(zhili, True, ('black'))

    def draw_text(self, screen, x, y):
        screen.blit(self.name, (x+100, y))
        screen.blit(self.tongbing, (x+100*2, y))
        screen.blit(self.wuli, (x+100*3, y))
        screen.blit(self.zhili, (x+100*4, y))

    def count_bing(self):
        # 计算兵力
        bob1 = int(self.b)
        zong = 100  # 根据兵力来来调整100,1000,10000
        color = 'red'

        if bob1 <= 2000:
            # 用红色点点
            zong = 100  # 根据兵力来来调整100,1000,10000
            color = 'red'
        elif bob1 > 2000 and bob1 <= 10000:
            # 用蓝色点点
            zong = 500  # 根据兵力来来调整100,1000,10000
            color = 'blue'
        elif bob1 > 10000 and bob1 <= 20000:
            zong = 1000
            # 白色小点点
            color = 'white'
        else:
            # 使用黑色小点点。一个黑色代表1万兵力
            zong = 10000
            # 黑色
            color = 'white'
        smy_b = bob1 // zong
        return (smy_b,color)





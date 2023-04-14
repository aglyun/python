import sys

import pygame

from static.main import *

# 初始化Pygame
pygame.init()


screen_width = 600
screen_height = 750
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('敲打三国')
# 加载地图图像
big_image = pygame.image.load('大地图.png').convert_alpha()   # 不能覆盖大地图
map_image = pygame.transform.scale(big_image, (600,600)).convert_alpha()  # 一定要设为最大，不然很模糊

# 每次放大地图，一定要从big地图开始，覆盖给map_image
map_rect = map_image.get_rect()
map_rect.y = 20
# 显示方框
b1, b2 = fk()
# 两个返回的按钮
return_b1 = GameImg('3.png',0,640, 600, 90)
return_b2 = GameImg('4.png',0,620, 600, 90)


zooms = [600, 1800]

flag = "未选择任何州"  # 代表当前操作的州几？
city_flag = 0  # 代表当时的操作是城几？

glob_view = '全国'  # 这是全国地图的标志,州，城市三个
c = pygame.time.Clock()
x = 10  # 控制1800地图的x轴速度
y = 10

# 字体对象
font = pygame.font.Font('C:\\Windows\\Fonts\\simhei.ttf', 26)
return_text = font.render('主公要去哪里？', True, (0,0,0))
b_text = font.render('并州', True, (0,0,0))
xu_text = font.render('徐州', True, (0,0,0))
j_text = font.render('交州', True, (0,0,0))
# 州1 文本
zhou1_t1 = font.render('豫州城', True, (0,0,0))
zhou1_t2 = font.render('采桑村', True, (0,0,0))


lock_zhou = False   # 是否锁定选区
lock_city = False   # 是否锁定城市

# 所有州区的城市，按照 '州1-城1'~ '州9-城9'效果排列
flag_s = None   # 保存州?-城？，这个变量有可能变成空白
city_name = None   # 变量保存城市
# 接口
zd = {1: 49, 2: 50, 3: 51, 4: 52, 5: 53, 6: 54, 7: 55, 8: 56, 9: 57}
# 城市的坐标
city_x = [
    # x坐标
    [0,-600,-1200],[-1800,-2400,-3000],[-3600,-4200,-4800],
]
city_y = [
    [0,-600, -1200],
    [-1800,-2400,-3000],
    [-3600, -4200,-4800],
]
return_city = False   # 返回城市视图


# 州
z_names = ['州%s'%i for i in range(1,10)]
# 城市
c_names = ['城%s'%i for i in range(1,10)]
while True:
    c.tick(60)# 判断视图

    screen.fill((0,0,0))
    screen.blit(map_image,map_rect)

    if zooms[0] >= 1800:
        zooms[0] = 1800
        lock_zhou = True   # 地图到达最大1800后锁定，不能操作其他区，除非返回

    if zooms[1] >= 5400:  # 控制地图最大尺寸5400
        zooms[1] = 5400
        lock_city = True  # 锁定城市 5400
        # 如果地图是最大的是时候，把城市去掉
        city_name = None
    if zooms[1] <= 1800:  # 控制地图最大尺寸5400
        zooms[1] = 1800
        lock_city = False  # 锁定城市 5400
    # 放大选中的州,视图是城市的时候才能触发这个
    if glob_view == '城市' and lock_zhou != True:
        map_image = select_zhou(flag, zooms, big_image, map_rect)

    x_zhou1_9 = [0, -600, -1200, -1800, -2400, -3000, -3600, -4200, -4800]
    y_zhou1_9 = [0, -580, -1200, -1800, -2400, -3000, -3600, -4200, -4800]
    # 后续添加一个选城市的函数，现在先用select_zhou的来测试
    if glob_view == '战斗' and lock_city != True and flag=='州1':
        e = select_city(city_name, zooms, big_image, map_rect, x_zhou1_9[0:3], y_zhou1_9[0:3], '州1')
        if e != None:
            map_image = e
    if glob_view == '战斗' and lock_city != True and flag=='州2':
        e = select_city(city_name, zooms, big_image, map_rect, x_zhou1_9[3:6], y_zhou1_9[0:3], '州2')
        if e != None:
            map_image = e
    if glob_view == '战斗' and lock_city != True and flag=='州3':
        e = select_city(city_name, zooms, big_image, map_rect, x_zhou1_9[6:9], y_zhou1_9[0:3], '州3')
        if e != None:
            map_image = e
    if glob_view == '战斗' and lock_city != True and flag=='州4':
        e = select_city(city_name, zooms, big_image, map_rect, x_zhou1_9[0:3], y_zhou1_9[3:6], '州4')
        if e != None:
            map_image = e
    if glob_view == '战斗' and lock_city != True and flag=='州5':
        e = select_city(city_name, zooms, big_image, map_rect, x_zhou1_9[3:6], y_zhou1_9[3:6], '州5')
        if e != None:
            map_image = e
    if glob_view == '战斗' and lock_city != True and flag=='州6':
        e = select_city(city_name, zooms, big_image, map_rect, x_zhou1_9[6:9], y_zhou1_9[3:6], '州6')
        if e != None:
            map_image = e
    if glob_view == '战斗' and lock_city != True and flag=='州7':
        e = select_city(city_name, zooms, big_image, map_rect, x_zhou1_9[0:3], y_zhou1_9[6:9], '州7')
        if e != None:
            map_image = e
    if glob_view == '战斗' and lock_city != True and flag=='州8':
        e = select_city(city_name, zooms, big_image, map_rect, x_zhou1_9[3:6], y_zhou1_9[6:9], '州8')
        if e != None:
            map_image = e
    if glob_view == '战斗' and lock_city != True and flag=='州9':
        e = select_city(city_name, zooms, big_image, map_rect, x_zhou1_9[6:9], y_zhou1_9[6:9], '州9')
        if e != None:
            map_image = e


    # 返回键操作缩小
    if glob_view == '全国':
        zooms[0] -= 20  # 表示慢慢缩小
        map_image = pygame.transform.scale(big_image, (zooms[0], zooms[0])).convert()
        map_rect.y += 20
        map_rect.x += 20
        # 返回到城市的视角 1800,返回到全国视角 600
        if map_rect.x >= 0:
            map_rect.x = 0
        if map_rect.y >= 0:
            map_rect.y = 20
        if zooms[0] <= 600:  # 控制缩小地图的时候最低大小为600
            zooms[0] = 600
            map_image = pygame.transform.scale(big_image, (zooms[0], zooms[0])).convert()
            lock_zhou = False  # 按下空格键解锁 锁定的区域
    # 返回城市
    if glob_view == '城市' and lock_city:
        zooms[1] -= 200
        map_image = pygame.transform.scale(big_image, (zooms[1], zooms[1])).convert()
        print('在这里返回城市选择图')
        if flag == "州1":
            map_rect.x = 0
            map_rect.y = 20
        if flag == "州2":
            map_rect.x = -600
            map_rect.y = 20
        if flag == "州3":
            map_rect.x = -1200
            map_rect.y = 20
        if flag == "州4":
            map_rect.x = 0
            map_rect.y = -580
        if flag == "州5":
            map_rect.x = -600
            map_rect.y = -580
        if flag == "州6":
            map_rect.x = -1200
            map_rect.y = -580
        if flag == "州7":
            map_rect.x = 0
            map_rect.y = -1200
        if flag == "州8":
            map_rect.x = -600
            map_rect.y = -1200
        if flag == "州9":
            map_rect.x = -1200
            map_rect.y = -1200
    if glob_view == "城市" or glob_view == '全国':
        flag_s = None

    # 赋值city_name,判断flag_s不是空白的时候才能赋值,并且没有锁上城市
    if flag_s != '' and flag_s != None and lock_city != True:
        city_name = flag_s
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # 当锁定选州后，才能进行判断
        if lock_zhou:
            # 这个是判断城区
            # if flag_s in z_c_name:
            for k in range(1, 10):  # 城市
                if i.type == pygame.KEYDOWN and i.key == zd[k]:
                    glob_view = '战斗'
                    flag_s = '城%s' % k  # 这里有可能赋值成空白

        if lock_zhou != True:   # 没锁之前，可以进行判断，否则不给判断，避免出现乱修改flag

            if i.type == pygame.KEYDOWN and i.key == pygame.K_1 and glob_view != '战斗':
                glob_view = '城市'  # 1800地图
                flag = '州1'
            elif i.type == pygame.KEYDOWN and i.key == pygame.K_2 and glob_view != '战斗':
                glob_view = '城市'  # 1800地图
                flag = '州2'
            elif i.type == pygame.KEYDOWN and i.key == pygame.K_3 and glob_view != '战斗':
                glob_view = '城市'  # 1800地图
                flag = '州3'
            elif i.type == pygame.KEYDOWN and i.key == pygame.K_4 and glob_view != '战斗':
                glob_view = '城市'  # 1800地图
                flag = '州4'
            elif i.type == pygame.KEYDOWN and i.key == pygame.K_5 and glob_view != '战斗':
                glob_view = '城市'  # 1800地图
                flag = '州5'
            elif i.type == pygame.KEYDOWN and i.key == pygame.K_6 and glob_view != '战斗':
                glob_view = '城市'  # 1800地图
                flag = '州6'
            elif i.type == pygame.KEYDOWN and i.key == pygame.K_7 and glob_view != '战斗':
                glob_view = '城市'  # 1800地图
                flag = '州7'
            elif i.type == pygame.KEYDOWN and i.key == pygame.K_8 and glob_view != '战斗':
                glob_view = '城市'  # 1800地图
                flag = '州8'
            elif i.type == pygame.KEYDOWN and i.key == pygame.K_9 and glob_view != '战斗':
                glob_view = '城市'  # 1800地图
                flag = '州9'
        # # 返回键1
        if i.type == pygame.KEYDOWN and i.key == pygame.K_SPACE and zooms[1] == 5400:
            lock_city = False  # 解锁，可以继续选城市
            # flag_name = "未选择城"
            glob_view = '城市'
            print('返回城市')

        if i.type == pygame.KEYDOWN and i.key == pygame.K_SPACE and zooms[1] == 1800:
            lock_zhou = False  # 按下空格键解锁 锁定的区域
            glob_view = '全国'
            print('返回全国')

    check_key(pygame.K_1, b2[0])
    check_key(pygame.K_2, b2[1], 20, 0)
    check_key(pygame.K_3, b2[2], 20, 0)
    check_key(pygame.K_4, b2[3], 220, 200)
    check_key(pygame.K_5, b2[4], 220, 200)
    check_key(pygame.K_6, b2[5], 220, 200)
    check_key(pygame.K_7, b2[6], 420, 400)
    check_key(pygame.K_8, b2[7], 420, 400)
    check_key(pygame.K_9, b2[8], 420, 400)
    check_key(pygame.K_SPACE, return_b2, 640, 620)  # 空格

    print("视角:%s，flag:%s,zooms[1]:%s, city:%s" %(glob_view, flag, zooms[1], city_name))

    # 方框
    for i in range(len(b1)):
        screen.blit(b1[i].image, b1[i].rect)
        screen.blit(b2[i].image, b2[i].rect)
        # 返回按钮
    screen.blit(return_b1.image, return_b1.rect)
    screen.blit(return_b2.image, return_b2.rect)

    # 字体
    screen.blit(return_text, (230, 660))
    screen.blit(b_text, (280, 100))
    screen.blit(xu_text, (480, 300))
    screen.blit(j_text, (80, 500))
    pygame.display.flip()
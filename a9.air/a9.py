# -*- encoding=utf8 -*-
__author__ = "22120"

from airtest.core.api import *
from time import *
import threading
# import multiprocessing
import sys
import logging

# logger = logging.getLogger('airtest')
# logger.setLevel(logging.WARNING)

ST.OPDELAY = 0.1
ST.THRESHOLD = 0.9
ST.FIND_TIMEOUT = 3
ST.FIND_TIMEOUT_TMP = 2
ST.SAVE_IMAGE = False
auto_setup(__file__, devices=["Android:///"])


class zero:
    #     初始化
    def 初始化():
        keyevent("BACK")

        #         while exists(Template(r"tpl1650084107350.png", record_pos=(0.446, -0.207), resolution=(3120, 1440)))==False and exists(Template(r"tpl1650093039504.png", record_pos=(0.448, -0.205), resolution=(3120, 1440)))==False:

        for i in range(7):
            if exists(Template(r"tpl1650093039504.png", record_pos=(0.448, -0.205), resolution=(3120, 1440))) == False:

                keyevent("BACK")
                sleep(0.5)
                keyevent("BACK")
                sleep(0.5)
                touch((0.9 * w, 0.9 * h))
                keyevent("BACK")
                sleep(0.5)
                keyevent("BACK")
                sleep(0.5)
            else:
                break

        if exists(
                Template(r"tpl1650946032931.png", threshold=0.9, record_pos=(-0.001, 0.079), resolution=(3120, 1440))):
            keyevent("BACK")

    def 过度多人上():
        if exists(Template(r"tpl1650093039504.png", record_pos=(0.448, -0.205), resolution=(3120, 1440))):
            touch((0.6 * w, 0.9 * h), times=2)

    def 过度多人下():
        if exists(Template(r"tpl1650076903619.png", record_pos=(0.111, 0.18), resolution=(3120, 1440))):
            touch((0.4 * w, 0.6 * h))
        elif exists(Template(r"tpl1650073628578.png", record_pos=(0.111, 0.182), resolution=(3120, 1440))):
            touch((0.6 * w, 0.9 * h))
            sleep(0.5)
            wait(Template(r"tpl1650076903619.png", record_pos=(0.111, 0.18), resolution=(3120, 1440)))
            touch((0.4 * w, 0.6 * h))

    def 过度每日(a):
        if exists(Template(r"tpl1650093039504.png", record_pos=(0.448, -0.205), resolution=(3120, 1440))):
            touch((0.4 * w, 0.9 * h), times=2)
        try:
            sleep(0.5)
            wait(Template(r"tpl1654128406528.png", record_pos=(0.432, -0.08), resolution=(3120, 1440)))
        except:
            pass

        #         if exists(Template(r"tpl1651044974045.png", rgb=True, record_pos=(0.409, -0.141), resolution=(3120, 1440))) or exists(Template(r"tpl1651045012507.png", rgb=True, record_pos=(0.409, -0.14), resolution=(3120, 1440))):

        #             raise
        #         else:
        #             pass

        if a == int(0):
            try:
                touch(Template(r"tpl1667471707905.png", record_pos=(0.104, 0.164), resolution=(3120, 1440)), times=2)


            except:
                swipe((0.5 * w, 0.8 * h), vector=[-0.5, 0])
                sleep(2)
                try:
                    touch(Template(r"tpl1667471707905.png", record_pos=(0.104, 0.164), resolution=(3120, 1440)),
                          times=2)
                except:
                    pass



        else:
            touch((a * 0.12 * w, 0.8 * h), times=2)

    def 过度赛季寻车():
        sleep(0.5)
        wait(Template(r"tpl1650093039504.png", record_pos=(0.448, -0.205), resolution=(3120, 1440)))
        touch((0.3 * w, 0.9 * h))
        sleep(0.5)
        wait(Template(r"tpl1651218481188.png", record_pos=(-0.193, 0.183), resolution=(3120, 1440)))
        touch(Template(r"tpl1651218499381.png", record_pos=(-0.431, -0.094), resolution=(3120, 1440)))
        sleep(0.5)
        wait(Template(r"tpl1651218532029.png", record_pos=(-0.239, -0.078), resolution=(3120, 1440)))
        touch(Template(r"tpl1651218532029.png", record_pos=(-0.239, -0.078), resolution=(3120, 1440)))

    def 生涯刷钱():
        sleep(0.5)
        wait(Template(r"tpl1650093039504.png", record_pos=(0.448, -0.205), resolution=(3120, 1440)))
        touch((0.9 * w, 0.9 * h), times=2)
        sleep(0.5)
        wait(Template(r"tpl1651547398554.png", record_pos=(-0.329, 0.201), resolution=(3120, 1440)))
        touch((0.75 * w, 0.95 * h))
        touch(Template(r"tpl1651547607967.png", record_pos=(0.227, -0.106), resolution=(3120, 1440)))

    def 过度赛季赛事():
        sleep(0.5)
        wait(Template(r"tpl1650093039504.png", record_pos=(0.448, -0.205), resolution=(3120, 1440)))
        touch((0.3 * w, 0.9 * h))
        sleep(0.5)
        for i in range(3):
            if exists(Template(r"tpl1659844782386.png", record_pos=(-0.318, 0.065), resolution=(3120, 1440))) == False:
                sleep(0.5)
                swipe((0.2 * w, 0.7 * h), vector=[0, -1])
                sleep(0.5)
            else:
                touch(Template(r"tpl1659844782386.png", record_pos=(-0.318, 0.065), resolution=(3120, 1440)), times=2)
                break

    def 初始化多人上():
        zero.初始化()
        zero.过度多人上()

    def 初始化多人下():
        zero.初始化()
        zero.过度多人下()

    def 初始化每日(self):
        zero.初始化()
        zero.过度每日(self)

    def 初始化赛季寻车():
        zero.初始化()
        zero.过度赛季寻车()

    def 初始化生涯刷钱():
        zero.初始化()
        zero.生涯刷钱()

    def 初始化赛季赛事():
        zero.初始化()
        zero.过度赛季赛事()


class one:
    #     选模式
    def 多人上():

        sleep(0.5)
        if exists(Template(r"tpl1650077146189.png", record_pos=(0.134, 0.183), resolution=(3120, 1440))):
            touch(Template(r"tpl1650077146189.png", record_pos=(0.134, 0.183), resolution=(3120, 1440)))
        elif exists(Template(r"tpl1650082350306.png", record_pos=(-0.006, 0.13), resolution=(3120, 1440))):
            touch(Template(r"tpl1650082350306.png", record_pos=(-0.006, 0.13), resolution=(3120, 1440)))
        else:
            zero.初始化多人上()
            one.多人上()

    def 多人下():
        if exists(Template(r"tpl1650077146189.png", record_pos=(0.134, 0.183), resolution=(3120, 1440))):
            touch(Template(r"tpl1650077146189.png", record_pos=(0.134, 0.183), resolution=(3120, 1440)))
        elif exists(Template(r"tpl1650082350306.png", record_pos=(-0.006, 0.13), resolution=(3120, 1440))):
            touch(Template(r"tpl1650082350306.png", record_pos=(-0.006, 0.13), resolution=(3120, 1440)))
        else:
            zero.初始化多人下()
            one.多人下()

    def 每日():
        try:
            sleep(0.5)
            wait(Template(r"tpl1650641664647.png", record_pos=(0.338, 0.178), resolution=(3120, 1440)))
            touch(Template(r"tpl1650641664647.png", record_pos=(0.338, 0.178), resolution=(3120, 1440)))

        except:
            zero.初始化每日
            one.每日

    def 赛季寻车():
        sleep(0.5)
        wait(Template(r"tpl1651218818970.png", record_pos=(-0.401, -0.051), resolution=(3120, 1440)))
        touch((0.9 * w, 0.9 * h))

    def 生涯刷钱():
        #         swipe((2000,200),(2000,1200),times=3,duration=0.01)
        sleep(0.5)
        wait(Template(r"tpl1651221471643.png", record_pos=(0.339, 0.19), resolution=(3120, 1440)))
        swipe((2000, 200), vector=[0, 0.8], duration=0.01)
        swipe((2000, 200), vector=[0, 0.8], duration=0.01)
        sleep(0.5)
        wait(Template(r"tpl1651550044691.png", record_pos=(-0.149, 0.013), resolution=(3120, 1440)))

        touch(Template(r"tpl1651550044691.png", record_pos=(-0.149, 0.013), resolution=(3120, 1440)))
        touch((2500, 1300))

    def 车手联赛():
        sleep(1)
        wait(Template(r"tpl1659341013531.png", record_pos=(0.077, -0.022), resolution=(3120, 1440)))
        try:
            touch(Template(r"tpl1659341035026.png", record_pos=(0.11, -0.021), resolution=(3120, 1440)))
        except:
            if exists(Template(r"tpl1659341052366.png", record_pos=(0.11, 0.068), resolution=(3120, 1440))):
                touch(Template(r"tpl1659341052366.png", record_pos=(0.11, 0.068), resolution=(3120, 1440)))
            else:
                touch(Template(r"tpl1659354210810.png", record_pos=(0.049, 0.07), resolution=(3120, 1440)))
        sleep(0.5)
        wait(Template(r"tpl1659341172016.png", record_pos=(0.334, 0.167), resolution=(3120, 1440)))
        touch(Template(r"tpl1659341183266.png", record_pos=(0.335, 0.166), resolution=(3120, 1440)))


class two:
    #     选车
    def 多人上选车():
        sleep(1)
        wait(Template(r"tpl1659862851179.png", record_pos=(-0.098, 0.066), resolution=(3120, 1440)))

        a = find_all(
            Template(r"tpl1660296282399.png", threshold=0.9, record_pos=(-0.046, 0.033), resolution=(3120, 1440)))
        if a != None:
            x = int(0)
            y = int(0)
            for i in a:
                x1 = i["result"][0]
                y1 = i["result"][1]
                if x1 > x:
                    x = x1
                    y = y1
                elif x1 == x and y1 > y:
                    y = y1
            touch((x, y))
        elif exists(Template(r"tpl1660301133586.png", record_pos=(0.16, 0.181), resolution=(3120, 1440))):
            touch(Template(r"tpl1660301133586.png", record_pos=(0.16, 0.181), resolution=(3120, 1440)))

        else:
            touch((0.63 * w, 0.2 * h))
            sleep(0.5)
            wait(Template(r"tpl1650853151285.png", record_pos=(-0.389, -0.045), resolution=(3120, 1440)))

            a = find_all(
                Template(r"tpl1660296282399.png", threshold=0.9, record_pos=(-0.046, 0.033), resolution=(3120, 1440)))
            if a != None:
                x = int(0)
                y = int(0)
                for i in a:
                    x1 = i["result"][0]
                    y1 = i["result"][1]
                    if x1 > x:
                        x = x1
                        y = y1
                    elif x1 == x and y1 > y:
                        y = y1
                touch((x, y))
            else:
                touch(Template(r"tpl1660301133586.png", record_pos=(0.16, 0.181), resolution=(3120, 1440)))
        sleep(0.5)

        wait(Template(r"tpl1649857446703.png", record_pos=(0.428, -0.002), resolution=(3120, 1440)))

        for i in range(23):
            if exists(Template(r"tpl1650077146189.png", record_pos=(0.134, 0.183), resolution=(3120, 1440))) == False:
                touch((0.35 * w, 0.5 * h))
            else:
                break
        touch(Template(r"tpl1650077146189.png", record_pos=(0.134, 0.183), resolution=(3120, 1440)))
        sleep(0.5)
        wait(Template(r"tpl1649861377674.png", record_pos=(-0.071, 0.136), resolution=(3120, 1440)))
        while exists(Template(r"tpl1649861377674.png", record_pos=(-0.071, 0.136), resolution=(3120, 1440))):
            if exists(Template(r"tpl1649866808747.png", record_pos=(0.351, -0.093), resolution=(3120, 1440))):
                touch(Template(r"tpl1649866808747.png", record_pos=(0.351, -0.093), resolution=(3120, 1440)))
                two.多人上选车()
        if exists(Template(r"tpl1649866808747.png", record_pos=(0.351, -0.093), resolution=(3120, 1440))):
            touch(Template(r"tpl1649866808747.png", record_pos=(0.351, -0.093), resolution=(3120, 1440)))
            two.多人上选车()

    def 多人下选车():
        sleep(3)
        a = find_all(
            Template(r"tpl1660296282399.png", threshold=0.9, record_pos=(-0.046, 0.033), resolution=(3120, 1440)))
        if a != None:
            x = int(0)
            y = int(0)
            for i in a:
                x1 = i["result"][0]
                y1 = i["result"][1]
                if x1 > x:
                    x = x1
                    y = y1
                elif x1 == x and y1 > y:
                    y = y1
            touch((x, y))


        elif exists(Template(r"tpl1650077146189.png", record_pos=(0.134, 0.183), resolution=(3120, 1440))):
            pass
        elif exists(Template(r"tpl1659059559403.png", record_pos=(0.365, 0.174), resolution=(3120, 1440))):
            print('raise跳过')
            raise


        else:
            touch((0.62 * w, 0.2 * h))
            sleep(0.5)
            a = find_all(
                Template(r"tpl1660296282399.png", threshold=0.9, record_pos=(-0.046, 0.033), resolution=(3120, 1440)))
            if a != None:
                x = int(0)
                y = int(0)
                for i in a:
                    x1 = i["result"][0]
                    y1 = i["result"][1]
                    if x1 > x:
                        x = x1
                        y = y1
                    elif x1 == x and y1 > y:
                        y = y1
                touch((x, y))
            else:
                print('raise结束')
                raise

        try:
            sleep(0.5)
            wait(Template(r"tpl1649857446703.png", record_pos=(0.428, -0.002), resolution=(3120, 1440)))
        except:
            pass
        #         while exists(Template(r"tpl1650077146189.png", record_pos=(0.134, 0.183), resolution=(3120, 1440)))==False:
        #             touch(Template(r"tpl1649857446703.png", record_pos=(0.428, -0.002), resolution=(3120, 1440)))
        for i in range(23):
            if exists(Template(r"tpl1650077146189.png", record_pos=(0.134, 0.183), resolution=(3120, 1440))) == False:
                touch((0.35 * w, 0.5 * h))
            else:
                break
        touch(Template(r"tpl1650077146189.png", record_pos=(0.134, 0.183), resolution=(3120, 1440)))
        sleep(0.5)
        wait(Template(r"tpl1649861377674.png", record_pos=(-0.071, 0.136), resolution=(3120, 1440)))
        while exists(Template(r"tpl1649861377674.png", record_pos=(-0.071, 0.136), resolution=(3120, 1440))):
            if exists(Template(r"tpl1649866808747.png", record_pos=(0.351, -0.093), resolution=(3120, 1440))):
                touch(Template(r"tpl1649866808747.png", record_pos=(0.351, -0.093), resolution=(3120, 1440)))
                two.多人下选车()
        if exists(Template(r"tpl1649866808747.png", record_pos=(0.351, -0.093), resolution=(3120, 1440))):
            touch(Template(r"tpl1649866808747.png", record_pos=(0.351, -0.093), resolution=(3120, 1440)))
            two.多人下选车()

    def 每日选车(self):
        if self == 'd':
            abcd = Template(r"tpl1663567530145.png", threshold=0.99, record_pos=(0.418, -0.142), resolution=(3120, 1440))
            ABCD = Template(r"tpl1659888564847.png", threshold=0.95, record_pos=(0.439, -0.02), resolution=(3120, 1440))
        elif self == 'c':
            abcd = Template(r"tpl1663567315761.png", threshold=0.99, record_pos=(0.418, -0.144), resolution=(3120, 1440))
            ABCD = Template(r"tpl1659888618912.png", threshold=0.95, record_pos=(0.143, -0.02), resolution=(3120, 1440))
        elif self == 'b':
            abcd = Template(r"tpl1663567565599.png", threshold=0.99, record_pos=(0.419, -0.145), resolution=(3120, 1440))
            ABCD = Template(r"tpl1663240427283.png", threshold=0.95, record_pos=(-0.263, -0.018),
                            resolution=(3120, 1440))
        sleep(0.5)
        wait(Template(r"tpl1650648319402.png", record_pos=(0.434, -0.123), resolution=(3120, 1440)))

        touch(Template(r"tpl1650648319402.png", record_pos=(0.434, -0.123), resolution=(3120, 1440)))
        sleep(0.5)
        wait(Template(r"tpl1650648380734.png", record_pos=(-0.413, -0.162), resolution=(3120, 1440)))
        touch((0.26 * w, 0.35 * h))
        sleep(0.1)
        touch((0.26 * w, 0.65 * h))
        sleep(0.1)
        touch((0.26 * w, 0.46 * h))
        sleep(0.5)
        touch((0.1 * w, 0.8 * h))

        sleep(1)
        wait(Template(r"tpl1659862851179.png", record_pos=(-0.098, 0.066), resolution=(3120, 1440)))

        if exists(ABCD):
            a = find_all(ABCD)
            if a != None:
                x = int(9999)
                y = int(9999)
                for i in a:
                    x1 = i["result"][0]
                    y1 = i["result"][1]
                    if x1 < x:
                        x = x1
                        y = y1
                    elif x1 == x and y1 < y:
                        y = y1
                touch((x, y))


        else:
            touch((0.99 * w, 0.8 * h))
        sleep(0.5)
        wait(Template(r"tpl1649857446703.png", record_pos=(0.428, -0.002), resolution=(3120, 1440)))
        #         for s in range(self):
        #             touch((0.35*w,0.5*h))
        for i in range(99):
            if exists(abcd) and exists(
                    Template(r"tpl1659884667909.png", record_pos=(0.359, 0.175), resolution=(3120, 1440))):
                touch(Template(r"tpl1659884667909.png", record_pos=(0.359, 0.175), resolution=(3120, 1440)))
                break
            else:
                touch((0.93 * w, 0.5 * h))
                sleep(0.5)

    def 生涯刷钱选车():
        sleep(0.5)
        wait(Template(r"tpl1650963353275.png", record_pos=(-0.101, -0.082), resolution=(3120, 1440)))
        swipe((3000, 900), vector=[-1.2, 0])
        swipe((3000, 900), vector=[-1.2, 0])
        sleep(0.5)
        wait(Template(r"tpl1651551084983.png", record_pos=(0.27, -0.038), resolution=(3120, 1440)))

        touch(Template(r"tpl1651551084983.png", record_pos=(0.27, -0.038), resolution=(3120, 1440)))
        sleep(0.5)
        wait(Template(r"tpl1649857446703.png", record_pos=(0.428, -0.002), resolution=(3120, 1440)))

        for i in range(23):
            if exists(Template(r"tpl1651555586279.png", record_pos=(0.367, 0.174), resolution=(3120, 1440))) == False:
                touch(Template(r"tpl1649857446703.png", record_pos=(0.428, -0.002), resolution=(3120, 1440)))
            else:
                break
        touch(Template(r"tpl1651555586279.png", record_pos=(0.367, 0.174), resolution=(3120, 1440)))

    def 车手联赛选车():
        sleep(0.5)
        wait(Template(r"tpl1659341272821.png", record_pos=(0.354, 0.173), resolution=(3120, 1440)))
        touch(Template(r"tpl1659341272821.png", record_pos=(0.354, 0.173), resolution=(3120, 1440)))
        sleep(1)
        if exists(Template(r"tpl1659859108034.png", record_pos=(-0.047, 0.05), resolution=(3120, 1440))):
            raise
        else:
            pass


class three:
    #     选路线
    def 选择路线开车():
        sleep(0.5)
        wait(Template(r"tpl1649859105505.png", record_pos=(0.413, -0.098), resolution=(3120, 1440)), timeout=90)
        while exists(Template(r"tpl1649859105505.png", record_pos=(0.413, -0.098), resolution=(3120, 1440))):
            touch((0.9 * w, 0.9 * h))
            sleep(0.1)

    #             touch((0.455*w,0.2*h))
    def 每日开车():
        sleep(0.5)
        wait(Template(r"tpl1650648910161.png", record_pos=(0.32, -0.15), resolution=(3120, 1440)), timeout=90)
        mr = int(0)
        while exists(Template(r"tpl1650648910161.png", record_pos=(0.32, -0.15), resolution=(3120, 1440))):
            touch((0.9 * w, 0.9 * h))
            sleep(0.1)

    #             touch((0.455*w,0.2*h))
    def 生涯刷金开车():
        sleep(0.5)
        wait(Template(r"tpl1651554704979.png", record_pos=(0.282, -0.144), resolution=(3120, 1440)), timeout=90)

        while exists(Template(r"tpl1651553034456.png", record_pos=(-0.363, -0.062), resolution=(3120, 1440))):
            touch((0.9 * w, 0.9 * h))

    def 车手联赛开车():
        sleep(0.5)
        wait(Template(r"tpl1651553034456.png", record_pos=(-0.363, -0.062), resolution=(3120, 1440)), timeout=60)
        #         while exists(Template(r"tpl1659341694278.png", record_pos=(0.314, 0.178), resolution=(3120, 1440)))==False:
        #             touch((0.9*w,0.9*h))
        #             touch((0.455*w,0.2*h))
        for i in range(50):
            if exists(Template(r"tpl1659341694278.png", record_pos=(0.314, 0.178), resolution=(3120, 1440))) == False:
                touch((0.9 * w, 0.9 * h))
                touch((0.455 * w, 0.2 * h))
            else:
                break


class four:
    #     结尾点击
    def 结尾():
        i = int(0)
        if exists(Template(r"tpl1649859105505.png", record_pos=(0.413, -0.098), resolution=(3120, 1440))) == False:
            while True:
                touch((0.9 * w, 0.9 * h))
                #         keyevent("BACK")
                i = i + 1
                if i >= 7 or exists(
                        Template(r"tpl1650125765547.png", record_pos=(-0.169, -0.029), resolution=(3120, 1440))):
                    break

    def 每日结尾():
        for i in range(7):
            if exists(Template(r"tpl1651046461620.png", record_pos=(0.339, -0.141), resolution=(3120, 1440))):
                break
            else:
                touch((0.9 * w, 0.9 * h))
        #         while exists(Template(r"tpl1651046461620.png", record_pos=(0.339, -0.141), resolution=(3120, 1440)))==False:
        #             touch((0.9*w,0.9*h))
        for i in range(3):
            if exists(Template(r"tpl1650641664647.png", record_pos=(0.338, 0.178), resolution=(3120, 1440))):
                break
            else:
                sleep(1)
                touch((0.9 * w, 0.9 * h))

        #         while exists(Template(r"tpl1650641664647.png", record_pos=(0.338, 0.178), resolution=(3120, 1440)))==False:
        #             touch((0.9*w,0.9*h))
        touch(Template(r"tpl1650641664647.png", record_pos=(0.338, 0.178), resolution=(3120, 1440)))

    def 赛季寻车结尾():
        temp1 = int(0)
        temp2 = int(0)
        while exists(Template(r"tpl1651046461620.png", record_pos=(0.339, -0.141), resolution=(3120, 1440))) == False:
            temp1 = temp1 + 1
            if temp1 > 9:
                break
            touch((0.9 * w, 0.9 * h))
        while exists(Template(r"tpl1651221471643.png", record_pos=(0.339, 0.19), resolution=(3120, 1440))) == False:
            temp2 = temp2 + 1
            if temp2 > 9:
                break
            touch((0.9 * w, 0.9 * h))
        touch(Template(r"tpl1651221471643.png", record_pos=(0.339, 0.19), resolution=(3120, 1440)))

    def 生涯刷金结尾():

        for i in range(11):
            if exists(Template(r"tpl1650084107350.png", record_pos=(0.446, -0.207), resolution=(3120, 1440))) == False:
                touch((0.9 * w, 0.9 * h))
            else:
                break
        if exists(Template(r"tpl1651556981559.png", record_pos=(-0.418, 0.183), resolution=(3120, 1440))) == False:
            keyevent("BACK")

    def 车手联赛结尾():
        for i in range(5):
            if exists(Template(r"tpl1659341694278.png", record_pos=(0.314, 0.178), resolution=(3120, 1440))):
                touch(Template(r"tpl1659341694278.png", record_pos=(0.314, 0.178), resolution=(3120, 1440)))
            else:
                pass


def 免费包():
    if exists(Template(r"tpl1651112588763.png", record_pos=(-0.002, -0.206), resolution=(3120, 1440))):
        touch((0.5 * w, 0.05 * h))
        print('发现免费包')
        sleep(0.5)
        wait(Template(r"tpl1651112713696.png", record_pos=(-0.071, -0.06), resolution=(3120, 1440)))
        touch((0.5 * w, 0.9 * h))
        sleep(0.5)
        wait(Template(r"tpl1651112814759.png", record_pos=(0.326, -0.12), resolution=(3120, 1440)))
        touch((0.5 * w, 0.9 * h))
    else:
        pass


# 后面接初始化

def 多人上循环():
    try:
        one.多人上()
        two.多人上选车()
        three.选择路线开车()
        four.结尾()
    except:
        zero.初始化多人上()
        多人上循环()


def 多人下循环():
    try:
        one.多人下()


    except:
        zero.初始化多人下()
        多人下循环()
    two.多人下选车()
    try:
        three.选择路线开车()
        four.结尾()
    except:
        zero.初始化多人下()
        多人下循环()


def 每日循环(a, b):
    try:
        one.每日()
        two.每日选车(b)

    except:
        zero.初始化每日(a)
        每日循环(a, b)
    sleep(1)
    if exists(Template(r"tpl1651053137963.png", record_pos=(0.169, -0.146), resolution=(3120, 1440))):
        keyevent("BACK")
        sleep(0.5)
        wait(Template(r"tpl1650644657193.png", record_pos=(0.358, 0.177), resolution=(3120, 1440)))
        touch((0.52 * w, 0.9 * h))
        raise
    else:
        pass
    try:
        three.每日开车()
        four.每日结尾()
    except:
        zero.初始化每日(a)
        每日循环(a, b)


def 赛季寻车循环(a):
    try:
        one.赛季寻车()
        two.每日选车(a)
    except:
        zero.初始化赛季寻车()
        赛季寻车循环()
    sleep(1)
    if exists(Template(r"tpl1651053137963.png", record_pos=(0.169, -0.146), resolution=(3120, 1440))):
        keyevent("BACK")
        sleep(0.5)
        wait(Template(r"tpl1650644657193.png", record_pos=(0.358, 0.177), resolution=(3120, 1440)))
        touch((0.52 * w, 0.9 * h))
        raise
    else:
        pass
    try:
        three.每日开车()
        four.赛季寻车结尾()
    except:
        zero.初始化赛季寻车()
        赛季寻车循环(a)


def 生涯刷金循环():
    try:
        one.生涯刷钱()
        two.生涯刷钱选车()
        three.生涯刷金开车()
        four.生涯刷金结尾()
    except:
        zero.初始化生涯刷钱()
        生涯刷金循环()


def 车手联赛循环():
    try:

        one.车手联赛()

    except:
        zero.初始化赛季赛事
        车手联赛循环()

    two.车手联赛选车()

    try:
        three.车手联赛开车()
        four.车手联赛结尾()
    except:
        zero.初始化赛季赛事
        车手联赛循环()


if __name__ == '__main__':
    w, h = device().get_current_resolution()  # 获取屏幕宽高
    if w < h:  # 根据宽高判断打开游戏
        try:
            start_app("com.gameloft.android.ANMP.GloftA9HM")
            sleep(0.5)
            wait(Template(r"tpl1650093039504.png", record_pos=(0.448, -0.205), resolution=(3120, 1440)), timeout=90)
            w, h = device().get_current_resolution()
        except:
            pass
#     shell("settings put system screen_brightness 1")  # 调低亮度


    def 脚本():
        n = int(0)
        while True:
            print('开始运行脚本')
            begin_time = time()
            #             免费包()

#             zero.初始化每日(0)
#             for i in range(5):
#                 print('每日' + str(i + 1))
#                 try:
#                     t1 = time()
#                     每日循环(int(0), str('d'))
#                     print(str(time() - t1) + '秒')
#                 except:
#                     break

            #             zero.初始化赛季寻车()
            #             for i in range(5):
            #                 print('赛季寻车'+str(i+1))
            #                 try:
            #                     t1=time()
            #                     赛季寻车循环(int(20))
            #                     print(str(time()-t1)+'秒')
            #                 except:
            #                     break

            #             zero.初始化赛季赛事()
            #             for i in range(5):
            #                 t1=time()
            #                 print('赛季赛事'+str(i+1))
            #                 try:
            #                     车手联赛循环()
            #                     print(str(time()-t1)+'秒')
            #                 except:
            #                     break

            zero.初始化多人下()
            for i in range(3):
                t1 = time()
                print('多人下' + str(i + 1))
                try:
                    多人下循环()
                    print(str(time() - t1) + '秒')
                except:
                    break

            zero.初始化多人上()
            for i in range(99):
                t1 = time()
                print('多人上' + str(i + 1))
                多人上循环()
                print(str(time() - t1) + '秒')

            #             zero.初始化生涯刷钱()
            #             for i in range(19):
            #                 t1=time()
            #                 print('生涯刷钱'+str(i+1))
            #                 生涯刷金循环()
            #                 print(str(time()-t1)+'秒')

            end_time = time()
            n = n + 1
            print('第{0}轮运行结束，用时{1}秒'.format(n, end_time - begin_time))
            d = shell("dumpsys battery | grep level")
            d = str(d)
            d = d.split(':')
            print('电量：' + d[1])


    def 监听来电():
        print('开始监听来电')

        d = shell("dumpsys battery | grep level")
        d = str(d)
        d = d.split(':')
        print('电量：' + d[1])

        m = shell("dumpsys telephony.registry | grep mCallState")
        while True:
            if m == shell("dumpsys telephony.registry | grep mCallState") and int(d[1]) >= 0:
                sleep(1)
                d = shell("dumpsys battery | grep level")
                d = str(d)
                d = d.split(':')
            elif m != shell("dumpsys telephony.registry | grep mCallState"):
                print('来电？')
                break
            elif int(d[1]) < 1:
                print('电量不足？')
                break

        shell("settings put system screen_brightness 100")
        stop_app("com.gameloft.android.ANMP.GloftA9HM")
        print('停止监听来电')
        sys.exit()


    threading.Thread(target=脚本).start()
    监听来电()




# -*- encoding=utf8 -*-
__author__ = "22120"

from airtest.core.api import *
from time import *
ST.OPDELAY=0.1
ST.THRESHOLD=0.8
ST.FIND_TIMEOUT=3
ST.FIND_TIMEOUT_TMP=2
auto_setup(__file__)
class zero:
#     初始化
    def 初始化():
        keyevent("BACK")

        while exists(Template(r"tpl1650084107350.png", record_pos=(0.446, -0.207), resolution=(3120, 1440)))==False and exists(Template(r"tpl1650093039504.png", record_pos=(0.448, -0.205), resolution=(3120, 1440)))==False:
            keyevent("BACK")
            touch((0.9*w,0.9*h)) 

        sleep(2)


        if exists(Template(r"tpl1650136816217.png", record_pos=(-0.006, -0.001), resolution=(2340, 1080))):
            keyevent("BACK")

        if exists(Template(r"tpl1650084107350.png", record_pos=(0.446, -0.207), resolution=(3120, 1440))):
                touch(Template(r"tpl1650084107350.png", record_pos=(0.446, -0.207), resolution=(3120, 1440)))
    def 过度多人上():
        if exists(Template(r"tpl1650076903619.png", record_pos=(0.111, 0.18), resolution=(3120, 1440))):
            touch(Template(r"tpl1650076903619.png", record_pos=(0.111, 0.18), resolution=(3120, 1440)))
        elif exists(Template(r"tpl1650073628578.png", record_pos=(0.111, 0.182), resolution=(3120, 1440))):
            touch(Template(r"tpl1650073628578.png", record_pos=(0.111, 0.182), resolution=(3120, 1440)))
            touch(Template(r"tpl1650076903619.png", record_pos=(0.111, 0.18), resolution=(3120, 1440)))
    def 过度多人下():
        if exists(Template(r"tpl1650076903619.png", record_pos=(0.111, 0.18), resolution=(3120, 1440))):
            touch((0.4*w,0.6*h))
        elif exists(Template(r"tpl1650073628578.png", record_pos=(0.111, 0.182), resolution=(3120, 1440))):
            touch(Template(r"tpl1650073628578.png", record_pos=(0.111, 0.182), resolution=(3120, 1440)))
            wait(Template(r"tpl1650076903619.png", record_pos=(0.111, 0.18), resolution=(3120, 1440)))
            touch((0.4*w,0.6*h))
    def 过度每日(self):
        if exists(Template(r"tpl1650093039504.png", record_pos=(0.448, -0.205), resolution=(3120, 1440))):
            touch((0.4*w,0.9*h),times=2)
        wait(Template(r"tpl1650640361028.png", record_pos=(-0.395, 0.129), resolution=(3120, 1440)))
        touch((self*0.12*w,0.8*h),times=2)


    def 初始化多人上():
        zero.初始化()
        zero.过度多人上()
    def 初始化多人下():
        zero.初始化()
        zero.过度多人下()
    def 初始化每日(self):
        zero.初始化()
        zero.过度每日(self)
class one:
#     选模式
    def 多人上():
        
    
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
            初始化多人下()
            多人下()
    def 每日():
        if exists(Template(r"tpl1650641664647.png", record_pos=(0.338, 0.178), resolution=(3120, 1440))):
            touch(Template(r"tpl1650641664647.png", record_pos=(0.338, 0.178), resolution=(3120, 1440)))

class two:
#     选车
    def 多人上选车():
        try:
            touch(Template(r"tpl1650266426795.png", record_pos=(0.326, 0.112), resolution=(3120, 1440)))


        except:
            try:
                touch(Template(r"tpl1649856850850.png", record_pos=(0.128, -0.127), resolution=(3120, 1440)))
            except:
                zero.初始化多人上()
                one.多人上()
                two.多人上选车()
            sleep(2)
            touch((0.8*w,0.8*h))
        try:
            touch(Template(r"tpl1650077146189.png", record_pos=(0.134, 0.183), resolution=(3120, 1440)))
        except:
            touch(Template(r"tpl1649857446703.png", record_pos=(0.428, -0.002), resolution=(3120, 1440)))
            while exists(Template(r"tpl1650077146189.png", record_pos=(0.134, 0.183), resolution=(3120, 1440)))==False:
                touch(Template(r"tpl1649857446703.png", record_pos=(0.428, -0.002), resolution=(3120, 1440)))
            touch(Template(r"tpl1650077146189.png", record_pos=(0.134, 0.183), resolution=(3120, 1440)))
        wait(Template(r"tpl1649861377674.png", record_pos=(-0.071, 0.136), resolution=(3120, 1440)))
        while exists(Template(r"tpl1649861377674.png", record_pos=(-0.071, 0.136), resolution=(3120, 1440))):
            if exists(Template(r"tpl1649866808747.png", record_pos=(0.351, -0.093), resolution=(3120, 1440))):
                touch(Template(r"tpl1649866808747.png", record_pos=(0.351, -0.093), resolution=(3120, 1440)))
                two.多人上选车()
        if exists(Template(r"tpl1649866808747.png", record_pos=(0.351, -0.093), resolution=(3120, 1440))):
            touch(Template(r"tpl1649866808747.png", record_pos=(0.351, -0.093), resolution=(3120, 1440)))
            two.多人上选车()
    def 多人下选车():
        wait(Template(r"tpl1650545811552.png", record_pos=(-0.335, 0.181), resolution=(3120, 1440)))
#         try:
#             touch(Template(r"tpl1650545811552.png", record_pos=(-0.335, 0.181), resolution=(3120, 1440)))



#         except:
        if exists(Template(r"tpl1650545963832.png", record_pos=(0.415, -0.128), resolution=(3120, 1440))):

            touch((0.62*w,0.2*h))
            if exists(Template(r"tpl1650545811552.png", record_pos=(-0.335, 0.181), resolution=(3120, 1440))):
                touch(Template(r"tpl1650545811552.png", record_pos=(-0.335, 0.181), resolution=(3120, 1440)))
            else:
                touch(Template(r"tpl1650606812184.png", record_pos=(-0.328, 0.181), resolution=(3120, 1440)))




        else:
            zero.初始化多人下()
            one.多人下()
            two.多人下选车()
#             sleep(2)
#             touch((0.8*w,0.8*h))
        try:
            touch(Template(r"tpl1650077146189.png", record_pos=(0.134, 0.183), resolution=(3120, 1440)))
        except:
            touch(Template(r"tpl1649857446703.png", record_pos=(0.428, -0.002), resolution=(3120, 1440)))
            while exists(Template(r"tpl1650077146189.png", record_pos=(0.134, 0.183), resolution=(3120, 1440)))==False:
                touch(Template(r"tpl1649857446703.png", record_pos=(0.428, -0.002), resolution=(3120, 1440)))
            touch(Template(r"tpl1650077146189.png", record_pos=(0.134, 0.183), resolution=(3120, 1440)))
        wait(Template(r"tpl1649861377674.png", record_pos=(-0.071, 0.136), resolution=(3120, 1440)))
        while exists(Template(r"tpl1649861377674.png", record_pos=(-0.071, 0.136), resolution=(3120, 1440))):
            if exists(Template(r"tpl1649866808747.png", record_pos=(0.351, -0.093), resolution=(3120, 1440))):
                touch(Template(r"tpl1649866808747.png", record_pos=(0.351, -0.093), resolution=(3120, 1440)))
                two.多人下选车()
        if exists(Template(r"tpl1649866808747.png", record_pos=(0.351, -0.093), resolution=(3120, 1440))):
            touch(Template(r"tpl1649866808747.png", record_pos=(0.351, -0.093), resolution=(3120, 1440)))
            two.多人下选车()
    def 每日选车(self):
        
        wait(Template(r"tpl1650647401621.png", record_pos=(0.272, -0.144), resolution=(3120, 1440)))

        
        touch(Template(r"tpl1650648319402.png", record_pos=(0.434, -0.123), resolution=(3120, 1440)))
        wait(Template(r"tpl1650648380734.png", record_pos=(-0.413, -0.162), resolution=(3120, 1440)))
        touch((0.26*w,0.35*h))
        sleep(1)
        touch((0.1*w,0.8*h))
        wait(Template(r"tpl1650647401621.png", record_pos=(0.272, -0.144), resolution=(3120, 1440)))
        touch((0.2*w,0.5*h))
        wait(Template(r"tpl1650644657193.png", record_pos=(0.358, 0.177), resolution=(3120, 1440)))
        for s in range(self-1):
            touch(Template(r"tpl1649857446703.png", record_pos=(0.428, -0.002), resolution=(3120, 1440)))
        try:
            touch(Template(r"tpl1650077146189.png", record_pos=(0.134, 0.183), resolution=(3120, 1440)))
        except:
            touch(Template(r"tpl1649857446703.png", record_pos=(0.428, -0.002), resolution=(3120, 1440)))
            while exists(Template(r"tpl1650077146189.png", record_pos=(0.134, 0.183), resolution=(3120, 1440)))==False:
                touch(Template(r"tpl1649857446703.png", record_pos=(0.428, -0.002), resolution=(3120, 1440)))
            touch(Template(r"tpl1650077146189.png", record_pos=(0.134, 0.183), resolution=(3120, 1440)))

class three:
#     选路线
    def 选择路线开车():
        wait(Template(r"tpl1649859105505.png", record_pos=(0.413, -0.098), resolution=(3120, 1440)),timeout=30)
        while exists(Template(r"tpl1649859105505.png", record_pos=(0.413, -0.098), resolution=(3120, 1440))):
            touch((0.9*w,0.9*h))
    def 每日开车():
        wait(Template(r"tpl1650648910161.png", record_pos=(0.32, -0.15), resolution=(3120, 1440)),timeout=30)
        while exists(Template(r"tpl1650648910161.png", record_pos=(0.32, -0.15), resolution=(3120, 1440))):
            touch((0.9*w,0.9*h))

class four:
#     结尾点击
    def 结尾():
        i=int(0)
        while exists(Template(r"tpl1649859105505.png", record_pos=(0.413, -0.098), resolution=(3120, 1440)))==False:
            touch((0.9*w,0.9*h))
    #         keyevent("BACK")

            i=i+1
            if i>=5 or exists(Template(r"tpl1650125765547.png", record_pos=(-0.169, -0.029), resolution=(3120, 1440))):
                break
            else:
                touch((0.9*w,0.9*h))


    
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
        two.多人下选车()
        three.选择路线开车()
        four.结尾()
    except:
        zero.初始化多人下()
        多人下循环()
def 每日循环(a,b):
    try:
        zero.初始化每日(a)
        one.每日()
        two.每日选车(b)
        three.每日开车()
    except:
        zero.初始化每日(a)
        每日循环(a,b)
if __name__=='__main__':
    w,h=device().get_current_resolution()
    if w<h:
        try:
            start_app("com.gameloft.android.ANMP.GloftA9HM")
            wait(Template(r"tpl1650093039504.png", record_pos=(0.448, -0.205), resolution=(3120, 1440)),timeout=60)
            w,h=device().get_current_resolution()
        except:
            pass
    n=int(0)
    shell("settings put system screen_brightness 1")
    while True:
        begin_time=time()
#         多人下循环()

        zero.初始化多人上()
        for i in range(20):
            print('up'+str(i))
            多人上循环()
            
        zero.初始化多人下()
        for j in range(4):
            print('down'+str(j))
            多人下循环()
            
        for k in range(4):
            每日循环(int(7),int(24))    
        end_time=time()
        n=n+1
        print('第{0}轮运行结束，用时{1}秒'.format(n,end_time-begin_time))
        

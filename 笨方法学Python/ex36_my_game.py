# 完成一个软件的最好方式是把它们拆解为像下面这样的小块：
# 1、在纸上写下你完成这个软件所需要做的所有任务。这就是你的待办事项列表。
# 2、先找到你列表中最容易的事情。
# 3、在你的源代码中增加注释，作为你完成这项任务的指南。
# 4、在这些注释下面，开始编码。
# 5、然后立即运行你的代码，看它是否正常工作。
# 6、循环的进行代码编写，测试运行，以及代码修正。
# 7、在你的列表中划掉刚完成的任务，然后再挑选下一个最容易完成的任务，重复进行以上步骤。

from sys import exit  # 引入exit模块
import datetime  # 引入日期时间包
import time  # 引入时间包


# 输出一个分割行
def print_line(line_style='-', line_number=60):
    '''line_style为输出线条的样式，默认为-；line_number为输出线条的长短，默认为40'''
    print(line_style * line_number)


# 输出一个进度条
def print_wait(wait_time=60, sleep=0.01, symbol='<'):
    '''输出一个等候沙漏'''
    wait = ['|', '/', '-', '|', '\\', symbol]
    while wait_time >= 0:
        wait_time -= 1
        for w in wait:
            time.sleep(0.01)
            print("." * wait_time + "%s\r" % w, end='')
    print('\n')


# 获取冒险者信息
def welcome():
    '''返回用户信息列表，列表格式为[姓名, 性别, 年龄]'''
    print("欢迎光临冒险岛游戏，现在请输入您的个人信息！")
    name = input("请输入您的姓名？> ")
    sex = input("请输入您的性别？> ")
    old = input("请输入您的年龄？> ")
    return [name, sex, old]


# 死亡模块
def die(info, life=False):
    '''输出info的内容并退出程序'''
    life_end_time = datetime.datetime.now()
    life_seconds = (life_end_time - life_start_time).seconds
    print_line('=')
    print(info)
    if life == False:
        print("感受着生命的流逝。。。您将死去。。。")
        print_wait(symbol='^')
        print("\t姓名：%s 性别：%s 年龄：%s岁" % (use_name, use_sex, use_old))
        print("\t开始冒险时间：%s\n\t于%s在冒险中不幸消亡。。。\n" % (
            life_start_time.strftime('%Y/%m/%d %H:%M:%S'), life_end_time.strftime('%Y/%m/%d %H:%M:%S')))
    elif life:
        print("恭喜你%s，勇敢的冒险者！\n你战胜了恐惧、贪婪和怯懦。完美成功的完成了这次冒险！" % use_name)
        print_wait()
        print("\t姓名：%s 性别：%s 年龄：%s岁" % (use_name, use_sex, use_old))
        print("\t开始冒险时间：%s\n\t于%s成功冒险并离开。。。\n" % (
            life_start_time.strftime('%Y/%m/%d %H:%M:%S'), life_end_time.strftime('%Y/%m/%d %H:%M:%S')))
    print_wait(symbol='@')
    print("欢迎下次再来冒险岛！")
    exit(0)


# 死亡之眼的房间
# 给出提示并让选择，如果在20秒内做出了逃跑选择，就能够逃出，否则也将死亡
def eye_rm(from_rm, first_in=True):
    '''from_rm为调用此模块的房间名'''
    print_line()
    starttime = datetime.datetime.now()  # 获取现在时刻
    if first_in:
        print("""
        这是一间漆黑的房间
        在房间的中央悬浮着一只巨大的眼睛
        这只眼睛现在还没有睁开。。。
        """)
    else:
        print("你又回到了这间有着巨大眼睛的房间。。。")
    choise = input("请尽快做出选择(逃跑或者等待)？> ")

    endtime = datetime.datetime.now()  # 获取用于计算时间差的现在时刻
    second = (endtime - starttime).seconds  # 计算时间差
    if choise == '逃跑' and second < 20:
        print("\n你成功逃出了这个可怕的房间！")
        if from_rm == 'gards_rm':
            print("你又回到那间满是可怕守卫的房间。。。")
            gards_rm(True)
        elif from_rm == 'trap_rm':
            print("你又回到了这个满是陷阱的房间。。。")
            trap_rm(True)
        else:
            die("天降神罚，你被一团烈火包裹。。。")
    elif choise == '逃跑' and second >= 20:
        die("时间到！那只眼睛猛地睁了开来。。。\n发出了可怕的光芒，将你笼罩。。。")
    elif choise == '等待':
        die("你选择了等待。。。那只眼睛慢慢地睁了开来。。。\n发出可怕的光芒，将你笼罩。。。")
    else:
        die("你没有做出正确的选择！那只眼睛突然睁了开来。。。\n发出可怕的光芒，将你笼罩。。。")


# 守卫房间
def gards_rm(isrun=False):
    '''满是守卫的房间：isrun将反应进入这间房间的形式，True = 逃跑进入，False = 正常进入'''
    print_line()
    if isrun == False:
        print("""
    这是一间普通的房间，在房间里散坐着一些
    正在打瞌睡的守卫。在他们的手边放着他们
    的随身武器。在房间的左边有扇门，这扇门
    很普通。。。
        """)
        choise_info = "请做出选择(退回、无声去开门或嘲讽)？> "
    else:
        print("你又逃到了这间满是守卫的房间。\n还算好，这些守卫还没有醒。")
        choise_info = "请做出选择(退回、逃出或嘲讽)？> "

    choise = input(choise_info)

    if choise == '嘲讽':
        die("你对着这些守卫大喊大叫，被吵醒的守卫们大怒！\n他们拿着武器向你杀来。。。")
    elif choise == '退回' and isrun == False:
        print("你退回了进来的那个房间。")
        start(False)
    elif choise == '退回' and isrun:
        print("你退回到了那间有着巨大眼睛的房间！")
        eye_rm('gards_rm', False)
    elif choise in ['无声去开门', '无声', '开门'] and isrun == False:
        print("你蹑手蹑脚地绕开守卫，轻轻地打开了不知通往哪里的门。")
        eye_rm('gards_rm')
    elif choise == '逃出' and isrun:
        print("你小心地绕过守卫，逃回到了进入这间房间的那个房间。")
        start(False)
    else:
        die("你没有做出正确的选择！被四周突然\n出现的利刃切割得鲜血淋淋。。。")


# 陷阱房间
def trap_rm(isrun=False):
    '''满是陷阱的房间：isrun将反应进入这间房间的形式，True = 逃跑进入，False = 正常进入'''
    print_line()
    if isrun == False:
        print("""
    你观察着四周，发现这间房间里除了门边的一块
    石头外空无一物。。。在你的右侧有着一扇隐隐
    透出黑色光芒的门，在门口的地上有着奇怪的花
    纹。
        """)
        choise_info = "请做出你的选择(石头、打开右边的门进入或退回)？> "
    elif isrun == True:
        print("你又回到了这间满是陷阱的房间。。。")
        choise_info = "请做出你的选择(退出或者回去)？> "

    choise = input(choise_info)

    if choise == '石头' and isrun == False:
        print("\n你拿起石头往那扇门下的奇怪花纹丢去，\n突然从门口两边的墙里弹出无数闪着寒芒的钢针。。。")
        print("你绕过陷阱，进入到了那扇门里。")
        print_wait()
        eye_rm('trap_rm')
    elif choise in ['打开右边的门进入', '打开', '进入'] and isrun == False:
        die("你走到那扇透出光芒的门口，正准备打开门得时候\n突然被两边墙里弹出的无数钢针射中\n像个刺猬一样倒在了血泊中。。。")
    elif choise in ['退回', '退出']:
        print("进入到了最开始来这间房间的那扇门中。")
        start(False)
    elif choise == '回去' and isrun == True:
        print("你想想有些不对劲，感觉那间有着巨大眼睛的房间\n还有什么你没有发现的秘密。所以又退了回去！")
        eye_rm('trap_rm', False)
    else:
        die("天降神雷，将你劈得飞了出去。。。")


# 熊的房间
def bear_rm(isrun=False, treasuy_box=False):
    '''有头熊的房间：isrun将反应进入这间房间的形式，True = 逃跑进入，False = 正常进入'''
    print_line()
    if isrun == False:
        print("""
    你进入到了一间有着森林气息的房间，
    在房间的左侧有着一扇不知道通往哪里
    的门。在门的不远处有着一头巨大的白
    熊，这头白熊正半眯着眼睛打着呼噜。。。
    在你不远处的地上有着一罐蜂蜜，在另
    一边的地上散乱地堆着一些石头。
        """)
        info_for_choice = "你将要如何选择呢？(蜂蜜、石头、嘲讽和退回) > "
    else:
        print("你又回到了这间有着巨熊的房间，巨熊正在不远处瞪着你！")
        info_for_choice = "你将要如何选择呢？(蜂蜜、石头、嘲讽和退回宝库) > "
    choise = input(info_for_choice)
    if choise == '蜂蜜' and isrun == False:
        print("巨熊被蜂蜜引开了，你蹑手蹑脚地进入了那扇神秘的门。。。")
        treasuy_rm()
    elif choise == '蜂蜜' and isrun:
        die("蜂蜜已经被你用掉了。。。巨熊一下扑了上来，\n血盆大口一下把你的手臂给咬住了。。。")
    elif choise == '石头'and isrun == False:
        die("你把石头砸到了巨熊的头上，它被你激怒了。\n扑上来一口咬住了你的大腿。。。")
    elif choise == '嘲讽':
        die("巨熊被你激怒了！！！一下扑到你的身上，咬\n住了你的脖子。。。")
    elif (choise == '退回' or choise == '退回宝库') and isrun == False:
        print("看到巨熊的你被吓呆了，想也没想就退了出去。")
        start(False)
    elif (choise == '退回' or choise == '退回宝库') and isrun:
        print("你在巨熊还没有反应过来的时候，退回了宝库！")
        treasuy_rm(True, treasuy_box)
    else:
        die("你做出了另类的选择，被一道天雷击中。。。")


# 宝藏屋
def treasuy_rm(isrun=False, treasuy_box=False):
    '''满是宝藏的房间'''
    print_line()
    if isrun == False:
        print("""
    你进入了一间金碧辉煌的房间，房间内
    到处都是金银珠宝。在房间的中央有一
    个巨大的宝箱散发着耀眼的光芒！在宝箱
    的下方有着一个散发着黑色光芒又有些类
    似门的东西。
        """)
    elif isrun and treasuy_box:
        die("你退回到了这间金碧辉煌的房间，前无去\n路后有大熊。现在已经走投无路了。。。")
    else:
        print("你又回到了这间金碧辉煌的房间。")
    while True:
        choise = input("请做出你的选择(宝箱、传送门或者退回)？> ")

        if choise == '宝箱' and treasuy_box == False:
            print_line()
            print("你小心翼翼地打开了宝箱。。。")
            print_wait()
            print("当你正在为宝箱里的各类宝物而兴奋的时候，\n突然发现那个散发着光芒的传送门不见了。。。\n")
            treasuy_box = True
        elif choise == '宝箱' and treasuy_box:
            print("宝箱已经被你打开了！！！\n")
        elif choise == '传送门' and treasuy_box == False:
            die("""
    你怀着忐忑的心情进入了那个散发着
    黑色光芒的传送门里，突然传送门散
    发出了一阵刺眼的光芒。你消失在了
    这个金币辉煌的房间。。。
            """, True)
        elif choise == '退回':
            print("你退出了这间房间。")
            bear_rm(True, treasuy_box)
        else:
            die("你做出了错误的选择！凭空降下一道天雷将你打的浑身\n焦黑。。。")


# 起 点
def start(first_start=True):
    '''起始房间'''
    while True:
        print_line()
        if first_start:
            print("""
    当你慢慢地醒来的时候，发现已经
    身处一间漆黑漆黑一片的房间。
    。。。。。。
    你努力地站了起来，仔细观察着四周；
    发现这间房间里什么都没有，只有不知
    通往哪里的3扇门。。。
    左边的是一扇黄色的门，右边的是一扇
    红色的门，在你的后面还有一扇发着淡淡
    荧光的门。。。
            """)
            first_start = False
        else:
            print("你又回到了刚醒来时的房间，\n这里有3扇不知通向哪里的门。")
        choise = input("请做出你的选择(左、右或者后)？> ")
        if choise == '左':
            bear_rm()
        elif choise == '右':
            trap_rm()
        elif choise == '后':
            gards_rm()
        elif choise == 'test':
            break
        else:
            print("脑海里响起一个突兀的声音！%s请做出正确的选择！！！\n然后你突然感觉脑袋一疼，晕了过去。。。" % use_name)
            print_wait()
            first_start = True


life_start_time = datetime.datetime.now()
print_line()
use_name, use_sex, use_old = welcome()
start()

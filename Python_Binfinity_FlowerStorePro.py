import time  # 引入设计进度条的相关库
import json

# 初始化
# 设置起始时间戳
start = time.perf_counter()
# 全局定义：
# 花卉信息总类"次数"：listtime = lt
lt = 3
# 花卉总数为：sum
sum = 0
# 循环介质置零：i
i = 0
# 内嵌默认管理员账户
defaultuser = {'name': 'Binfinity', 'passwd': '050328Cb'}  # 设置默认管理员账户
# 检索现有的鲜花内容：
try:
    file = open('flowers.txt', "r", encoding='utf-8')
except FileNotFoundError:
    print(
        """
----========================----
            未找到仓库
----========================----
        """
    )
else:
    contents = file.readlines()  # 将文件中的所有行都读入contents列表中
    # 将默认花卉信息导入至花卉列表：
    flower = []
    for content in contents:
        flower.append(content[3:-1])
    tempsum = int(len(flower) / lt)


# 蜜汁进度条：
def Progress_bar():
    scale = 50
    print('加载中'.center(scale // 2, '-'))
    for i in range(scale + 1):
        a = '*' * i
        b = '.' * (scale - i)
        c = (i / scale) * 100
        dur = time.perf_counter() - start
        print('\r{:^3.0f}%[{}->{}]{:.2f}s'.format(c, a, b, dur), end='')
        time.sleep(0.1)
    print('\n' + '加载完成'.center(scale // 2, '-'))
    print(
        """
    ★~☆·☆。~*∴*~★*∴ *·∴~*★*∴*★~☆·☆。~*∴*~★

    の┅∞   欢迎来到 Binfinity FlowerStore    の┅∞ 

    ★~☆·☆。~*∴*~★*∴ *·∴~*★*∴*★~☆·☆。~*∴*~★
        """
    )





def Administrators():
    users = []  # 使用列表来存储所有用户信息
    with open("Administrators.txt", 'r', encoding='utf-8') as f:
        for line in f:
            user_data = json.loads(line.strip())  # 使用json模块安全地解析数据
            users.append(user_data)

    for i in range(4):
        name = input('请输入用户名：')
        passwd = input('请输入密码：')
        again_passwd = input('请再次输入密码：')

        if len(name.strip()) == 0:
            print('用户名不能为空，请重新输入。还可输入%d次' % (3 - i))
            continue

        if passwd != again_passwd:
            print('两次输入的密码不一致，请重新输入。还可输入%d次' % (3 - i))
            continue

        for user in users:
            if name == user['name']:
                print('用户名重复，请重新输入。还可输入%d次' % (3 - i))
                break
        else:  # 如果没有找到重复的用户名，则执行以下代码块
            new_user = {'name': name, 'passwd': passwd}
            users.append(new_user)
            with open("Administrators.txt", 'a', encoding='utf-8') as f:  # 以追加模式打开文件
                f.write(json.dumps(new_user) + '\n')  # 使用json模块安全地写入数据
            print('恭喜，注册成功')
            return  # 注册成功后直接退出函数，不再继续循环
    print('注册失败，已达到最大尝试次数')


# 管理员用户登录代码
def Administrators_log_in(shutdown):  # shutdown作为强制关闭词，用于输入次数过多强制退出
    with open("Administrators.txt", 'r+', encoding='utf-8') as f:
        getinformation = f.readlines()  # 将文件的所有行读入到getinformation中
        tempuserslist = []  # 创建一个临时列表用来存放所有的“字典”形式的字符串
        for count in range(3):  # 循环三遍，即三次输入错误的机会，三遍之后执行强制退出
            name = input('请输入用户名： ')
            password = input('请输入密码： ')
            for getit in getinformation:  # 把所有的字典循环一遍
                tempuserslist.append(getit)  # 循环了导入到列表里
            for gettemplistline in tempuserslist:  # 把列表循环一遍
                users = eval(gettemplistline)  # 依次导入到users中进行对比
                if (name != users['name'] or password != users['passwd']) and (
                        name != defaultuser['name'] or password != defaultuser['passwd']):
                    continue
                print('登录成功！')
                shutdown = 1  # 强制关闭词，为0时触发
                return shutdown  # 将强制关闭词的值返回到主函数中去
            if (name == users['name'] and password == users['passwd']) and (
                    name != defaultuser['name'] or password != defaultuser['passwd']):
                continue
            lost = 2 - count  # lost用来计算剩余可试错次数
            if count < 2:
                print('用户名或密码错误,还有{:}次机会'.format(lost))
            else:
                alertexit = '输入错误次数过多，程序终止'
                print(alertexit)
                shutdown = 0  # 同上，为0触发
                return shutdown

        f.close()

# ____________________★____________________


# 执行进度条
# Progress_bar()

#程序主循环：
while True:
    #首页：
    print(
"""
"……………·～·…οΟ○ の ○Οο…·～·…………… "
        
1.注册, 2.登录,3.管理员登录
""")

    choosefirst = input('请输入您选择的序号：')
    if choosefirst == '1':
        Administrators()
    elif choosefirst == '2':
        print()
    elif choosefirst == '3':
        print("管理员")
        Administrators_log_in(1)


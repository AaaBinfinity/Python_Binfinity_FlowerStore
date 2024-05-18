import time  # 引入设计进度条的相关库

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


def logup():
    with open("users.txt", 'r+', encoding='utf-8') as f:
        information = f.readlines()
        for it in information:
            it = it.strip()  # 清除换行符
            users = eval(it)  # f.read()读取的是字符串，用eval()将字符串转化为字典
        for i in range(4):
            name = input('请输入用户名：')
            passwd = input('请输入密码：')
            again_passwd = input('请再次输入密码：')
            if len(name.strip()) != 0 and name != users['name'] and len(passwd.strip()) != 0 and passwd == again_passwd:
                users = {'name': name, 'passwd': passwd}  # 往字典中插入新数据
                f.writelines(str(users) + '\n')  # 将字典写入文件
                print('恭喜，注册成功')
                f.close()
                break
            elif len(name.strip()) == 0:
                print('用户名不能为空，请重新输入。还可输入%d次' % (3 - i))
            elif name == users['name']:
                print('用户名重复，请重新输入。还可输入%d次' % (3 - i))
            elif len(passwd.strip()) == 0:
                print('密码不能为空，请重新输入。还可输入%d次' % (3 - i))
            elif again_passwd != passwd:
                print('两次输入的密码不一致，请重新输入。还可输入%d次' % (3 - i))

    # 用户登录代码
    def login(shutdown):  # shutdown作为强制关闭词，用于输入次数过多强制退出
        with open("users.txt", 'r+', encoding='utf-8') as f:
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
                    print('登录成功！')  # 上面的对比不只是对比文件新导入的，还有系统自带的管理员账户defaultuser
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


Progress_bar()

import time


# 初始化函数
def start():
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
    defaultuser = {'name': 'admin', 'passwd': 'passwd'}  # 设置默认管理员账户
    # 检索现有的花卉内容：
    try:  # try...except...else为一种书写格式，用以检测
        file = open('default.txt', "r", encoding='utf-8')
    except FileNotFoundError:
        print("暂时没有库存哦~")
    else:
        contents = file.readlines()  # 将文件中的所有行都读入contents中
        # 将默认学生信息导入至学生列表：
        student = []
        for content in contents:
            student.append(content[3:-1])
        tempsum = int(len(student) / lt)
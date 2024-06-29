# Binfinity_Flower_Store
这是俺滴python期末课设捏(大一)~

[TOC]



## 项目介绍

**Binfinity FlowerStore** 是一个基于 Python 编写的花卉商店销售和管理系统。

提供用户注册、登录、浏览花卉、购买花卉以及管理员管理花卉库存、用户信息等功能。

## 技术栈

- **编程语言**：Python
- **数据存储**：文本文件（如 `flowers.txt`储存花卉数据、`users.txt` 储存用户数据和 `Administrators.txt`储存管理员数据），未来计划迁移到数据库
- **依赖库**：`json`, `time` 等

## 主要功能

#### Tips:

​	程序内置了一个默认的用户：

```
		`用户名：Binfinity`

​		`密码：050328`
```



### 用户功能

- **注册与登录**：用户通过简单的步骤即可完成注册，包括输入用户名、密码以及确认密码，系统会在注册时验证用户名是否唯一，并提示用户密码是否一致，确保注册信息的准确性和安全性。
- **花卉浏览**：查看各类花卉的详细信息。
- **购买花卉**：支持购买功能，对仓库库存进行比对。
- **搜索花卉**：支持对花卉的搜索功能

### 管理员功能

- **管理员登录**：特定账户登录，用于管理系统。
- **查看库存**：实时查看花卉库存情况。
- **添加/更新/删除花卉**：全面管理花卉信息。
- **添加管理员**：管理员可以添加新的管理员账户到系统中，扩大管理团队的规模，提高系统的管理效率。同时，系统会对新添加的管理员账户进行验证和授权，确保只有合法的管理员才能登录系统。
- **搜索花卉**：支持对花卉的搜索功能

## 实现细节

1. **数据处理**：系统使用 Python 标准库中的 `json` 模块来处理用户信息和花卉信息的读取、解析和存储。通过读取文本文件中的数据，将其解析为 Python 字典对象，方便后续的处理和操作。
2. **用户验证**：在用户注册和登录过程中，系统会对用户名和密码进行验证，确保输入的有效性。对于管理员登录，系统还会检查是否为默认管理员账户，以提供额外的权限。
3. **菜单导航**：系统通过命令行界面提供菜单导航功能，用户可以根据提示输入相应的序号来选择所需的功能。不同的用户类型（普通用户和管理员）将看到不同的菜单选项。
4. **进度条实现**：进度条的实现依赖于 Python 的 `time` 库和循环结构。通过计算循环次数和当前时间戳，系统可以动态更新进度条的显示内容，模拟数据加载等过程的进度。

## 数据存储与读取

目前，我们使用文本文件存储花卉信息、用户信息和管理员信息。虽然这种方法简单易行，但未来我们计划迁移到数据库系统，以提高数据存储和访问的效率及安全性。

## 用户界面与交互

Binfinity FlowerStore 目前通过命令行界面（CLI）与用户交互。我们计划在未来开发图形用户界面（GUI），以提供更加友好和直观的用户体验。

## 如何贡献

我们欢迎任何形式的贡献，包括但不限于：

- 报告或修复 bug
- 提交功能请求或建议
- 编写或改进文档
- 添加新的功能或优化现有功能

请通过 GitHub 的 `Issues` 和 `Pull Requests` 来参与我的项目。

## 文件说明

- `flowers.txt`：存储花卉信息的文件。
- `users.txt`：存储用户信息的文件。
- `Administrators.txt`：存储管理员信息的文件。
- `Python_Binfinity_FlowerStore.py`：主程序文件，包含所有功能的实现。

## 环境要求

- Python 3.x
- 需要安装 `json` 模块（通常在标准库中已包含）

## 使用指南

1. **克隆仓库**
    ```bash
    git clone https://github.com/AaaBinfinity/Python_Binfinity_FlowerStore.git
    cd Binfinity-FlowerStore
    ```

2. **运行程序**
   
    ```bash
    python Python_Binfinity_FlowerStore.py
    ```
    
3. **功能选择**
    - 启动程序后，您将看到一个主菜单，可以选择注册、登录、管理员登录或退出程序。

## 示例

### 注册用户
启动程序后选择 `1` 进行注册：
```plaintext
1.注册, 2.登录, 3.管理员登录, 4.退出程序
请输入您选择的序号：1
请输入用户名：example_user
请输入密码：password123
请再次输入密码：password123
恭喜，注册成功
```

### 登录用户
注册成功后选择 `2` 进行登录：
```plaintext
1.注册, 2.登录, 3.管理员登录, 4.退出程序
请输入您选择的序号：2
请输入用户名：example_user
请输入密码：password123
登录成功！
```

### 查看花卉
登录成功后选择 `1` 查看所有花卉：
```plaintext
1.显示所有花卉    2.购买花卉    3.搜索花卉    4.退出登录
请输入您选择的序号：1
加载中--------- 50%[************->************]0.50s
所有花卉的详细信息如下：
花卉名称：玫瑰
花卉单价：10.0 元
花语：爱情
==============================
```

## 贡献

如果你有好的建议或者发现了BUG，欢迎提交 issues 和 pull requests。



感谢您使用 Binfinity FlowerStore 系统！如有任何问题，请随时联系我。

## 与我联系：

**Email：**

```bash
binfinity@qq.com
```
**Wechat：**

```bash
iabc-5305442
```

------

# About Code

> `以下是代码中每个功能和函数的详细介绍：`

## 全局初始化
```python
import time
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
# 内嵌默认账户（和管理员账户）
defaultuser = {'name': 'Binfinity', 'passwd': '050328'}

# 全局变量，用于存储花卉信息
flowers = []。
```

## 函数定义

### `load_flowers`

#### 功能
`load_flowers` 函数用于从指定的文件（默认为 `flowers.txt`）中加载花卉信息，并将这些信息存储到一个全局列表 `flowers` 中。该函数读取文件中的每一行数据，并将其解析为花卉的名称、价格、库存和含义。

#### 参数
- `filename`：文件名，默认为 `flowers.txt`。该文件应包含花卉的相关信息，每一行代表一种花卉，格式为：`name,price,stock,meaning`。

#### 全局变量
- `flowers`：全局列表，用于存储从文件中读取的花卉信息。每个花卉信息存储为一个字典，字典的键为 `name`、`price`、`stock` 和 `meaning`。

#### 实现步骤
1. **声明全局变量**：
   - 使用 `global flowers` 声明全局变量 `flowers`，确保在函数内部对 `flowers` 的操作影响到全局变量。

2. **文件操作**：
   - 使用 `with open(filename, 'r', encoding='utf-8') as file` 语句打开指定的文件，并确保文件会在操作结束后自动关闭。
   - 如果文件不存在，则抛出 `FileNotFoundError` 异常，并打印 `"未找到仓库"`。

3. **读取和解析文件内容**：
   - 逐行读取文件内容，并去除每行的首尾空白字符（使用 `strip()` 方法）。
   - 使用 `split(',')` 方法将每行数据按逗号分隔为不同部分，并存储到 `parts` 列表中。
   - 将解析出的数据存储到字典中，并将字典追加到 `flowers` 列表中。

4. **数据存储**：
   - 每个花卉的信息都存储在一个字典中，字典的键包括：
     - `name`：花卉名称，字符串类型。
     - `price`：花卉价格，浮点数类型。
     - `stock`：花卉库存，整数类型。
     - `meaning`：花卉含义，字符串类型。

#### 异常处理
- **FileNotFoundError**：当指定的文件未找到时，捕获该异常并打印错误信息 `"未找到仓库"`。

#### 示例
假设 `flowers.txt` 文件的内容如下：
```
Rose,10.5,50,Love
Tulip,7.3,30,Grace
Sunflower,5.0,20,Happiness
```

调用 `load_flowers()` 函数后，`flowers` 列表将包含以下数据：
```python
flowers = [
    {'name': 'Rose', 'price': 10.5, 'stock': 50, 'meaning': 'Love'},
    {'name': 'Tulip', 'price': 7.3, 'stock': 30, 'meaning': 'Grace'},
    {'name': 'Sunflower', 'price': 5.0, 'stock': 20, 'meaning': 'Happiness'}
]
```

#### 完整代码
```python
def load_flowers(filename='flowers.txt'):
    """从文件中加载花卉信息"""
    global flowers
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                flowers.append({
                    'name': parts[0],
                    'price': float(parts[1]),
                    'stock': int(parts[2]),
                    'meaning': parts[3]
                })
    except FileNotFoundError:
        print("未找到仓库")
```

该函数确保在文件存在的情况下正确加载花卉信息，并存储到全局列表 `flowers` 中以供后续使用。

### `save_flowers`

#### 功能
`save_flowers` 函数用于将全局列表 `flowers` 中的花卉信息保存到指定的文件（默认为 `flowers.txt`）中。该函数将每个花卉的信息格式化为字符串，并写入文件。

#### 参数
- `filename`：文件名，默认为 `flowers.txt`。保存花卉信息的文件名。

#### 全局变量
- `flowers`：全局列表，包含多个花卉信息的字典，每个字典包含 `name`、`price`、`stock` 和 `meaning` 键。

#### 实现步骤
1. **文件操作**：
   - 使用 `with open(filename, 'w', encoding='utf-8') as file` 语句以写入模式打开指定的文件，并确保文件会在操作结束后自动关闭。

2. **写入文件**：
   - 遍历全局列表 `flowers` 中的每个花卉字典。
   - 将每个花卉的信息格式化为 `name,price,stock,meaning` 的字符串格式，并写入文件中。
   - 每条花卉信息写入一行，行尾添加换行符 `\n`。

#### 示例
假设全局列表 `flowers` 的内容如下：
```python
flowers = [
    {'name': 'Rose', 'price': 10.5, 'stock': 50, 'meaning': 'Love'},
    {'name': 'Tulip', 'price': 7.3, 'stock': 30, 'meaning': 'Grace'},
    {'name': 'Sunflower', 'price': 5.0, 'stock': 20, 'meaning': 'Happiness'}
]
```

调用 `save_flowers()` 函数后，`flowers.txt` 文件将包含以下内容：
```
Rose,10.5,50,Love
Tulip,7.3,30,Grace
Sunflower,5.0,20,Happiness
```

#### 完整代码
```python
def save_flowers(filename='flowers.txt'):
    """将花卉信息保存到文件"""
    with open(filename, 'w', encoding='utf-8') as file:
        for flower in flowers:
            file.write(f"{flower['name']},{flower['price']},{flower['stock']},{flower['meaning']}\n")
```



### `buy_flower`

#### 功能
`buy_flower` 函数用于允许用户交互式地购买花卉。用户可以输入花卉名称和数量，系统会检查库存并更新库存信息。如果用户选择继续购买，可以继续操作；如果选择退出，则结束购买并保存数据。

#### 主要步骤
1. **无限循环**：
   - 使用 `while True` 创建无限循环，允许用户不断购买花卉，直到他们选择退出。

2. **获取用户输入**：
   - 提示用户输入想购买的花卉名称，如果输入为“退出”，则结束购买流程，保存数据并退出循环。
   - 提示用户输入想购买的数量，并尝试将其转换为整数。如果转换失败，提示用户重新输入数量。

3. **查找花卉并检查库存**：
   - 遍历全局列表 `flowers`，查找与用户输入名称匹配的花卉。
   - 如果找到花卉，检查库存是否足够：
     - 如果库存足够，计算总价格，减少库存并提示购买成功的信息。
     - 如果库存不足，提示库存不足的信息。
   - 如果未找到花卉，提示未找到该花卉。

4. **继续购买选项**：
   - 提示用户是否继续购买其他花卉，如果用户输入不是“是”，则结束购买流程，保存数据并退出循环。

5. **保存花卉信息**：
   - 在每次成功购买后或用户选择退出时，调用 `save_flowers` 函数保存最新的花卉信息到文件。

#### 参数
- 该函数没有参数，通过用户输入与全局变量 `flowers` 交互。

#### 全局变量
- `flowers`：全局列表，包含多个花卉信息的字典，每个字典包含 `name`、`price`、`stock` 和 `meaning` 键。

#### 示例
假设全局列表 `flowers` 的内容如下：
```python
flowers = [
    {'name': 'Rose', 'price': 10.5, 'stock': 50, 'meaning': 'Love'},
    {'name': 'Tulip', 'price': 7.3, 'stock': 30, 'meaning': 'Grace'},
    {'name': 'Sunflower', 'price': 5.0, 'stock': 20, 'meaning': 'Happiness'}
]
```

用户输入以下信息：
1. 输入花卉名称：“Rose”
2. 输入购买数量：“5”
3. 提示购买成功并继续购买。
4. 输入花卉名称：“Tulip”
5. 输入购买数量：“40”
6. 提示库存不足并继续购买。
7. 输入“退出”结束购买。

#### 完整代码
```python
def buy_flower():
    """购买花卉，并提供继续购买的选项"""

    while True:  # 无限循环，直到用户选择不再购买
        name = input("请输入您想购买的花卉名称（或输入'退出'结束购买）：")
        if name.lower() == '退出':  # 提供退出的选项
            print("感谢您的购买，欢迎下次光临！")
            save_flowers()  # 在退出前保存最新的花卉信息
            break  # 退出循环

        quantity_str = input("请输入您想购买的数量：")

        # 尝试将输入的数量转换为整数
        try:
            quantity = int(quantity_str)
        except ValueError:
            print("购买数量必须是一个整数，请重新输入。")
            continue  # 跳过当前循环的剩余部分，重新开始循环

        flower_found = False
        for flower in flowers:
            if flower['name'] == name:
                flower_found = True
                if flower['stock'] >= quantity:
                    total_price = flower['price'] * quantity
                    flower['stock'] -= quantity
                    print(f"购买成功！您购买了{quantity}朵{name}，总价为{total_price}元。")
                    save_flowers()  # 购买成功后立即保存最新的花卉信息
                    break  # 找到并购买后退出循环
                else:
                    print(f"库存不足，无法购买{quantity}朵{name}。")

        if not flower_found:
            print(f"未找到花卉：{name}")

        # 询问用户是否继续购买
        continue_purchase = input("您是否想继续购买其他花卉？（是/否）：").strip().lower()
        if continue_purchase != '是':
            print("感谢您的购买，欢迎下次光临！")
            save_flowers()  # 在退出前保存最新的花卉信息
            break  # 如果用户不想继续购买，则退出循环
```

#### 解释与关键点
- **输入与验证**：对用户输入的花卉名称和数量进行验证，确保操作的有效性。
- **库存检查与更新**：在购买成功后即时更新库存，并保存到文件中，保证数据的实时性。
- **用户交互**：提供友好的用户交互选项，允许用户根据需要继续购买或退出。

### ``view_stock`
#### 功能
`view_stock` 函数用于显示当前所有花卉的库存情况。它遍历全局列表 `flowers`，打印每种花卉的名称和库存数量。

#### 主要步骤
1. **遍历花卉列表**：
   - 使用 `for` 循环遍历全局列表 `flowers` 中的每个花卉字典。
   
2. **打印库存信息**：
   - 对于每个花卉字典，提取花卉的名称和库存数量，并打印出来。

#### 参数
- 该函数没有参数，通过全局变量 `flowers` 获取花卉信息。

#### 全局变量
- `flowers`：全局列表，包含多个花卉信息的字典，每个字典包含 `name`、`price`、`stock` 和 `meaning` 键。

#### 示例
假设全局列表 `flowers` 的内容如下：
```python
flowers = [
    {'name': 'Rose', 'price': 10.5, 'stock': 50, 'meaning': 'Love'},
    {'name': 'Tulip', 'price': 7.3, 'stock': 30, 'meaning': 'Grace'},
    {'name': 'Sunflower', 'price': 5.0, 'stock': 20, 'meaning': 'Happiness'}
]
```

调用 `view_stock()` 函数将打印以下信息：
```
花卉名称：Rose, 库存：50
花卉名称：Tulip, 库存：30
花卉名称：Sunflower, 库存：20
```

#### 完整代码
```python
def view_stock():
    """查看库存"""
    for flower in flowers:
        print(f"花卉名称：{flower['name']}, 库存：{flower['stock']}")
```

#### 解释与关键点
- **遍历列表**：使用 `for` 循环遍历全局变量 `flowers` 中的每个花卉字典。
- **提取信息**：从每个花卉字典中提取 `name` 和 `stock`，并格式化打印。
- **简单易用**：函数设计简洁，直接打印当前所有花卉的库存情况，方便用户查看。

### `add_flower`

#### 功能
`add_flower` 函数用于向全局列表 `flowers` 中添加新的花卉信息，并在添加后立即将更新后的列表保存到文件中。

#### 主要步骤
1. **添加花卉信息**：
   - 将新的花卉信息作为字典追加到全局列表 `flowers` 中。

2. **保存更新后的列表**：
   - 调用 `save_flowers` 函数，将更新后的 `flowers` 列表保存到文件中。

#### 参数
- `name`（字符串）：新花卉的名称。
- `price`（浮点数）：新花卉的价格。
- `stock`（整数）：新花卉的库存数量。
- `meaning`（字符串）：新花卉的含义。

#### 全局变量
- `flowers`：全局列表，包含多个花卉信息的字典，每个字典包含 `name`、`price`、`stock` 和 `meaning` 键。

#### 示例
假设全局列表 `flowers` 初始内容如下：
```python
flowers = [
    {'name': 'Rose', 'price': 10.5, 'stock': 50, 'meaning': 'Love'},
    {'name': 'Tulip', 'price': 7.3, 'stock': 30, 'meaning': 'Grace'}
]
```

调用 `add_flower('Sunflower', 5.0, 20, 'Happiness')` 后，`flowers` 列表将更新为：
```python
flowers = [
    {'name': 'Rose', 'price': 10.5, 'stock': 50, 'meaning': 'Love'},
    {'name': 'Tulip', 'price': 7.3, 'stock': 30, 'meaning': 'Grace'},
    {'name': 'Sunflower', 'price': 5.0, 'stock': 20, 'meaning': 'Happiness'}
]
```

#### 完整代码
```python
def add_flower(name, price, stock, meaning):
    """添加花卉"""
    flowers.append({
        'name': name,
        'price': price,
        'stock': stock,
        'meaning': meaning
    })
    save_flowers()
```

#### 解释与关键点
- **添加新花卉**：通过 `flowers.append` 方法，将包含新花卉信息的字典追加到全局列表 `flowers` 中。
- **保存列表**：调用 `save_flowers` 函数，将更新后的花卉信息保存到文件中，确保数据持久化。
- **易用性**：函数接受四个参数，便于用户添加新的花卉信息，并自动处理保存操作。

### `update_flower`

#### 功能
`update_flower` 函数允许用户更新指定花卉的信息（价格、库存和花语），并在更新后显示更新前后的信息对比。

#### 主要步骤
1. **查找花卉**：
   - 根据用户输入的花卉名称在全局列表 `flowers` 中查找对应的花卉信息。
   - 如果找到，保存旧的信息；如果未找到，提示用户并退出函数。

2. **获取用户更新信息**：
   - 询问用户是否需要更新价格、库存和花语，并根据用户的选择获取新的值。

3. **更新花卉信息**：
   - 根据用户提供的新信息，更新对应的花卉信息。

4. **保存更新后的列表**：
   - 调用 `save_flowers` 函数，将更新后的 `flowers` 列表保存到文件中。

5. **显示更新前后的信息比对**：
   - 打印更新前的信息和更新后的信息，供用户对比查看。

#### 参数
- 该函数不接受任何参数，所有的交互都是通过用户输入实现的。

#### 全局变量
- `flowers`：全局列表，包含多个花卉信息的字典，每个字典包含 `name`、`price`、`stock` 和 `meaning` 键。

#### 示例
假设全局列表 `flowers` 初始内容如下：
```python
flowers = [
    {'name': 'Rose', 'price': 10.5, 'stock': 50, 'meaning': 'Love'},
    {'name': 'Tulip', 'price': 7.3, 'stock': 30, 'meaning': 'Grace'}
]
```

用户输入要更新的花卉名称为 "Rose"，并选择更新价格为 12.0，库存为 45，不更新花语，函数执行后的输出如下：
```plaintext
花卉信息已更新：Rose
更新前信息：
名称：Rose, 单价：10.5, 库存：50, 花语：Love
更新后信息：
名称：Rose, 单价：12.0, 库存：45, 花语：Love
```

#### 完整代码
```python
def update_flower():
    """更新某个花卉信息，并在更新后进行比对确认"""
    global flowers
    flower_name = input("请输入要更新的花卉名称：")
    flower_found = False
    old_info = {}

    # 查找花卉并保存旧信息
    for flower in flowers:
        if flower['name'] == flower_name:
            flower_found = True
            old_info = flower.copy()  # 保存旧的花卉信息
            break

    # 如果没有找到花卉，则直接返回
    if not flower_found:
        print(f"未找到花卉：{flower_name}")
        return

    # 询问用户是否要更新价格、库存、花语
    new_price = None
    new_stock = None
    new_meaning = None

    if input("是否更新价格？(y/n) ").lower() == 'y':
        new_price = float(input("请输入新的价格："))

    if input("是否更新库存？(y/n) ").lower() == 'y':
        new_stock = int(input("请输入新的库存数量："))

    if input("是否更新花语？(y/n) ").lower() == 'y':
        new_meaning = input("请输入新的花语：")

    # 更新花卉信息
    for flower in flowers:
        if flower['name'] == flower_name:
            if new_price is not None:
                flower['price'] = new_price
            if new_stock is not None:
                flower['stock'] = new_stock
            if new_meaning is not None:
                flower['meaning'] = new_meaning
            break  # 找到并更新后退出循环

    # 保存更新后的花卉信息到文件
    save_flowers()

    # 显示更新前后的信息比对
    print(f"花卉信息已更新：{flower_name}")
    print("更新前信息：")
    print(f"名称：{old_info['name']}, 单价：{old_info['price']}, 库存：{old_info['stock']}, 花语：{old_info['meaning']}")
    
    # 获取更新后的花卉信息用于显示
    updated_flower = next((flower for flower in flowers if flower['name'] == flower_name), None)
    print("更新后信息：")
    print(f"名称：{updated_flower['name']}, 单价：{updated_flower['price']}, 库存：{updated_flower['stock']}, 花语：{updated_flower['meaning']}")
```

#### 解释与关键点
- **查找花卉**：通过遍历全局列表 `flowers` 查找用户指定的花卉，并保存旧的信息。
- **用户交互**：通过多次用户输入，确定需要更新的信息。
- **更新操作**：仅更新用户选择要更新的字段，其它字段保持不变。
- **保存列表**：调用 `save_flowers` 函数，将更新后的花卉信息保存到文件中，确保数据持久化。
- **信息比对**：在更新后显示更新前后的信息，方便用户确认修改。

### `delete_flower`

#### 功能
`delete_flower` 函数用于删除指定的花卉信息，并在删除后更新文件中的花卉数据。

#### 主要步骤
1. **查找花卉**：
   - 遍历全局列表 `flowers` 查找与用户提供的花卉名称匹配的花卉。
   
2. **确认删除**：
   - 找到匹配的花卉后，询问用户是否确认删除。
   
3. **执行删除**：
   - 如果用户确认删除，则从列表中删除该花卉，并调用 `save_flowers` 函数保存更新后的列表。
   
4. **未找到花卉**：
   - 如果在列表中未找到与用户提供的名称匹配的花卉，提示用户未找到。

#### 参数
- `name`：字符串类型，表示要删除的花卉名称。

#### 全局变量
- `flowers`：全局列表，包含多个花卉信息的字典，每个字典包含 `name`、`price`、`stock` 和 `meaning` 键。

#### 示例
假设全局列表 `flowers` 初始内容如下：
```python
flowers = [
    {'name': 'Rose', 'price': 10.5, 'stock': 50, 'meaning': 'Love'},
    {'name': 'Tulip', 'price': 7.3, 'stock': 30, 'meaning': 'Grace'}
]
```

用户输入要删除的花卉名称为 "Rose"，并确认删除，函数执行后的输出如下：
```plaintext
确认要删除Rose吗？(y/n): y
Rose已成功删除。
```

删除后，全局列表 `flowers` 的内容为：
```python
flowers = [
    {'name': 'Tulip', 'price': 7.3, 'stock': 30, 'meaning': 'Grace'}
]
```

#### 完整代码
```python
def delete_flower(name):
    """删除某个花卉"""
    for i, flower in enumerate(flowers):
        if flower['name'] == name:
            confirm = input(f"确认要删除{name}吗？(y/n): ")
            if confirm.lower() == 'y':
                del flowers[i]
                save_flowers()
                print(f"{name}已成功删除。")
                return
    print(f"未找到花卉：{name}")
```

#### 解释与关键点
- **查找花卉**：通过遍历全局列表 `flowers`，使用 `enumerate` 函数获取每个花卉及其索引，便于删除操作。
- **用户确认**：在删除花卉前，提示用户确认操作，防止误删除。
- **执行删除**：用户确认后，从列表中删除指定花卉，并调用 `save_flowers` 函数保存更新后的数据。
- **未找到花卉**：如果在列表中未找到与用户提供的名称匹配的花卉，提示用户未找到，确保用户了解操作结果。

### `search_flower`

#### 功能
`search_flower` 函数用于通过花卉名称或花语关键词搜索花卉，并显示匹配结果。

#### 主要步骤
1. **获取关键词**：
   - 请求用户输入要搜索的花卉名称或花语关键词。
   
2. **搜索匹配**：
   - 遍历全局列表 `flowers`，将名称或花语含有关键词的花卉信息添加到结果列表 `results` 中。
   
3. **显示结果**：
   - 如果找到匹配的花卉信息，则依次显示匹配结果中花卉的名称和花语。
   - 如果未找到匹配的花卉信息，则显示未找到的提示信息。

#### 参数
- 无参数，用户在函数内部输入要搜索的关键词。

#### 全局变量
- `flowers`：全局列表，包含多个花卉信息的字典，每个字典包含 `name`、`price`、`stock` 和 `meaning` 键。

#### 示例
假设全局列表 `flowers` 初始内容如下：
```python
flowers = [
    {'name': 'Rose', 'price': 10.5, 'stock': 50, 'meaning': 'Love'},
    {'name': 'Tulip', 'price': 7.3, 'stock': 30, 'meaning': 'Grace'}
]
```

用户输入要搜索的关键词为 "Love"，函数执行后的输出如下：
```plaintext
请输入要搜索的花卉名称或花语关键词：Love
找到与关键词'Love'匹配的花卉：
花卉名称：Rose, 花语：Love
```

用户输入要搜索的关键词为 "Sunflower"，函数执行后的输出如下：
```plaintext
请输入要搜索的花卉名称或花语关键词：Sunflower
未找到与关键词'Sunflower'匹配的花卉。
```

#### 完整代码
```python
def search_flower():
    """搜索某个花卉（通过花名或者花语），在函数体内请求用户输入关键词"""
    keyword = input("请输入要搜索的花卉名称或花语关键词：")
    results = []
    for flower in flowers:
        if keyword in flower['name'] or keyword in flower['meaning']:
            results.append(flower)
    if results:
        print(f"找到与关键词'{keyword}'匹配的花卉：")
        for flower in results:
            print(f"花卉名称：{flower['name']}, 花语：{flower['meaning']}")
    else:
        print(f"未找到与关键词'{keyword}'匹配的花卉。")
```

#### 解释与关键点
- **搜索匹配**：通过遍历全局列表 `flowers`，使用 `in` 运算符判断关键词是否包含在花卉的名称或花语中，实现匹配功能。
- **结果显示**：根据搜索结果 `results` 中是否有元素，选择性地显示匹配的花卉信息或未找到的提示信息，提高用户体验。

### `view_all_products`

#### 功能
`view_all_products` 函数用于查看所有花卉的详细信息，包括名称、单价和花语。

#### 主要步骤
1. **检查花卉信息**：
   - 检查全局列表 `flowers` 是否有花卉信息。

2. **显示详细信息**：
   - 如果存在花卉信息，则逐个显示每种花卉的名称、单价和花语。
   - 使用分隔线增强信息展示的清晰度。

#### 参数
- 无参数。

#### 全局变量
- `flowers`：全局列表，包含多个花卉信息的字典，每个字典包含 `name`、`price`、`stock` 和 `meaning` 键。

#### 示例
假设全局列表 `flowers` 包含以下花卉信息：
```python
flowers = [
    {'name': 'Rose', 'price': 10.5, 'stock': 50, 'meaning': 'Love'},
    {'name': 'Tulip', 'price': 7.3, 'stock': 30, 'meaning': 'Grace'}
]
```

执行 `view_all_products` 函数后的输出如下：
```plaintext
所有花卉的详细信息如下：
花卉名称：Rose
花卉单价：10.5 元
花语：Love
==============================
花卉名称：Tulip
花卉单价：7.3 元
花语：Grace
==============================
全部花卉展示完毕！
```

如果全局列表 `flowers` 为空，则输出如下：
```plaintext
仓库中没有花卉信息。
全部花卉展示完毕！
```

#### 完整代码
```python
def view_all_products():
    """查看所有商品（花卉）的详细信息"""
    if flowers:
        print("所有花卉的详细信息如下：")
        for flower in flowers:
            print(f"花卉名称：{flower['name']}")
            print(f"花卉单价：{flower['price']} 元")
            # print(f"花卉库存：{flower['stock']}")
            print(f"花语：{flower['meaning']}")
            print("=" * 30)  # 分隔线，使信息更清晰
    else:
        print("仓库中没有花卉信息。")
    print("全部花卉展示完毕！")
```

#### 解释与关键点
- **信息显示**：通过遍历全局列表 `flowers`，逐个显示每种花卉的名称、单价和花语，使用分隔线增强信息的可读性。
- **空仓库处理**：如果全局列表 `flowers` 为空，输出相应的提示信息，提醒用户仓库中没有花卉信息。

### `Progress_bar`

```python
# 蜜汁进度条：
def Progress_bar():
    scale = 25
    print('加载中'.center(scale // 2, '-'))
    for i in range(scale + 1):
        a = '****' * i
        b = '....' * (scale - i)
        c = (i / scale) * 100
        dur = time.perf_counter() - start
        print('\r{:^3.0f}%[{}->{}]{:.2f}s'.format(c, a, b, dur), end='')
        time.sleep(0.1)
    print('\n' + '加载完成'.center(scale // 2, '-'))
    print("=" * 30)  # 分隔线，使信息更清晰
def Progress_bar():
    scale = 25
    print('加载中'.center(scale // 2, '-'))
    for i in range(scale + 1):
        a = '****' * i
        b = '....' * (scale - i)
        c = (i / scale) * 100
        dur = time.perf_counter() - start
        print('\r{:^3.0f}%[{}->{}]{:.2f}s'.format(c, a, b, dur), end='')
        time.sleep(0.1)
    print('\n' + '加载完成'.center(scale // 2, '-'))
    print("=" * 30)
```
- **功能**：显示一个进度条，用于模拟加载过程。

### `Administrators_logup`
```python

# 注册管理员
def Administrators_logup():
    print("=" * 30)  # 分隔线，使信息更清晰
    Administrators = []  # 使用列表来存储所有用户信息
    with open("Administrators.txt", 'r', encoding='utf-8') as f:
        for line in f:
            user_data = json.loads(line.strip())  # 使用json模块安全地解析数据
            Administrators.append(user_data)

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

        for user in Administrators:
            if name == user['name']:
                print('用户名重复，请重新输入。还可输入%d次' % (3 - i))
                break
        else:  # 如果没有找到重复的用户名，则执行以下代码块
            new_user = {'name': name, 'passwd': passwd}
            Administrators.append(new_user)
            with open("Administrators.txt", 'a', encoding='utf-8') as f:  # 以追加模式打开文件
                f.write(json.dumps(new_user) + '\n')  # 使用json模块安全地写入数据
            print('恭喜，注册成功')
            return  # 注册成功后直接退出函数，不再继续循环
    print('注册失败，已达到最大尝试次数')

```
- **功能**：管理员注册功能，将注册信息保存到`Administrators.txt`文件。

### 函数目的和结构

`Administrators_login` 函数的目的是允许用户尝试以管理员身份登录。用户有三次机会输入正确的用户名和密码。如果连续三次输入错误，程序将终止并返回0。如果登录成功，函数返回1。

#### 代码流程解释

1. **打印分隔线**：`print("=" * 30)` 打印一个由30个等号组成的分隔线，使输出信息更加清晰。
2. **打开文件**：使用 `with open("Administrators.txt", 'r+', encoding='utf-8') as f:` 打开名为 "Administrators.txt" 的文件，该文件可能包含管理员的用户名和密码信息。这里使用了 `r+` 模式，意味着文件既可以读取也可以写入，但在这个函数中实际上并没有进行写入操作。
3. **读取文件内容**：`getinformation = f.readlines()` 读取文件的所有行，并将它们存储在 `getinformation` 列表中。
4. **初始化临时列表**：`tempAdministratorslist = []` 创建一个空列表，用于存储从文件中读取的管理员信息。但需要注意的是，这个列表在每次循环中都被重新填充，这是不必要的。
5. **登录尝试循环**：`for count in range(3):` 开始一个循环，允许用户最多尝试登录三次。
6. **用户输入**：通过 `input` 函数获取用户输入的用户名和密码。
7. **填充临时列表**：这个步骤实际上是不必要的，因为 `getinformation` 已经包含了所有需要的信息。但是，代码将 `getinformation` 中的每一行再次添加到 `tempAdministratorslist` 中。
8. **验证登录信息**：接下来的循环遍历 `tempAdministratorslist`，并使用 `eval` 函数（这里应该使用 `json.loads` 更安全）将每行字符串转换为字典格式。然后，它检查输入的用户名和密码是否与列表中的某个管理员信息匹配。这里存在一个逻辑问题，即它同时检查管理员信息和 `defaultuser` 的信息，这可能会导致混淆。
9. **登录成功或失败**：如果用户名和密码匹配，则打印“管理员登录成功！”并返回1。如果三次尝试都不成功，则打印“输入错误次数过多，程序终止”并返回0。
10. **关闭文件**：`f.close()` 试图关闭文件，但实际上这是不必要的，因为 `with` 语句会在代码块结束时自动关闭文件。

#### 函数定义

`Administrators_logup` 函数是一个用于注册管理员账号的函数。

#### 函数流程

1. **初始化**
   - 首先，函数打印了一个分隔线，使信息输出更加清晰。
   - 然后，初始化了一个空列表 `Administrators`，用于存储已有的用户信息。
2. **读取已有用户信息**
   - 函数通过打开名为 "Administrators.txt" 的文件，并逐行读取其中的内容。
   - 每一行都被视为一个JSON对象，通过 `json.loads` 方法解析成Python字典，并添加到 `Administrators` 列表中。
3. **用户注册流程**
   - 函数进入一个最多循环4次的for循环，用于给用户最多4次尝试注册的机会。
   - 在每次循环中，函数会提示用户输入用户名和密码，并要求再次输入密码以确认。
   - 接着，函数会进行一系列的检查：
     - 如果用户名为空，会提示用户重新输入。
     - 如果两次输入的密码不一致，也会提示用户重新输入。
     - 如果输入的用户名在 `Administrators` 列表中已存在，同样会提示用户重新输入。
   - 如果用户名和密码都符合要求，并且用户名是唯一的，那么函数会创建一个新的用户字典，包含用户名和密码，并将其添加到 `Administrators` 列表中。
   - 新用户的信息会以JSON格式追加到 "Administrators.txt" 文件的末尾。
   - 注册成功后，函数会打印一条成功消息，并立即返回，退出函数。
4. **注册失败**
   - 如果用户在4次尝试内都未能成功注册，函数会打印一条注册失败的消息。

#### 注意事项

- 函数使用了 `json` 模块来安全地解析和写入JSON数据。这是一个很好的做法，因为它能确保数据的完整性和一致性。
- 函数在检查用户名是否已存在时使用了 `for...else` 结构。这是一个Python中的特殊结构，当 `for` 循环正常结束时（即没有被 `break` 语句中断），`else` 块中的代码会被执行。在这里，`else` 块用于处理用户名不重复的情况。
- 函数在注册成功后立即返回，这是一个良好的设计，因为它避免了不必要的循环迭代。
- 函数通过文件I/O操作与持久化存储交互，这意味着即使程序关闭并重新启动，已注册的用户信息也不会丢失。

 

### `Administrators_login`
```python

# 管理员用户登录代码
def Administrators_login(shutdown):  # shutdown作为强制关闭词，用于输入次数过多强制退出
    print("=" * 30)  # 分隔线，使信息更清晰
    with open("Administrators.txt", 'r+', encoding='utf-8') as f:
        getinformation = f.readlines()  # 将文件的所有行读入到getinformation中
        tempAdministratorslist = []  # 创建一个临时列表用来存放所有的“字典”形式的字符串
        for count in range(3):  # 循环三遍，即三次输入错误的机会，三遍之后执行强制退出
            name = input('请输入用户名： ')
            password = input('请输入密码： ')
            for getit in getinformation:  # 把所有的字典循环一遍
                tempAdministratorslist.append(getit)  # 循环了导入到列表里
            for gettemplistline in tempAdministratorslist:  # 把列表循环一遍
                Administrators = eval(gettemplistline)  # 依次导入到Administrators中进行对比
                if (name != Administrators['name'] or password != Administrators['passwd']) and (
                        name != defaultuser['name'] or password != defaultuser['passwd']):
                    continue
                print('管理员登录成功！')
                shutdown = 1  # 强制关闭词，为0时触发
                return shutdown  # 将强制关闭词的值返回到主函数中去
            if (name == Administrators['name'] and password == Administrators['passwd']) and (
                    name != defaultuser['name'] or password != defaultuser['passwd']):
                continue
            lost = 2 - count  # lost用来计算剩余可试错次数
            if count < 2:
                print('用户名或密码错误,还有{:}次机会'.format(lost))
            else:
                alertexit = '输入错误次数过多，程序终止'
                print(alertexit)
                return 0

        f.close()

```
- **功能**：管理员登录功能，验证管理员账号和密码。

#### 函数目的和结构

`Administrators_login` 函数的目的是允许用户尝试以管理员身份登录。用户有三次机会输入正确的用户名和密码。如果连续三次输入错误，程序将终止并返回0。如果登录成功，函数返回1。

#### 代码流程解释

1. **打印分隔线**：`print("=" * 30)` 打印一个由30个等号组成的分隔线，使输出信息更加清晰。
2. **打开文件**：使用 `with open("Administrators.txt", 'r+', encoding='utf-8') as f:` 打开名为 "Administrators.txt" 的文件，该文件可能包含管理员的用户名和密码信息。这里使用了 `r+` 模式，意味着文件既可以读取也可以写入，但在这个函数中实际上并没有进行写入操作。
3. **读取文件内容**：`getinformation = f.readlines()` 读取文件的所有行，并将它们存储在 `getinformation` 列表中。
4. **初始化临时列表**：`tempAdministratorslist = []` 创建一个空列表，用于存储从文件中读取的管理员信息。但需要注意的是，这个列表在每次循环中都被重新填充，这是不必要的。
5. **登录尝试循环**：`for count in range(3):` 开始一个循环，允许用户最多尝试登录三次。
6. **用户输入**：通过 `input` 函数获取用户输入的用户名和密码。
7. **填充临时列表**：这个步骤实际上是不必要的，因为 `getinformation` 已经包含了所有需要的信息。但是，代码将 `getinformation` 中的每一行再次添加到 `tempAdministratorslist` 中。
8. **验证登录信息**：接下来的循环遍历 `tempAdministratorslist`，并使用 `eval` 函数（这里应该使用 `json.loads` 更安全）将每行字符串转换为字典格式。然后，它检查输入的用户名和密码是否与列表中的某个管理员信息匹配。这里存在一个逻辑问题，即它同时检查管理员信息和 `defaultuser` 的信息，这可能会导致混淆。
9. **登录成功或失败**：如果用户名和密码匹配，则打印“管理员登录成功！”并返回1。如果三次尝试都不成功，则打印“输入错误次数过多，程序终止”并返回0。
10. **关闭文件**：`f.close()` 试图关闭文件，但实际上这是不必要的，因为 `with` 语句会在代码块结束时自动关闭文件。

## 菜单选项

```python
def Users():
    while True:
        print(
            """
    ！！！=========！！==！====！！=消费者登录=！！=====！====！！=====！！！
          1.显示所有花卉    2.购买花卉      3.搜索花卉     4.退出登录 
        """
        )
        # 消费者选择
        choose = input('请输入您选择的序号：')
        if choose == "1":
            print("▂﹍▂﹍▂﹍查看所有花卉▂﹍▂﹍▂﹍▂﹍▂  ")

            # 执行进度条
            Progress_bar()
            view_all_products()
            print("=" * 30)  # 分隔线，使信息更清晰
        elif choose == "2":
            print("▂﹍▂﹍▂﹍购买花卉▂﹍▂﹍▂﹍▂﹍▂")

            # 执行进度条
            Progress_bar()
            buy_flower()
            print("=" * 30)  # 分隔线，使信息更清晰
        elif choose == "3":
            print("▂﹍▂﹍▂﹍搜索花卉▂﹍▂﹍▂﹍▂﹍▂")

            # 执行进度条
            Progress_bar()
            search_flower()
            print("=" * 30)  # 分隔线，使信息更清晰
        elif choose == "4":
            print("=" * 30)  # 分隔线，使信息更清晰
            if esc() == 1:
                break

        else:
            print()
            print("﹏﹋﹏﹋﹏﹋﹏﹋﹏﹋﹏﹋﹏﹋﹏﹋﹏ ※”  ")
            print("选择无效，请输入正确的序号")


```
- **功能**：用户菜单，提供查看库存、购买花卉、查看所有商品信息、搜索花卉、退出系统等功能选项。

```python
def Administrators():
    while True:
        print(
            """
    ！！！=============！！=====！！=========！！=管理员登录=！！===========！！=====！！=======================！！！    
    
    1. 查看库存   2. 添加花卉   3. 购买花卉     4. 更新花卉信息    5. 删除花卉   6.添加管理员   7.搜索花卉    8.退出程序           
            """
        )
        # 用户选择2
        choose2 = input('请输入您选择的序号：')
        if choose2 == '1':
            print("▂﹍▂﹍▂﹍查看库存▂﹍▂﹍▂﹍▂﹍▂  ")

            # 执行进度条
            Progress_bar()
            view_stock()
        elif choose2 == '2':
            print("▂﹍▂﹍▂﹍添加花卉▂﹍▂﹍▂﹍▂﹍▂ ")

            # 执行进度条
            Progress_bar()
            print("！！！=============！！=====！！======")
            name = input("请输入您想添加的花卉名称")
            print("！！！=============！！=====！！======")
            price = input("请输入您想添加的花卉单价")
            print("！！！=============！！=====！！======")
            stock = input("请输入您想添加的花卉库存")
            print("！！！=============！！=====！！======")
            meaning = input("请输入您想添加的花卉花语")
            print("！！！=============！！=====！！======")
            add_flower(name=name, price=price, stock=stock, meaning=meaning)
            print("完成添加！！")
            print("！！！=============！！=====！！======")
        elif choose2 == '3':
            print("▂﹍▂﹍▂﹍购买花卉▂﹍▂﹍▂﹍▂﹍▂")
            # 执行进度条
            Progress_bar()
            buy_flower()
            print("！！！=============！！=====！！======")
        elif choose2 == '4':
            print("▂﹍▂﹍▂﹍更新花卉▂﹍▂﹍▂﹍▂﹍▂ ")
            # 执行进度条
            Progress_bar()
            update_flower()
        elif choose2 == '5':
            print("▂﹍▂﹍▂﹍删除花卉▂﹍▂﹍▂﹍▂﹍▂ ")

            # 执行进度条
            Progress_bar()
            delete_flower(name=input("请输入您想要删除的花卉："))
        elif choose2 == '6':
            print("▂﹍▂﹍▂﹍添加管理员▂﹍▂﹍▂﹍▂﹍▂")
            # 执行进度条
            Progress_bar()
            Administrators_logup()
        elif choose2 == "7":
            print("▂﹍▂﹍▂﹍搜索花卉▂﹍▂﹍▂﹍▂﹍▂ ")

            # 执行进度条
            Progress_bar()
            search_flower()
        elif choose2 == "8":
            esc()
            return 1
        else:
            print()
            print("﹏﹋﹏﹋﹏﹋﹏﹋﹏﹋﹏﹋﹏﹋﹏﹋﹏ ※”  ")
            print("选择无效，请输入正确的序号")

```
- **功能**：管理员菜单，提供查看库存、添加花卉、更新花卉信息、删除花卉、查看所有商品信息、搜索花卉、退出系统等功能选项。

```python

def main():
    load_flowers()  # 加载花卉信息
    # 执行进度条
    Progress_bar()
    print(
        """
        ★~☆·☆。~*∴*~★*∴ *·∴~*★*∴*★~☆·☆。~*∴*~★
    
        の┅∞   欢迎来到 Binfinity FlowerStore    の┅∞ 
    
        ★~☆·☆。~*∴*~★*∴ *·∴~*★*∴*★~☆·☆。~*∴*~★
        """
    )
    # 程序主循环：


    while True:

        # 首页：
        print(
            """
    " ……………·～·…οΟ○ の ○Οο…·～·…………… "
    
    1.注册, 2.登录,3.管理员登录,4.退出程序
             """)
        # 用户选择1
        choosefirst = input('请输入您选择的序号：')
        if choosefirst == '1':
            print("▂﹍▂﹍▂﹍▂﹍▂﹍▂﹍▂﹍▂  ")

            logup()

            print(".*""*.*""*.*""*.*""**""*.*""**""*.*  ")

        elif choosefirst == '2':
            print("▂﹍▂﹍▂﹍▂﹍▂﹍▂﹍▂﹍▂  ")
            if login(1) == 0:
                break
            else:
                Users()
            print(".*""*.*""*.*""*.*""**""*.*""**""*.*  ")
        elif choosefirst == '3':
            if Administrators_login(1) == 0:
                break
            else:
                Administrators()

        elif choosefirst == '4':
            if esc() == 1:
                break
            else:
                print("程序继续运行")

        else:
            print("﹏﹋﹏﹋﹏﹋﹏﹋﹏﹋﹏﹋﹏﹋﹏﹋﹏ ※”  ")
            print("选择无效，请输入正确的序号")

```
- **功能**：主程序入口，提供用户登录、管理员登录、管理员注册、退出系统等功能选项。

  ### `Users`
  - **功能**：用户菜单，提供查看库存、购买花卉、查看所有商品信息、搜索花卉、退出系统等功能选项。
  - **主要功能**：
    - 显示用户菜单选项，包括查看所有花卉、购买花卉、搜索花卉和退出登录。
    - 根据用户选择执行相应的操作，比如调用 `Progress_bar()` 显示进度条，调用 `view_all_products()` 查看所有商品信息，调用 `buy_flower()` 购买花卉等。

  ### `Administrators`
  - **功能**：管理员菜单，提供查看库存、添加花卉、更新花卉信息、删除花卉、查看所有商品信息、搜索花卉、退出系统等功能选项。
  - **主要功能**：
    - 显示管理员菜单选项，包括查看库存、添加花卉、购买花卉、更新花卉信息、删除花卉、添加管理员、搜索花卉和退出程序。
    - 根据管理员选择执行相应的操作，比如调用 `Progress_bar()` 显示进度条，调用 `view_stock()` 查看库存，调用 `add_flower()` 添加花卉信息等。

  ### `main`
  - **功能**：主程序入口，提供用户注册、登录、管理员登录、管理员注册、退出系统等功能选项。
  - **主要功能**：
    - 显示主菜单选项，包括用户注册、登录、管理员登录、退出程序。
    - 根据用户选择执行相应的操作，比如调用 `logup()` 进行用户注册，调用 `login()` 进行用户登录，调用 `Administrators_login()` 进行管理员登录等。


### 运行主程序
```python
if __name__ == "__main__":
    main()
```
- **功能**：运行主程序，启动花卉销售系统。
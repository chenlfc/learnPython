# Python 编程快速上手 - 让繁琐工作自动化（学习笔记）

> 有关作者的帮助信息可以访问他的博客[http://inventwithpython.com/blog](http://inventwithpython.com/blog)

## 目录

[TOC]



## 第一部分 Python 编程基础

### 1.1 数学操作符

> 下表列出了Python的所有数学操作符，优先级从高到低

| 操作符 | 操作          | 例子  | 求值为 |
| ------ | ------------- | ----- | ------ |
| **     | 指数          | 2**3  | 8      |
| %      | 取模/取余数   | 22%8  | 6      |
| //     | 整除/商数取整 | 22//8 | 2      |
| /      | 除法          | 22/8  | 2.75   |
| *      | 乘法          | 3*5   | 15     |
| -      | 减法          | 5-2   | 3      |
| +      | 加法          | 2+2   | 4      |

* 一些基本的常用函数

  * `print()` 打印输出
  * `input()` 接受输入
  * `len()` 返回字符串长度

  * `str()` 转换为字符串
  * `int()` 转换为整数
  * `float()` 转换为浮点数

### 1.2 控制流

#### 1.2.1 比较操作符

| 操作符 | 含义     |
| ------ | -------- |
| ==     | 等于     |
| !=     | 不等于   |
| <      | 小于     |
| >      | 大于     |
| <=     | 小于等于 |
| >=     | 大于等于 |

#### 1.2.2 布尔操作符

* 3个布尔操作符（and、or和not）

  * and操作符的真值表

    | 表达式          | 求值为 |
    | --------------- | ------ |
    | True and True   | True   |
    | True and False  | False  |
    | False and True  | False  |
    | False and False | False  |

  * or操作符的真值表

    | 表达式         | 求值为 |
    | -------------- | ------ |
    | True or True   | True   |
    | True or False  | True   |
    | False or True  | True   |
    | False or False | False  |

  * not操作符的真值表

    | 表达式    | 求值为 |
    | --------- | ------ |
    | not True  | False  |
    | not False | True   |

#### 1.2.3 控制流语句

##### 1.2.3.1 if语句

> if语句

* if语句包含以下部分

  * if关键字

  * 条件(即求值为True或False的表达式)

  * 冒号

  * 在下一行开始，缩进的代码块(称为if子句)

    ```python
    if name == 'Alice':
        print('Hi, Alice.')
    ```

> else语句
>
> if子句后面有时候也可以跟着else语句。只有jif语句的条件为False时，else子句才会执行

* else语句中包含以下部分

  * else关键字

  * 冒号

  * 在下一行开始，缩进的代码块（称为else子句）

    ```python
    if name == 'Alice':
        print('Hi, Alice.')
    else
    	print('Hello, stranger.')
    ```

> elif语句

* elif语句中包含以下部分

  * elif关键字

  * 条件(即求值为True或False的表达式)

  * 冒号

  * 在下一行开始，缩进的代码块(称为elif子句)

    ```python
    if name == 'Alice':
        print('Hi, Alice.')
    elif age < 12:
        print('You are not Alice, kiddo.')
    ```


##### 1.2.3.2 while循环语句

> while循环语句
>
> 利用while语句，可以让一个代码块一遍又一遍的执行。只要while语句的条件为True，while子句中的代码就会执行

* while语句总是包含下面几部分

  * while关键字

  * 条件(求值为True或False的表达式)

  * 冒号

  * 从新行开始，缩进的代码块(称为while子句)

    ```python
    spam = 0
    while spam < 6:
        print('Hello, world.')
        spam = spam + 1
    ```

> break语句
>
> 有一个捷近，让执行提前跳出while语句。如果执行遇到break语句，就会马上退出while循环子句。

```python 
while True:
    print('Please type your name.')
    name = input()
    if name == 'your name':
        break
print('Thank you!')
```

> continue语句
>
> 如果程序执行遇到continue语句，就会马上跳回到循环开始处，重新对循环条件求值（这也是执行到大循环末尾时发生的事情）

```python
while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
	print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')
```

##### 1.2.3.3 for循环和range()函数

> 如果想让一个代码块执行固定次数，可以通过for循环语句和range()函数来实现

* for语句看起来像`for i in range(5):`这样，总包换以下部分

  * for关键字
  * 一个变量名
  * in关键字
  * 调用range()方法，最多传入3个参数
  * 冒号
  * 从下一行开始，缩进的代码块（称为for子句）

  ```python
  print('My name is')
  for i in range(6):
      print('Jimmy Five Times (' + str(i) + ')')
  ```

* range()的开始、停止和步长参数

  ```python
  for i in range(0, 10, 2):
      print(i)
  ```

  * 第一个参数是for循环变量开始的值
  * 第二个参数是上限
  * 第三个参数是步长

##### 1.2.3.4 导入模块

> 在开始使用一个模块中的函数前，必须用import语句导入该模块

* import语句包含以下部分

  * import关键字
  * 模块的名称
  * 可选的更多模块名称，之间用逗号隔开

  ```python
  import random
  for i in range(6):
      print(random.randint(1,10))
  ```

* from import语句

  * `from random import *`导入random模块中的所有函数
  * **使用完成的名称会让代码更可读，所以最好使用普通形式的import语句**

* 用sys.exit()提前结束程序

  * 要使用sys.exit()函数，必须先导入sys

  ```python
  import sys
  while True:
      print('Type exit to exit.')
      response = input()
      if respose == 'exit':
          sys.exit()
      print('You typed ' + response + '.')
  ```

### 1.3 函数

> 函数就像一个程序内的小程序

```python
def hello():
    print('Howdy!')
    print('Howdy!!!')
    print('Hello there.')
hello()
hello()
hello()
```

* def语句和参数 `def hello(name):`
* 返回值和return语句，return语句包含以下部分
  * return关键字
  * 函数应该返回的值或表达式
* None值
  * None表示没有值。None是NoneType数据类型的唯一值

> 如果需要在一个函数内修改全局变量，就是用global语句

```python
def spam():
    global eggs
    eggs = 'spam'
eggs = 'global'
spam()
print(eggs)
```

> 异常处理，错误可以使用try和except语句来处理

```python
def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')
```

### 1.4 列表

> “列表”是一个值，它包含多个字构成的序列。
>
> 术语“列表值”指的是列表本身（它做为一个值，可以保存在变量中，或传递给函数，像所有其他值一样），而不是指列表值之内的那些值。

* 列表值看起来像这样：`['cat','bat','rat','elephant']`
  * 列表用左方括号开始，右方括号结束，即[]。
  * 列表中的值也称为“表项”。表项用逗号分隔（就是说，他们是“逗号分隔的”）
#### 1.4.1 用下表取得列表中的单个值
* 列表中的第一个值的下标是0，第二个值的下表是1，以此类推
* 负数下标：整数值-1指的是列表中的最后一个下标，-2指的是列表中倒数第二个下标，以此类推
#### 1.4.2 利用切片取得子列表
* 就像下标可以取得列表中的单个值一样，“切片”可以从列表中取得多个值，结果是一个新列表
* spam[1:4]是一个列表和切片
#### 1.4.3 用len()取得列表的长度
* 用下标改变列表中的值
* 列表连接和列表复制
  * +操作符可以连接两个列表
  * *操作符可以用于一个列表和一个整数，实现列表的复制
* 用del语句从列表中删除值

#### 1.4.4 使用列表

```python
catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) + 
         ' (or enter nothint to stop.):')
   	name = input()
    if name == '':
        break
    catNames = catNames + [name] # list concatenation
print('The cat names are:')
for name in catNames:
    print(' ' + name)
```

#### 1.4.5 一个常见的Python技巧
> 在for循环中使用`range(len(someList))`，迭代列表的每一个下标

#### 1.4.6 in和not in操作符

> 利用in和not in操作符，可以确定一个值是否在列表中

* in和not in用在表达式中，连接两个值

  * 一个要在列表中查找的值
  * 以及待查找的列表

  ```python
  >>> 'howdy' in ['hello', 'hi', 'howdy', 'heyas']
  True
  >>> spam = ['hello', 'hi', 'howdy', 'heyas']
  >>> 'cat' in spam
  False
  >>> 'howdy' not in spam
  False
  >>> 'cat' not in spam
  True
  ```

  ```python
  myPets = ['Zophie', 'Pooka', 'Fat-tail']
  print('Enter a pet name:')
  name = input()
  if name not in myPets:  # 检查myPets列表中是否包含输入的名字
      print('I do not have a pet named ' + name)
  else:
      print(name + ' is my pet.')
  ```

#### 1.4.7 多重赋值技巧

> 多重赋值技巧是一种快捷方式，让你在一行代码中，用列表中的值为多个变量赋值

```python
cat = ['fat', 'black', 'loud']
size, color, disposition = cat
```

* 变量的数目和列表的长度必须严格相等，否则Python将给出ValueError

### 1.5 增强的赋值操作

> 增强的赋值操作符

| 增强的赋值语句 | 等价的赋值语句  |
| -------------- | --------------- |
| spam += 1      | spam = spam + 1 |
| spam -= 1      | spam = spam - 1 |
| spam *= 1      | spam = spam * 1 |
| spam /= 1      | spam = spam / 1 |
| spam %= 1      | spam = spam % 1 |

### 1.6 方法

> 方法和函数是一回事，只是它是调用在一个值上。
>
> 例如，如果有一个列表存储在spam中，你可以在这个列表上调用index()列表方法，就像`spam.index('hello')` 一样。

#### 1.6.1 用index()方法在列表中查找值

* 列表值有一个index()方法，可以传入一个值，如果该值存在于列表中，就返回它的下标
* 如果该值不在列表中，Python就报ValueError
* 如果列表中存在重复的值，它就返回第一次出现的下标

#### 1.6.2 用append()和insert()方法在列表中添加值

> 要在列表中添加新值，就使用append()和insert()方法

* append()方法调用，将参数添加到列表末尾
* insert()方法调用，第一个参数是新值的下标，第二个参数是要插入的新值

#### 1.6.3 用remove()方法从列表中删除值

> 给remove()方法传入一个值，他将从被调用的列表中删除

* 试图删除不存在的值，将导致ValueError错误

#### 1.6.4 用sort()方法将列表的值排序

> 数值的列表或字符串的列表，能用sort()方法排序

* 也可以指定reverse关键字参数为True，让sort()按逆序排序`spam.sort(reverse=True)`
* 使用sort()方法，应该注意3件事
  * 不要写出 `spam=spam.sort()` 这样的代码，试图记录返回值
  * 不能对既有数字又有字符串值的列表排序，Python不知道如何比较它们，键返回TypeError错误
  * sort()方法对字符串排序时，使用“ASCII字符顺序”，而不是世纪的字典顺序
  * **如果要按照普通的字典顺序来排序，就在sort()方法调用时，将关键字参数key设置为str.lower**

### 1.7 类似列表的类型：字符串和元组

#### 1.7.1 可变和不可变数据类型

> 列表和字符串在一个重要的方面是不同的。

* 列表是“可变的”数据类型，它的值可以添加、删除或改变
* 字符串是“不可变的”数据类型，它不能被更改。尝试对字符串中的一个字符重新赋值，将导致TypeError错误。

#### 1.7.2 元组数据类型

> 除了两个方面，“元组”数据类型几乎与列表数据类型一样

* 首先，元组输入时用圆括号()，而不是用方括号[]
* 其次，元组像字符串一样，是不可变的。元组不能让它们的值被修改、添加或删除。

#### 1.7.3 用list()和tuple()函数来转换类型

> 函数list()和tuple()将返回传递给它们的值的列表和元组版本

#### 1.7.4 copy模块的copy()和deepcopy()函数

> 在处理列表和字典时，尽管传递引用常常是最方便的方法，但如果不希望函数变动影响原来的列表或字典，可以使用Python提供的名为copy的模块，其中包含copy()和deepcopy()函数

* `copy.copy()`可以用来复制列表或字典这样的可变值，而不只是复制引用

  ```python
  >>> import copy
  >>> spam = ['A', 'B', 'C', 'D']
  >>> cheese = copy.copy(spam)
  >>> cheese[1] = 42
  >>> spam
  ['A', 'B', 'C', 'D']
  >>> cheese
  ['A', 42, 'C', 'D']
  ```

* `copy.deepcopy()`可以复制列表中包含的列表，`deepcopy()`函数将同时复制他们内部的列表

### 1.8 字典和结构化数据

> 像列表一样，“字典”是许多值的集合。但不像列表的下标，字典的索引可以使用许多不同数据类型，不只是整数。字典的索引被称为“键”，键及其关联的值称为“键-值”对。

* 在代码中，字典输入时带花括号{}

```python
>>> myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
>>> myCat['size']
'fat'
>>> 'My cat has ' + myCat['color'] + ' fur.'
'My cat has gray fur.'
```

#### 1.8.1 keys()、values()和items()方法

> 有3个字典方法，它们将返回类似列表的值，分别对应于字典的键、值和键-值对：keys()、values()和items()

* 这些方法返回的值不是真正的列表，他们不能被修改。但这些数据类型(分别是dict_keys、dict_values和dict_items)可以用于for循环
* 如果希望通过这些方法得到一个真正的列表，就把类似列表的返回值传递给list函数。

```python
>>> spam = {'color': 'red', 'age': 42}
>>> spam.keys()
dict_keys(['color', 'age'])
>>> list(spam.keys())
['color', 'age']
```

#### 1.8.2 检查字典中是否存在键或值

> 可以使用`in`和`not in`操作符检查字典中的`keys()`和`values()`方法返回的列表中是否存在

#### 1.8.3 get()方法

> 字典有一个get()方法，它有两个参数：要取得其值的键，以及如果改键不存在时，返回的备用值。

#### 1.8.4 setdefault()方法

> 常常需要为字典中某个键设置一个默认值，当该键没有任何值时使用它。

```python
>>> spam = {'name': 'Pooka', 'age': 5}
>>> spam.setdefault('color', 'black')
'black'
>>> spam
{'color': 'black', 'age': 5, 'name': 'Pooka'}
>>> spam.setdefault('color', 'white')
'black'
>>> spam
{'color': 'black', 'age': 5, 'name': 'Pooka'}
```

#### 1.8.5 漂亮打印

> 如果程序中导入pprint模块，就可以使用pprint()和pformat()函数，它们将“漂亮打印”一个字典的字。

```python
import pprint
message = 'It was a bright cold day in April, and the colocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
    
pprint.pprint(count)
```

* 如果字典本身包含嵌套的列表或字典，pprint.pprint()函数就特别有用
* 如果希望得到漂亮打印的文本作为字符串，而不是显示在屏幕上，那就调用pprint.pformat()。下面两行代码是等价的：

```python
pprint.pprint(someDictonaryValue)
print(pprint.pformat(someDictonaryValue))
```

### 1.9 字符串操作


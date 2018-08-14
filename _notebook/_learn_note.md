# 学习Python过程中的一些记录笔记

> ## 字符串操作相关

* ### 修改字符串的大小写

  ```python
  str.title() #将字符串输出为首字母大写
  str.upper()、str.lower() #将字符串输出为全大写或全小写
  ```

* ### 合并（拼接）字符串
  * 使用加符号+连接2个字符串
  * 删除空白
    ```python
    str.rstrip()  # 删除右侧空白
    str.strip()   # 删除头尾处所有空白
    ```

> ## 一些关于图表库matplotlib的问题与学习内容

* **关于matplotlib的用法可以去** [查看各种图表的生成代码](https://matplotlib.org/gallery/)
* **要了解pylot中所有的颜色映射**

  * 访问 [https://matplotlib.org/](https://matplotlib.org/)
  * 单击 Examples
  * 滚动到 Color Examples
  * 再单击 colormaps_reference

> ## 一些关于Pygal的问题与学习内容

* 要了解使用Pygal可创建什么样的图表，可以访问[http://www.pygal.org/](http://www.pygal.org/)并依次点击
  * Documentation
  * Chart types

> ## 数据可视化
>
> 下载数据
>
> 用Python模块csv来处理以CSV格式存储的书记及用模块json来处理以JSON格式存储的数据
>
> 可以去[下载](https://nostarch.com/pythoncrashcourse/)本书的配套资源

* ### CSV文件格式
  * 一系列以逗号分隔的值的文本文件，内容格式如下
    ```python
    2014-1-5,61,44,26,18,7,-1,56,30,9,30.34,30.27,30.15,,,,10,4,,0.00,0,,195
    ```
  * 天气数据从[http://www.wunderground.com/history/](http://www.wunderground.com/history/)下载

* ## 模块 datetime
  * 将字符串'2014-7-1'转换为一个表示相应时间的对象

      ```python
      # 导入时间模块
      >>> from datetime import datetime
      # 调用方法将字符串转换为时间对象
      >>> first_date = datetime.striptime('2014-7-1', '%Y-%m-%d')
      # 打印输出时间对象内容
      >>> print(first_date)
      2014-07-01 00:00:00
      ```

  * `strptime()`可接受的各种实参，如下表

      | 实参  | 含义                            |
      | :---: | :------------------------------ |
      | %A    | 星期的名称，如Monday            |
      | %B    | 月份名，如January               |
      | %m    | 用数字表示的月份（01~12）       |
      | %d    | 用数字表示月份中的一天（01~31） |
      | %Y    | 四位的年份，如2015              |
      | %y    | 两位的年份，如15                |
      | %H    | 24小时制的小时数（00~23）       |
      | %I    | 12小时制的小时数（01~12）       |
      | %p    | am或pm                          |
      | %M    | 分钟数（00~59）                 |
      | %s    | 秒数（00~61）                   |

* ### JSON文件格式
  * 下载世界人口数据从[http://data.okfn.org/](http://data.okfn.org/)下载
  * 输出json格式文件时，中文乱码时可以加上参数，代码段如下

    ```python
    # encoding='utf-8'用于打开中文时不出现乱码
    with open(json_filename, 'w', encoding='utf-8') as f:
        # 参数ensure_ascii=False使输出中文时不出现乱码
        json.dump(iso_codes, f, ensure_ascii=False)
    ```

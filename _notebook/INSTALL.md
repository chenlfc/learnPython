# 关于一些Python相关插件集合的升级与安装过程遇到的问题的汇总

> ## 关于更换pip配置的方法

* pip源配置文件可以放置的位置如下

  ```powershell
  Linux/Unix:
  /etc/pip.conf
  ~/.pip/pip.conf
  ~/.config/pip/pip.conf

  Mac OSX:
  ~/Library/Application Support/pip/pip.conf
  ~/.pip/pip.conf
  /Library/Application Support/pip/pip.conf

  Windows:
  %APPDATA%\pip\pip.ini
  %HOME%\pip\pip.ini
  C:\Documents and Settings\All Users\Application Data\PyPA\pip\pip.conf (Windows XP)
  C:\ProgramData\PyPA\pip\pip.conf (Windows 7及以后)
  ```

* 如果没有pip目录或者pip.ini文件，可以新建一个。然后在里面输入以下内容并保存。其中的注释要去掉

  ```powershell
  [global]

  index-url = http://pypi.douban.com/simple #豆瓣源，可以换成其他的源

  trusted-host = pypi.douban.com            #添加豆瓣源为可信主机，要不然可能报错

  disable-pip-version-check = true
  #取消pip版本检查，排除每次都报最新的pip

  timeout = 120
  ```

* 国内好用的几个pip镜像源如下

  ```powershell
  阿里云 http://mirrors.aliyun.com/pypi/simple/

  中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/

  豆瓣(douban) http://pypi.douban.com/simple/

  清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/

  中国科学技术大学 http://pypi.mirrors.ustc.edu.cn/simple/
  ```

> ## 关于安装预览版本的方法说明

* 在 pip install pylint 后加上参数 astroid --pre 用于安装预览版本 -U --user

  ```powershell
  pip install pylint astroid --pre -U --user
  ```

> ## 升级pip
> **首先下载最新版的pip**

* 可以先使用

  ```powershell
  python -m pip install --upgrade pip astroid --pre -U --user
  #安装失败后，从提示的下载链接地址下载最新版的pip
  ```

* 进入E:\Python 3\

  ```powershell
  python -m pip install --upgrade
  pip-18.0-py2.py3-none-any.whl -U --user
  ```

> ## 安装Pygame

* 这是预览版

  ```powershell
  pip install pygame astroid --pre -U --user
  pip install pygame-1.9.4-cp37-cp37m-win_amd64.whl --user
  pip install pygame-1.9.4-cp37-cp37m-win32.whl --user
  ```

> ## 安装最新的Pylint

* 下载并安装相对应的版本，如果无法自动下载，可以复制安装过程中未成功下载的链接，使用迅雷等下载后进行安装

  ```powershell
  pip install pylint-2.0.1-py3-none-any.whl --user
  pip install colorama-0.3.9-py2.py3-none-any.whl --user
  pip install lazy-object-proxy-1.3.1.tar.gz --user
  pip install six-1.11.0-py2.py3-none-any.whl --user
  ```

> ## 安装matplotlib，用于数据可视化的包

* 关于matplotlib的用法可以去[查看各种图表的生成代码](https://matplotlib.org/gallery/)
* 首先要安装的包

  ```powershell
  pip install --user python_dateutil-2.7.3-py2.py3-none-any.whl
  pip install --user numpy-1.15.0-cp37-none-win_amd64.whl
  pip install --user cycler-0.10.0-py2.py3-none-any.whl
  pip install --user pytz-2018.5-py2.py3-none-any.whl
  pip install --user kiwisolver-1.0.1-cp37-none-win_amd64.whl

  pip install --user matplotlib-2.2.2-cp37-cp37m-win32.whl # 32位版的安装包
  pip install --user matplotlib-2.2.2-cp37-cp37m-win_amd64.whl # 64位版的安装包
  ```

> ## 安装Python的可视化包Pygal
> **我们可以使用它是用来生成可缩放的矢量图形文件**
* 安装 Pygal

  ```powershell
  pip install --user pygal
  # 无法自动安装时，按提示链接用迅雷下载文件后再进行安装
  pip install pygal-2.4.0-py2.py3-none-any.whl --user
  ```

* 要了解使用Pygal可创建什么样的图表，可以访问[http://www.pygal.org/](http://www.pygal.org/)并依次点击
  * Documentation
  * Chart types

> ## 安装 pygal_maps_world
> **我们将使用它来返回国别码，代替原来的 pygal.i18n**
* 安装

  ```powershell
  pip install --user pygal_maps_world
  # 安装不成功时，从提示的链接下载后再进行安装
  pip install --user pygal_maps_world-1.0.2.tar.gz
  ```

> ## 安装rope
> **用于在VS Code中批量修改变量名的插件**
* 安装rope

  ```powershell
  pip install rope-0.10.7.tar.gz --user
  ```

> ## 安装requests
> **用于向网站请求信息以及检查返回的相应**
* 安装requests

  ```powershell
  pip install --user requests
  ```

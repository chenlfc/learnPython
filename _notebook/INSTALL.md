# 关于一些Python相关插件集合的升级与安装过程遇到的问题的汇总

> ## 关于安装预览版本的方法说明

* 在 pip install pylint 后加上参数 astroid --pre 用于安装预览版本 -U --user

  ```bat
  pip install pylint astroid --pre -U --user
  ```

> ## 升级pip
> **首先下载最新版的pip**

* 可以先使用

  ```bat
  python -m pip install --upgrade pip astroid --pre -U --user
  #安装失败后，从提示的下载链接地址下载最新版的pip
  ```

* 进入E:\Python 3\

  ```bat
  python -m pip install --upgrade
  pip-18.0-py2.py3-none-any.whl -U --user
  ```

> ## 安装Pygame

* 这是预览版

  ```bat
  pip install pygame astroid --pre -U --user
  pip install pygame-1.9.4-cp37-cp37m-win_amd64.whl --user
  pip install pygame-1.9.4-cp37-cp37m-win32.whl --user
  ```

> ## 安装最新的Pylint

* 下载并安装相对应的版本，如果无法自动下载，可以复制安装过程中未成功下载的链接，使用迅雷等下载后进行安装

  ```bat
  pip install pylint-2.0.1-py3-none-any.whl --user
  pip install colorama-0.3.9-py2.py3-none-any.whl --user
  pip install lazy-object-proxy-1.3.1.tar.gz --user
  pip install six-1.11.0-py2.py3-none-any.whl --user
  ```

> ## 安装matplotlib，用于数据可视化的包

* 关于matplotlib的用法可以去[查看各种图表的生成代码](https://matplotlib.org/gallery/)
* 首先要安装的包

  ```bat
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

  ```bat
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

  ```bat
  pip install --user pygal_maps_world
  # 安装不成功时，从提示的链接下载后再进行安装
  pip install --user pygal_maps_world-1.0.2.tar.gz
  ```

> ## 安装rope
> **用于在VS Code中批量修改变量名的插件**
* 安装rope

  ```bat
  pip install rope-0.10.7.tar.gz --user
  ```

> ## 安装requests
> **用于向网站请求信息以及检查返回的相应**
* 安装requests

  ```bat
  pip install --user requests
  ```

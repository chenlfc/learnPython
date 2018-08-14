# 利用Django开发Web应用程序

> ## Python提供了一组开发Web应用程序的卓越工具
> **在这个项目里学习了如何使用这个工具开发一个名为“学习笔记”的项目，这是一个在线日志系统**

* 在这里学习了如何使用[Django](http://djangoproject.com/)进行开发
* **Django** 是一个Web框架，一套用于帮助开发交互式网站的工具

> ## 建立项目

* ### 制定规范
  * **完整的规范详细说明了项目的目标，阐述了项目的功能，并讨论了项目的外观和用户界面。与任何良好的项目规划和商业计划书一样，规范应突出重点，帮助避免项目偏离轨道。**
  * 这里不会指定完整的项目规划，而只列出一些明确的目标，以突出开发的重点。
    * *我们要编写一个名为“学习笔记”的Web应用程序，让用户能够记录感兴趣的主题，并在学习每个主题的过程中添加日志条目。“学习笔记”的主页对这个网站进行描述，并邀请用户注册或登录。用户登录后，就可以创建新主题、添加新条目以及阅读既有的条目。*

* ### 建立虚拟环境
  * 为项目建立一个新目录，在终端中切换到这个目录，并创建一个虚拟环境。
  * 用以下命令创建一个名为 **ll_env** 的虚拟环境
    ```powershell
    python -m venv ll_env
    ```
  * 如果不能正常使用模块，可以安装virtualenv包
    ```powershell
    pip install --user virtualenv
    ```
* ### 激活虚拟环境
  * 建立虚拟环境后，休要用以下命令激活它
    ```powershell
    使用命令 ll_env\Scripts\activate 来激活这个虚拟环境
    要停止使用虚拟环境，可以执行命令 deactivate
    ```
* ### 安装Django
  * 创建并激活了虚拟环境后，就可以安装Django了
  * 激活虚拟环境后，执行一下命令
    ```powershell
    pip install Django
    ```
* ### 在Django中创建项目
  * 在依然处于活动的虚拟环境下执行如下命令来新建一个项目
    ```powershell
    django-admin.exe startproject learning_log .
    ```
  * 新建一个名为learning_log的项目,这个命令最后的句点让新项目使用合适的目录结构，这样开发完成后可轻松地将应用程序部署到服务器
  * 千万别忘了这个【 **句点** 】，否则部署时会遭遇一些配置问题。如果忘了，就将创建的文件和文件夹删除(ll_env除外)，再重新运行这个命令
    ```powershell
    # 上一条Django语句创建了如下文件内容，如漏了句点就需删除它们
    manage.py     # 这是一个简单的程序，它接受命令并将其交给Django的相关部分去运行
    learning_log  # 文件夹
      settings.py # 指定Django如何与我们的系统交互以及如何管理项目
      urls.py     # 告诉Django应创建哪些网页来响应浏览器请求
      wsgi.py     # 帮助Django提供它创建的文件
                  # 它是web server gateway interface(Web服务器网关接口)的首字母缩写
    ```
* ### 创建数据库
  * Django将大部分与项目相关的信息都存储在数据库中，因此我们需要创建一个供Django使用的数据库
  * 在处于活动虚拟环境中执行下面命令
    ```powershell
    python manage.py migrate
    # 以下是输出的信息
    # 第一二行Django指出它将创建必要的数据库表
    # 用于存储我们将在这个项目中使用的信息
    # 再确保数据库结构与当前代码匹配
    Operations to perform:
      Apply all migrations: admin, auth, contenttypes, sessions
    Running migrations:
      Applying contenttypes.0001_initial... OK
      --snip--
      Applying auth.0009_alter_user_last_name_max_length... OK
      Applying sessions.0001_initial... OK
    ```
  * 在目录下Django有创建了一个文件
  * SQLite是一种使用单个文件的数据库，是编写简单应用程序的理想选择
    ```powershell
    db.sqlite3
    ```
  * **查看项目**
  * 下面来核实Django是否正确地创建了项目。为此，可执行命令runserver，如下所示：
    ```powershell
    python manage.py runserver
    # 下面是输出信息
    Performing system checks...

    # 这里Django通过检查确认正确地创建了项目
    System check identified no issues (0 silenced).
    August 14, 2018 - 11:19:49
    # 这里指出了使用地Django地版本以及当前使用的设置文件地名称
    Django version 2.1, using settings 'learning_log.settings'
    # 这里指出了项目的URL
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CTRL-BREAK.
    ```
  * **如果出现错误消息 “That port is already in use” (指定端口已被占用)，请执行如下命令，让Django使用另一个端口
    ```powershell
    python manage.py runserver 8001 # 端口号可以一直加大尝试，知道能够使用为止
    ```
* ### 创建应用程序
  * Django项目由一系列应用程序组成，它们协同工作，让项目成为一个整体。
  * **在运行着runserver的终端窗口外**，再打开一个终端窗口
  * 并切换到 **manage.py** 所在目录。激活虚拟环境，再执行命令startapp
    ```powershell
    ll_env/scripts/activate
    python manage.py startapp learning_logs

    learning_logs\models.py # 这个文件将用来定义要在应用程序中管理的数据
    ```
  * 定义模型 **models.py**
    * 我们创建了一个名为 **Topic** 的类，它继承了Model - Django中一个定义了模型基本功能的类。
    * **要获悉可在模型中使用的各种字段，请参阅[Django Model Field Reference（Django模型字段参考）](https://docs.djangoproject.com/en/2.1/ref/models/fields/)**
  * 激活模型 **settings.py**
    * 要使用模型，必须让Django将应用程序包含到项目中。
      ```python
      INSTALLED_APPS = [
          --snip--
          'django.contrib.staticfiles',

          # 我的应用程序
          'learning_logs',
      ]
      ```
    * 通过将应用程序编组，在项目不断增大时有助于对应用程序进行跟踪。
    * 以上新建了一个名为 **我的应用程序** 的片段，目前它只包含应用程序 **learning_logs**
  * **接下来让Django修改数据库，使其能够存储与模型Topic相关的信息。**
    * 为此我们需要在终端窗口中执行下面的命令
      ```powershell
      python manage.py makemigrations learning_logs
      # 输出如下内容
      Migrations for 'learning_logs':
        learning_logs\migrations\0001_initial.py
          - Create model Topic
      ```
    * makemigrations让Django确定该如何修改数据库，输出表明了Django创建了一个名为 **0001_initial.py**的迁移文件，这个文件将在数据库中为模型Topic创建一个表
    * 接下去需要应用这种迁移，让Django替我们修改数据库
      ```powershell
      python manage.py migrate
      # 输出如下内容，与我们创建数据库时输出的基本一样
      Operations to perform:
        Apply all migrations: admin, auth, contenttypes, learning_logs, sessions
      Running migrations:
        # 这里表明learning_logs应用迁移一切正常
        Applying learning_logs.0001_initial... OK
      ```
  * **每当需要修改“学习笔记”管理的数据是，都采取如下三个步骤：**
    1. 修改models.py
    2. 对learning_logs调用makemigrations
    3. 让Django迁移项目
  * **Django管理网站**
    * 为应用程序定义模型时，Django提供的管理网站（admin site）让我们能够轻松地处理模型。
    * 创建超级用户
      ```powershell
      python manage.py createsuperuser
      # 以下是交互信息
      Username (leave blank to use 'administrator'): ll_admin
      Email address: chenlfc@126.com
      Password:
      Password (again):
      Superuser created successfully.
      ```
  * 向管理网站注册模型 **admin.py**
    * Django自动再管理网站中添加了一些模型，如User和Group，但对于我们创建的模型，必须手工进行注册。
    ```powershell
    # 在终端激活服务器
    python manage.py runserver
    # 在浏览器中输入如下网址，进入管理员登陆界面
    http://127.0.0.1:8000/admin
    # 输入username和password
    ```
  * 定义模型 **Entry**
    1. 修改 **models.py** 文件
    2. 对learning_logs调用makemigrations
    3. 让Django迁移项目
    4. 修改 **admin.py** 文件，注册模型
  * **Django shell**
    * 输入一些数据后，就可以通过交互式终端会话以编程方式查看这些数据了。这种交互式环境成为 **Django shell**
    * 下面是一个交互式shell会话示例
      ```powershell
      python manage.py shell
      --snip--
      >>> from learning_logs.models import Topic
      >>> Topic.objects.all()
      <QuerySet [<Topic: Chess>, <Topic: Rock Climbing>]>
      ```
    * 我们可以像遍历列表一样遍历查询集
      ```powershell
      >>> topics = Topic.objects.all()
      >>> for topic in topics:
      ...     print(topic.id, topic)
      ...
      1 Chess
      2 Rock Climbing
      ```
    * 知道对象ID后，就可以获取该对象并查看其任何属性
      ```powershell
      >>> t = Topic.objects.get(id=1)
      >>> t.text
      'Chess'
      >>> t.date_added
      datetime.datetime(2018, 8, 14, 7, 53, 17, 576890, tzinfo=<UTC>)
      ```
    * 还可以查看与主题相关联的项目
      ```powershell
      >>> t.entry_set.all()
      <QuerySet [<Entry: The opening is the first part of the game, roughly...>,
      <Entry: 国际象棋的第一个阶段是大局，大致是钱10步左右。在开局阶段，最好做三件事情：将象和马调出来；努力控制...>]>
      ```
    * **每次修改模型后，都需要重启shell**
  * **Django API**
    * 编写访问项目中的数据的代码时，我们编写的是查询。
    * 关于如何查询数据的文档，其网址为[https://docs.djangoproject.com/en/2.1/topics/db/queries/](https://docs.djangoproject.com/en/2.1/topics/db/queries/)
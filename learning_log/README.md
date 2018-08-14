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
    ```bat
    python -m venv ll_env
    ```
  * 如果不能正常使用模块，可以安装virtualenv包
    ```bat
    pip install --user virtualenv
    ```
* ### 激活虚拟环境
  * 建立虚拟环境后，休要用以下命令激活它
    ```bat
    使用命令 ll_env\Scripts\activate 来激活这个虚拟环境
    要停止使用虚拟环境，可以执行命令 deactivate
    ```
* ### 安装Django
  * 创建并激活了虚拟环境后，就可以安装Django了
  * 激活虚拟环境后，执行一下命令
    ```bat
    pip install Django
    ```
* ### 在Django中创建项目
  * 在依然处于活动的虚拟环境下执行如下命令来新建一个项目
    ```bat
    django-admin.exe startproject learning_log .
    ```
  * 新建一个名为learning_log的项目,这个命令最后的句点让新项目使用合适的目录结构，这样开发完成后可轻松地将应用程序部署到服务器
  * 千万别忘了这个【 **句点** 】，否则部署时会遭遇一些配置问题。如果忘了，就将创建的文件和文件夹删除(ll_env除外)，再重新运行这个命令
    ```bat
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
    ```bat
    python manage.py migrate
    Operations to perform:
      Apply all migrations: admin, auth, contenttypes, sessions
    Running migrations:
      Applying contenttypes.0001_initial... OK
      --snip--
      
    ```
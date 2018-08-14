# 关于git的一些设置问题，以及安装与使用过程中的一些问题的汇总

> ![GitHub Logo](https://www.easyicon.net/download/png/1128210/48/)
>
> ## git 提交很慢或者卡住writing objects的解决方法

* 执行以下代码

  ```powershell
  git config --global http.postBuffer 524288000
  ```

* 解决github 打开、拉取、推送速度慢的问题
  * 打开ipaddress.com,查询如下两个域名，并分别记录下其对应的ip：

    ```powershell
    github.com
    github.global.ssl.fastly.net
    ```

  * 更新host文件

    ```powershell
    192.30.253.112 github.com
    151.101.185.194 github.global.ssl.fastly.net
    ```

  * 刷新dns缓存，在命令终端输入如下命令

    ```powershell
    ipconfig /flushdns
    ```

> ## 配置git

* 配置用户名与用户邮箱，同网站注册信息一致

  ```powershell
  git config --global user.name "YourName"
  git config --global user.email "YourName@gmail.com"
  ```

* 查看配置

  ```powershell
  git config user.name
  git config user.email
  ```

* 配置远程仓库地址，在项目根目录中打开终端，执行命令：

  ```powershell
  git remote add origin https://github.com/kenight/project1.git
  ```

* 将分支与远程地址进行关联

  ```powershell
  git push --set-upstream origin master
  ```

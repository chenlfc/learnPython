# 自己做的一些类与模块的存储位置及功能说明

> ## 气温转换类 ConversionForC
> ### 用于华氏度℉与摄氏度℃之间的转换
> 文件存储位置: anaiysis_data\conversion_f_c.py

* 变量： _temperature_ **要转换的温度**
* 方法：
  * _f_to_c()_ **华氏度到摄氏度的转换**
  * _c_to_f()_ **摄氏度到华氏度的转换**

    ``` template codes
    from conversion_f_c import ConversionForC as Cfc

    cfc = Cfc() #使用默认值，默认为0
    cfc.temperature = 30 # 设置要转换的温度的值
    print(cfc.f_to_c()) # 输出华氏度转换为摄氏度的值
    print(cfc.c_to_f()) # 输出摄氏度转换为华氏度的值
    ```
---

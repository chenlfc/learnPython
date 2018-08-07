# 网上找到的一些代码的实验
import requests
import re
import time
local = time.strftime("%Y.%m.%d")
url = "http://www.redocn.com/" #DevSkim: ignore DS137138 until 2018-08-07 
con = requests.get(url)
content = con.text
reg = r"(rb/.*?.jpg)"
a = re.findall(reg, content, re.S)[0]
print(a)
read = requests.get("https://s.cn.bing.net/az/hprichbg/" + a)
f = open("%s.pg" % local, 'wb')
f.write(read.content)
f.close()

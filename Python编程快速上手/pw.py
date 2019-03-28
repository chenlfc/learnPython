#! python3.7
# pw.py - 一个简单的密码保险箱程序，不具备保险功能
import sys
import pyperclip

# TODO:... ...

PASSWORD = {'email': 'adakdf;a;skjf432k4j23jOUIOJO',
            'blog': 'KLJLDJ)(ujdjfaslk23r32jh;asd',
            'pass': '12345'}

if len(sys.argv) < 2:
    print('python pw.py [account] - account为密码账号名')
    sys.exit()

account = sys.argv[1]

if account in PASSWORD:
    print(account + ' 的密码已经复制到剪贴板。')
    pyperclip.copy(PASSWORD[account])
else:
    print('账号名错误: ' + account)

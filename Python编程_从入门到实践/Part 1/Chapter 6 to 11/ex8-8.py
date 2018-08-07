# -*- coding: utf-8 -*-
# cretae by o.c. 2018/7/24
from _for_ex import pt_title

pt_title('EX 8 - 8')


def make_album(singer, album):
    """返回包含歌手，专辑的字典
    
    Arguments:
        singer {str}} -- 歌手
        album {str} -- 专辑名
    """
    return {'singer': singer, 'album': album}


albums = []

while True:
    print("请输入歌手及专辑的相关信息：")
    print("(输入'q'退出)")
    singer = input("歌手：")
    if singer == 'q':
        break
    album = input("专辑：")
    if album == 'q':
        break
    albums.append(make_album(singer, album))

print("\n--- 所有的歌手专辑信息如下 ---")
for al in albums:
    singer = al['singer']
    album = al['album']
    print("歌手 " + singer.title() + " 专辑 " + album.title())

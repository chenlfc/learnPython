# -*- coding: utf-8 -*-
# cretae by o.c. 2018/7/24
from _for_ex import pt_title

pt_title('EX 8 - 7')


def make_album(singer, name, album):
    """返回包含歌手，歌曲名和专辑的字典
    
    Arguments:
        singer {str}} -- 歌手
        name {str} -- 歌曲名
        album {str} -- 专辑名
    """
    return {'singer': singer, 'name': name, 'album': album}


albums = []
albums.append(make_album('jake', 'lalal', 'blla'))
albums.append(make_album('stven', 'vivivi', 'vlala'))

for album in albums:
    singer = album['singer']
    name = album['name']
    alb = album['album']
    print("\nThe singer name is: " + singer.title() + "\n\tDa da da is: " +
            name.title() + "\n\tAlbum is: " + alb.title())

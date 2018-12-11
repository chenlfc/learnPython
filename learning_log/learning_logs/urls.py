"""定义learning_logs的URL模式"""
# from django.conf.urls import url
from django.urls import path, re_path
from . import views

# urlpatterns是一个列表，包含可在应用程序learning_logs中请求的网页
urlpatterns = [
    # 主页
    # url(r'^$', views.index, name='index'),
    path('', views.index, name='index'),
    # 显示所有主题
    re_path(r'^topics/$', views.topics, name='topics'),
    # 特定主题的详细页面
    re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
]

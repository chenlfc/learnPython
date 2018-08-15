"""定义learning_logs的URL模式"""
# from django.conf.urls import url
from django.urls import path
from . import views

# urlpatterns是一个列表，包含可在应用程序learning_logs中请求的网页
urlpatterns = [
    # 主页
    # url(r'^$', views.index, name='index'),
    path('', views.index, name='index')
]

from django.contrib import admin

# Register your models here.
# 在这里注册我们的模型
from learning_logs.models import Topic, Entry

admin.site.register(Topic)
admin.site.register(Entry)

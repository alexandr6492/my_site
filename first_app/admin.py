from django.contrib import admin

from .models import Article, Topic, Comment, UserPreference

admin.site.register(Topic)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(UserPreference)

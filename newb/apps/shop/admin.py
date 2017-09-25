from django.contrib import admin

from .models import Developer, Editor, Genre, Platform, VideoGame

admin.site.register(Genre)
admin.site.register(Platform)
admin.site.register(Developer)
admin.site.register(Editor)
admin.site.register(VideoGame)

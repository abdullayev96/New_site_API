from django.contrib import admin

from .models import *


#
# class NewAdmin(admin.ModelAdmin):
#     list_display = ['id', 'name', 'title', 'show_images']
#
#     def show_images(self, obj):
#         return "\n".join([a.name for a in obj.images.all()])
#
#
#     list_filter = ('name', 'title')
#     search_fields = ("name",)
#     ordering = ("created_at",)

# class FotoAdmin(admin.ModelAdmin):
#     list_display = ['id','cat','img','body']
#
#     list_filter = ('cat__name', )
#     search_fields = ("body",)
#     ordering = ("created_at",)
#
#


#
# class VideoAdmin(admin.ModelAdmin):
#     list_display = ['id','get_videos','body','categ']
#
#     list_filter = ('categ__name', )
#     search_fields = ("body",)
#     ordering = ("created_at",)
#
#     def get_videos(self, obj):
#         return "\n".join([p.videos for p in obj.video.all()])
#


class ActionAdmin(admin.ModelAdmin):
    list_display = ['id','name' ,'img','body','cat']

    list_filter = ('cat__name', )
    search_fields = ("name",)
    ordering = ("created_at",)



# class InforAdmin(admin.ModelAdmin):
#     list_display = ['id','name','file','cate']
#
#     list_filter = ('cate__name', )
#     search_fields = ("name",)
#     ordering = ("created_at",)
#
#
#
#     def get_videos(self, obj):
#         return "\n".join([p.videos for p in obj.video.all()])
#



admin.site.register(News)
admin.site.register(ImageNews)
admin.site.register(Category)
admin.site.register(Video)
admin.site.register(Fotogallery)
admin.site.register(Videogallery)
admin.site.register(Action, ActionAdmin)
admin.site.register(FileBook)
admin.site.register(Information)




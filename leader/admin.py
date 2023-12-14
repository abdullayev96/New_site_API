from django.contrib import admin
from .models import *



class LeaderAdmin(admin.ModelAdmin):
    list_display = ['id','image', 'full_name','position','phone','email','admission_days','facebook',
                     'whatsapp','instagram', 'work_activity','tasks_functions']

    list_filter = ('full_name', 'phone')
    search_fields = ("full_name",)
    ordering = ("created_at",)



class PurposeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','title']

    list_filter = ('name', )
    search_fields = ("name",)
    ordering = ("created_at",)




class RegionAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name','position', 'facebook', 'whatsapp', 'instagram']

    list_filter = ('full_name','position' )
    search_fields = ("full_name",)
    ordering = ("created_at",)



class TizimAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','image', 'body']

    list_filter = ('name','body' )
    search_fields = ("name",)
    ordering = ("created_at",)




admin.site.register(Leader, LeaderAdmin)
admin.site.register(Category)
admin.site.register(Agency)
admin.site.register(Purpose, PurposeAdmin)
admin.site.register(RegionOffice, RegionAdmin)
admin.site.register(Tizim, TizimAdmin)


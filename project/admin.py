from django.contrib import admin
from .models import *




class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id','cat','name' ,'image','body','facebook','whatsapp','instagram']

    list_filter = ('cat__name', )
    search_fields = ("name",)
    ordering = ("created_at",)




admin.site.register(ProjectName, ProjectAdmin)
admin.site.register(Category)



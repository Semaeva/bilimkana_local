from django.contrib import admin
from .models import *
from parler.admin import TranslatableAdmin


class NewsAdmin(TranslatableAdmin):
    list_display = ('title', 'description', 'image')
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'image')
        }),
    )


class ManagersAdmin(TranslatableAdmin):
    list_display = ('name', 'title', 'image')
    fieldsets = (
        (None, {
            'fields': ('name', 'title', 'image')
        }),
    )


class ProjectsAdmin(TranslatableAdmin):
    list_display = ('title', 'description', 'image')
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'image')
        }),
    )


class TeachersAdmin(TranslatableAdmin):
    list_display = ('name', 'description', 'image')
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'image')
        }),
    )


class ContactAdmin(TranslatableAdmin):
    list_display = ('email', 'phone', "address", "insta")
    fieldsets = (
        (None, {
            'fields': ('email', 'phone', "address", "insta"),
        }),
    )


admin.site.register(News, NewsAdmin)
admin.site.register(OurPartner)
admin.site.register(NewsImage)
admin.site.register(CallBack)
admin.site.register(Managers, ManagersAdmin)
admin.site.register(Teachers, TeachersAdmin)
admin.site.register(Projects, ProjectsAdmin)
admin.site.register(Contact, ContactAdmin)



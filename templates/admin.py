# Register your models here.

from django.contrib import admin

from templates.models import Template, Member, TemplateCategory, TemplateTag, Text, Image, Introduce


class MemberAdmin(admin.ModelAdmin):
    search_fields = ['name']


class TemplateAdmin(admin.ModelAdmin):
    search_fields = ['name']


class TemplateCategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']


class TemplateTagAdmin(admin.ModelAdmin):
    search_fields = ['tag_name']


admin.site.register(Template, TemplateAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(TemplateCategory, TemplateCategoryAdmin)
admin.site.register(TemplateTag, TemplateTagAdmin)
admin.site.register(Text)
admin.site.register(Image)
admin.site.register(Introduce)

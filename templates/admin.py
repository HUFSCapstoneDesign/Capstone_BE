# Register your models here.

from django.contrib import admin

from templates.models import Member, Template, TemplateCategory, Image, Introduce, Text

admin.site.register(Member)
admin.site.register(Template)
admin.site.register(TemplateCategory)
admin.site.register(Image)
admin.site.register(Introduce)
admin.site.register(Text)

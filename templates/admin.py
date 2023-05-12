# Register your models here.

from django.contrib import admin

from templates.models import Template, Member, TemplateCategory, TemplateTag, Text, Image, Introduce

admin.site.register(Template)
admin.site.register(Member)
admin.site.register(TemplateCategory)
admin.site.register(TemplateTag)
admin.site.register(Text)
admin.site.register(Image)
admin.site.register(Introduce)

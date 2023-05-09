# Register your models here.

from django.contrib import admin

from templates.models import Member


class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

    admin.site.register(Member)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Form, Question

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1

class FormAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['user', 'form_title', 'form_description']}),
    ]
    inlines = [QuestionInline]


admin.site.register(Form, FormAdmin)

# Register your models here.

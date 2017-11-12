# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible

QUES_TYPE = (
    ('', 'Select'),
    ('SH', 'Short'),
    ('SC', 'Single Choice'),
    ('MC', 'Multiple Choice'),
)

@python_2_unicode_compatible  # only if you need to support Python 2
class Form(models.Model):
    user = models.ForeignKey(User, null=True)
    form_title = models.CharField(max_length=1000)
    form_description = models.CharField(max_length=2000)
    total_ques = models.CharField(max_length=2000, null=True)
    def __str__(self):
        return self.form_title


@python_2_unicode_compatible  # only if you need to support Python 2
class Question(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    #option = models.ForeignKey(Option, on_delete=models.CASCADE, null=True)
    ques_title = models.CharField(max_length=1000)
    ques_type = models.CharField(max_length=20, choices=QUES_TYPE, default='')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.ques_title

@python_2_unicode_compatible  # only if you need to support Python 2
class Option(models.Model):
    ques = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name






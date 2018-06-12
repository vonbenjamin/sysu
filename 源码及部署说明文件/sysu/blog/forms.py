#!/usr/bin/env python
# coding=utf-8
from datetime import datetime 
from .models import Blog
from django import forms
from django.forms import  fields
from django.contrib.contenttypes.models import ContentType
from django.db.models import ObjectDoesNotExist
from ckeditor.widgets import CKEditorWidget



class BlogForm(forms.Form):
    title= forms.CharField()
    content = forms.CharField(widget=CKEditorWidget(),error_messages={'required': '内容不能为空'})
    CHOICES= (
    ('程序设计','程序设计'),
    ('高等数学','高等数学'),
    ('系统分析与设计','系统分析与设计'),
    ('线性代数','线性代数'),
    ('数字电路','数字电路'),
    ) 
    blog_type = forms.ChoiceField(widget=forms.Select, choices=CHOICES)           
    def __init__(self, *args, **kwargs):
        if 'user' in kwargs:
            self.user = kwargs.pop('user')
        super(BlogForm, self).__init__(*args, **kwargs)

    def clean(self):
        # 判断用户是否登录
        if self.user.is_authenticated:
            self.cleaned_data['user'] = self.user
        else:
            raise forms.ValidationError('用户尚未登录')
        
        blog_type = self.cleaned_data['blog_type']
        return self.cleaned_data



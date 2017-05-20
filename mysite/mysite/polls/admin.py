#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015��12��16��

@author: chendq
'''

# admin  admin123654 dongquan@rrkd.cn

from django.contrib import admin
from .models import Question

admin.site.register(Question)
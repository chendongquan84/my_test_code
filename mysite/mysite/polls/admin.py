#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017年5月21日

@author: dongquan
'''

# admin  admin123654 dongquan@rrkd.cn

from django.contrib import admin
from .models import Question

admin.site.register(Question)
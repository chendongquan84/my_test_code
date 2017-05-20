#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017��5��17��

@author: dongquan
'''
import django
django.setup()

from .models import Question, Choice
print Question.objects.all()
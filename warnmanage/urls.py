#-*- coding:utf-8 -*-
from django.conf.urls import url
from django.contrib import admin
from warnmanage.warnhome import *
from warnmanage.warnloginfo import *
from cert.public import *
 

'''

'''



urlpatterns = [
     url('^home/', warnhome),
     url('^mailto/', mailtoindex),
     url('^mailtodel/(?P<id>\d*)/', mailtodel),
     url('^mailtoadd/', mailtoadd),
     url('^log/', warninfo),
     
     
     
     
     ]
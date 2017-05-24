#-*- coding:utf-8 -*-
from django.conf.urls import url
from django.contrib import admin
from certhome.certindex import *
from cert.public import indexdel
from searchcert.Searchcert import searchdate

'''

'''



urlpatterns = [
     url('^search/', searchdate),
     url('^date/', commitdate),
     
]
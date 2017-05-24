# -*- coding:utf-8 -*-
from django.conf.urls import url
from django.contrib import admin
from cert.certhp import  certmanage
from certhome.certindex import *
from cert.public import indexdel
from certhome.indexadd import *
from certhome.indexedit import *

'''

'''



urlpatterns = [
     url('^info.html', certmanage),
     url('^(?P<id>\d*)/', certindexinfo),
     url('^del/(?P<id>\d*)/', delcert),
     url('^add', addcert),
     url('^indexadd/(?P<id>\d*)/', indexadd),
     url('^indexsave/(?P<id>\d*)', indexsave),
     url('^indexdel/(?P<id>\d*)/(?P<delid>\d*)', indexdel),
     url('^indexedit/(?P<id>\d*)/(?P<editid>\d*)', indexedit),
     url('^editsave/(?P<id>\d*)/(?P<editid>\d*)', indexeditsave),
     
]

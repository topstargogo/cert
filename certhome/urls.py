# -*- coding:utf-8 -*-
from django.conf.urls import url
from django.contrib import admin
from certhome.certindex import *
from cert.public import indexdel
from certhome.indexadd import *
from certhome.indexedit import *

'''

'''



urlpatterns = [
     url('^info.html', certindexinfo),

     url('^indexadd/', indexadd),
     url('^indexsave/', indexsave),
     url('^indexdel/(?P<delid>\d*)', indexdel),
     url('^indexedit/(?P<editid>\d*)', indexedit),
     url('^editsave/(?P<editid>\d*)', indexeditsave),
     
]

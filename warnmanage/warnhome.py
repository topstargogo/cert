#-*- coding:utf-8 -*-

from django.shortcuts import render_to_response,redirect,render
from cert.public import *


def warnhome(request):
        return render_to_response('warn/warnhome.html')
    
def mailtoindex(request):
        ret =  mailtoinfo(request)
        return render(request,'warn/mailto.html',{'ret':ret})


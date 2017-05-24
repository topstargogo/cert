#-*- coding:utf-8 -*-

from warnmanage.models import *
from django.shortcuts import render_to_response, redirect, render

def warninfo(request):
    
    ret = warnlog.objects.all()
    return render(request,'warn/warnlog.html',{'ret':ret})

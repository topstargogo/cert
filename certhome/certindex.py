# -*- coding:utf-8 -*-


from django.shortcuts import render_to_response, redirect, render
from django.http.response import HttpResponse
from certhome.models import *
from cert.public import *

    
def certindexinfo(request):

    certinfo = systemdetail.objects.all().order_by("name")         
    ret = certdetailinfo(request, certinfo)

    return render(request, 'certindex.html', {'ret':ret})

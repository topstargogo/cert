# -*- coding:utf-8 -*-


from django.shortcuts import render_to_response, redirect, render
from django.http.response import HttpResponse
from certhome.models import *
from cert.public import *

    
def certindexinfo(request, id):
    certinfo = systemdetail.objects.filter(sysid_id=id)               
    ret = certdetailinfo(request, certinfo)         
    return render(request, 'certindex.html', {'ret':ret, 'id':id})

# -*- coding:utf-8 -*-

from django.shortcuts import render_to_response, redirect, render
from cert.public import *



def indexedit(request,  editid):
    
    ret = indexdetailinfo(request, editid)
    return render(request, 'editpage.html', {'ret':ret,  "editid":editid})

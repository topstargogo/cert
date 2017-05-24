# -*- coding:utf-8 -*-

from django.shortcuts import render_to_response, redirect, render
from cert.public import *



def indexadd(request, id):
    
    
    return render_to_response("addpage.html", {"id":id})

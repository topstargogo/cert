#-*- coding:utf-8 -*-

from django.shortcuts import render_to_response,redirect,render
from cert.public import *



def searchdate(request):
    
    
    return render_to_response("searchcert/search.html")
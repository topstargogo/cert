#-*- coding:utf-8 -*-

from django.shortcuts import render_to_response,redirect,render
from django.http.response import HttpResponse
from django.template.context_processors import request

def homepage(request):
        
        return render_to_response('certhome.html')    
            
            

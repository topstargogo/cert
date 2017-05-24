##-*- coding:utf-8 -*-

from django.shortcuts import render_to_response,redirect,render
from django.core.mail import send_mail  
from certhome.models import systemdetail
from datetime import datetime,date
from warnmanage.models import *
import time


def check():
    now = datetime.strptime(time.strftime('%Y-%m-%d',time.localtime(time.time())), '%Y-%m-%d').date()
    mail = ["".join(x.values()) for x in  mailto.objects.values("mailto")]
  
     
    date = systemdetail.objects.all()
    for i in date:
        if not i.publickeydaystop  is None and not  i.privatekeydaystop is None:
          if (i.publickeydaystop - now ).days == 31 or (i.privatekeydaystop - now ).days == 31 :
            send_mail('证书到期', u'%s到期'%(i.businessname), 'ops_notify@howbuy.com', mail, fail_silently=False)
            info = {"log":u'%s到期'%(i.businessname),"warndate":now}
            rs = warnlog(**info)
            rs.save()
            

           
            

     
    

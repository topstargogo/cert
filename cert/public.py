#-*- coding:utf-8 -*-

from warnmanage.models import *
from certhome.models import *
from django.shortcuts import render_to_response,redirect,render
from django.http.response import HttpResponse
from django.template.context_processors import request
from datetime import datetime,date
from itertools import chain
from django.db.models import Q
#from pip.cmdoptions import cert
from warnmanage.checkcert import check



def GetFormPost(request,FormId):
    new = dict()
    for x in FormId:
        new[x] = request.POST.get(x)
#          
        if  not new[x] == u"" and x == "publickeydaystart" :
             new[x]=datetime.strptime(new[x], '%Y-%m-%d').date()

             
        if  not new[x] == u"" and x == "publickeydaystop" :
             new[x]=datetime.strptime(new[x], '%Y-%m-%d').date()


             
        if not new[x] == u"" and x == "privatekeydaystart" :
             new[x]=datetime.strptime(new[x], '%Y-%m-%d').date()

             
        if not new[x] == u"" and x == "privatekeydaystop" :
             new[x]=datetime.strptime(new[x], '%Y-%m-%d').date()

        if not new[x] == u"" and x == "daystart" :
             new[x]=datetime.strptime(new[x], '%Y-%m-%d').date() 
        
        if not new[x] == u"" and x == "daystop" :
             new[x]=datetime.strptime(new[x], '%Y-%m-%d').date()    
             
    return new





def certdetailinfo(request,cert):
    
    
    for i in cert:
        if i.name == None:
           i.name = ""
        if i.businessname == None:
           i.businessname = ""
        if i.publickeydaystart == None:
           i.publickeydaystart = ""
        else:
           i.publickeydaystart=str(i.publickeydaystart)  
        if i.publickeydaystop == None:
           i.publickeydaystop = ""
        else:
           i.publickeydaystop=str(i.publickeydaystop)  
        if i.privatekeydaystart == None:
           i.privatekeydaystart = ""
        else:
           i.privatekeydaystart=str(i.privatekeydaystart)  
        if i.privatekeydaystop == None:
           i.privatekeydaystop = ""
        else:
           i.privatekeydaystop=str(i.privatekeydaystop)  
        if i.publicgain == None:
           i.publicgain = ""  
        if i.privategain == None:
           i.privategain = "" 
        if i.update == None:
           i.update = ""   
        
    return cert  


def indexdetailinfo(request,id):
    
    cert = systemdetail.objects.filter(id=id)
    for i in cert:
        if i.name == None:
           i.name = ""        
        if i.businessname == None:
           i.businessname = ""
        if i.publickeydaystart == None:
           i.publickeydaystart = ""
        else:
           i.publickeydaystart=str(i.publickeydaystart)  
        if i.publickeydaystop == None:
           i.publickeydaystop = ""
        else:
           i.publickeydaystop=str(i.publickeydaystop)  
        if i.privatekeydaystart == None:
           i.privatekeydaystart = ""
        else:
           i.privatekeydaystart=str(i.privatekeydaystart)  
        if i.privatekeydaystop == None:
           i.privatekeydaystop = ""
        else:
           i.privatekeydaystop=str(i.privatekeydaystop)  
        if i.publicgain == None:
           i.publicgain = ""  
        if i.privategain == None:
           i.privategain = "" 
        if i.update == None:
           i.update = ""   
        
    return cert  




def indexsave(request):
    if request.method == 'POST':


        form_key = ['id','name','businessname','publickeydaystart','publickeydaystop','privatekeydaystart','privatekeydaystop','publicgain','privategain','update']        
        form_value = GetFormPost(request,form_key)
        certid = []
        for a in systemdetail.objects.all():        
             certid.append(a.id)
        id = [ i for i in range(1,1000) ]    
        id = list(set(id)-set(certid))
        form_value["id"]=id[0]
        if form_value["publickeydaystart"] == u""  :
             form_value.pop("publickeydaystart")
        if form_value["publickeydaystop"] == u""  :
             form_value.pop("publickeydaystop") 
        if form_value["privatekeydaystart"] == u""  :
             form_value.pop("privatekeydaystart") 
        if form_value["privatekeydaystop"] == u""  :
             form_value.pop("privatekeydaystop")   
        rs = systemdetail(**form_value)
        rs.save()
        
        return redirect("/cert/info.html")

def indexdel(request,delid):
    systemdetail.objects.filter(id=delid).delete()
    return redirect("/cert/info.html")

def indexeditsave(request,editid):
    if request.method == 'POST':
 
 
        form_key = ['name','businessname','publickeydaystart','publickeydaystop','privatekeydaystart','privatekeydaystop','publicgain','privategain','update']        
        form_value = GetFormPost(request,form_key)
        form_value['id'] = int(editid)
        if form_value["publickeydaystart"] == u""  :
             form_value.pop("publickeydaystart")
        if form_value["publickeydaystop"] == u""  :
             form_value.pop("publickeydaystop") 
        if form_value["privatekeydaystart"] == u""  :
             form_value.pop("privatekeydaystart") 
        if form_value["privatekeydaystop"] == u""  :
             form_value.pop("privatekeydaystop")   
                
        rs = systemdetail(**form_value)
        rs.save()
        return redirect('/cert/info.html')
    
def commitdate(request):    
    ret = {}
    b = []
    if request.method == 'POST':
        form_key = ['daystart','daystop']
        form_value = GetFormPost(request,form_key)
        if form_value["daystart"] == u"" or form_value["daystop"] == u"" :
            ret["message"]= "日期不能为空"
        
            return render_to_response("searchcert/search.html",ret)   
        elif   form_value["daystart"]>form_value["daystop"]:
            ret["message"]= "结束日期必须大于开始日期"
            return render_to_response("searchcert/search.html",ret)
        else:            
            certinfo = systemdetail.objects.filter(Q(publickeydaystop__range=(form_value["daystart"],form_value["daystop"]))|Q(privatekeydaystop__range=(form_value["daystart"],form_value["daystop"])))           
            ret=certdetailinfo(request,certinfo)


            return render(request,'searchcert/searchresult.html',{'ret':ret})
               
            
def mailtoinfo(request):
                   
    mailtoinfo =  mailto.objects.all()
    return mailtoinfo
    
def mailtodel(request,id):
    mailto.objects.filter(id=id).delete()
    ret=mailtoinfo(request)
    return render(request,'warn/mailto.html',{'ret':ret})
def mailtoadd(request):
    mailid = []
    addmail = request.POST.get("mail")
    if not addmail is None and request.method == 'POST':
        
        addmail = addmail.strip()
        if not len(addmail) == 0  and  not addmail.find("@") == -1 and not addmail.find(".com") == -1:
            
        
            for a in mailto.objects.all():        
                mailid.append(a.id)
            id = [ i for i in range(1,1000) ]    
            id = list(set(id)-set(mailid))
               
            addmail = request.POST.get("mail")
            mailto.objects.create(id=id[0],mailto=addmail)
            return redirect('/warnmanage/mailto')
        else:
            ret=mailtoinfo(request)
           
            message='请输入正确的邮箱地址'

            return render(request,'warn/mailto.html',{'ret':ret,'message':message})
    else:
        return redirect('/warnmanage/mailto')

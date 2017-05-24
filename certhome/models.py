from __future__ import unicode_literals

from django.db import models

# Create your models here.
class systeminfo(models.Model):
    id = models.IntegerField(null=False, primary_key=True)
    name = models.CharField(max_length=30)
    
class systemdetail(models.Model):
    sysid = models.ForeignKey("systeminfo")  
    businessname = models.CharField(null=True, max_length=50)
    publickeydaystart = models.DateField(null=True, auto_now=False, auto_now_add=False)
    publickeydaystop = models.DateField(null=True, auto_now=False, auto_now_add=False)
    privatekeydaystart = models.DateField(null=True, auto_now=False, auto_now_add=False)
    privatekeydaystop = models.DateField(null=True, auto_now=False, auto_now_add=False)
    publicgain = models.CharField(null=True, max_length=50)
    privategain = models.CharField(null=True, max_length=50)
    update = models.CharField(null=True, max_length=50)

from __future__ import unicode_literals

from django.db import models

# Create your models here.


# Create your models here.
class mailto(models.Model):
    mailto = models.CharField(max_length=30)
    
class warnlog(models.Model):
    
    log = models.CharField(null=False,max_length=50)
    warndate = models.DateField(null=False,auto_now=False,auto_now_add=False)
    

from django.db import models
from user.models import *
# Create your models here.

class Home(models.Model):
    user=models.ForeignKey(Profile ,null=True,blank=True,on_delete=models.CASCADE)
    first=models.CharField("First Line Of Text in Homepage",max_length = 100,null=True,blank=True)
    second=models.CharField("Second Line Of Text in Homepage",max_length = 100,null=True,blank=True)
    third=models.CharField("Third Line Of Text in Homepage",max_length = 100,null=True,blank=True)
    
    class Meta:
        verbose_name_plural = "Home"

    def __str__(self):
        return self.first+" "+self.second
from django.db import models
from django.utils import timezone
# Create your models here.
class Customer_reg(models.Model):
    Name = models.CharField(max_length=200)
   
    Phone = models.CharField(max_length=200,unique=True)
    Address = models.CharField(max_length=200)
    
    Username = models.CharField(max_length=200,unique=True)
    Password = models.CharField(max_length=200)
    


class Volunteer_reg(models.Model):
    Name = models.CharField(max_length=200)
   
    Phone = models.CharField(max_length=200,unique=True)
    Address = models.CharField(max_length=200)
    
    Username = models.CharField(max_length=200,unique=True)
    Password = models.CharField(max_length=200)






class Waste_table(models.Model):
    Uname=models.CharField(max_length=200)
    Latitude=models.CharField(max_length=200)
    Longitude=models.CharField(max_length=200)
    Address=models.CharField(max_length=200)
    Description=models.CharField(max_length=200)
    Vstatus=models.CharField(max_length=200,default="Not accepted")
    Reqstatus=models.CharField(max_length=200,default="Nil")
    Image_path=models.CharField(max_length=200)
    Waste_types=models.CharField(max_length=200,default="")
    Date=models.CharField(max_length=200,default="")
    Vuname=models.CharField(max_length=200,default="")
    Status=models.CharField(max_length=200,default="Not completed")






class Chat_table(models.Model):
    From=models.CharField(max_length=250)
    To=models.CharField(max_length=300)
    chat=models.CharField(max_length=300)
    sts=models.CharField(max_length=300,default="not read")



class chatMessages(models.Model):
    user_from = models.IntegerField()
    user_to = models.IntegerField()
    message = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
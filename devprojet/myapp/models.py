from django.db import models
 
# Create your models here.


class login(models.Model):  
        name = models.CharField(max_length=100)  
        age = models.IntegerField()  
        mojor = models.CharField(max_length=15) 
        contact =models.IntegerField() 
   
        class Meta:  
            db_table = "tblemployee"
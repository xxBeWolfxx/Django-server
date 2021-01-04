from django.db import models
from django.db.models import Model
from django.core.validators import int_list_validator, validate_comma_separated_integer_list

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length = 15)
    lastname = models.CharField(max_length = 20)
    login = models.CharField(max_length = 10)
    password = models.CharField(max_length = 10)
    email = models.EmailField(max_length = 254, blank = True)
    ESPoutputs = models.ManyToManyField('ESPOut', blank = True, null = True)
    ESPsensor = models.ManyToManyField('ESPSensor', blank = True, null = True)
    ESPoCount = models.IntegerField(blank = True, default = 0)
    ESPsCount = models.IntegerField(blank = True, default = 0)
    
    def __str__(self):
        return self.lastname
    
    



class ESPSensor(models.Model):
    name = models.CharField(max_length = 20, null = True)
    pin = models.IntegerField()
    valueTemp = models.IntegerField(blank = True)
    
    valueAvgDay = models.CharField(validators=[validate_comma_separated_integer_list], max_length = 24, blank = True, default = '')
    valueAvgWeek = models.CharField(validators=[validate_comma_separated_integer_list], max_length = 7, blank = True, default = '')
    
    description = models.TextField(blank = True, null = True)
    
    def __str__(self):
        return self.name
    
    

	
    
    
class ESPOut(models.Model):
    name = models.CharField(max_length = 20, null = True)
    pin = models.IntegerField()
    status = models.BooleanField(default = False)
    description = models.TextField(blank = True, null = True)
    
    def __str__(self):
        return self.name
    





    

from django.db import models
import datetime

class Appointment(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    department = models.CharField(max_length=20)
    date = models.CharField(max_length=50)
    message = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    subject = models.CharField(max_length=20)
    message = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Comment(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.EmailField()
    date = datetime.date.today()
    message = models.CharField(max_length=100)
    def __str__(self):
        return self.fname
    
class Doctor(models.Model):
    name = models.CharField(max_length=20)
    department = models.CharField(max_length=20)
    degree = models.CharField(max_length=20)
    photo = models.ImageField(upload_to = 'images/', default = '')
    def __str__(self):
        return self.name
    
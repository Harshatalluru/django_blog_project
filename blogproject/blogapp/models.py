from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.

class post(models.Model):
    title = models.CharField(max_length=200)
    body = RichTextField()
    #image = models.ImageField(upload_to='images/',null=True, verbose_name="")
    Create_at = models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
        return self.title

    
class contactus(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    country = models.CharField(max_length=10)
    message = models.TextField(max_length=10000000)

    def __str__(self):
        return self.first_name


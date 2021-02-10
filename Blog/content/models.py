from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class Content(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=200,unique=True)
    image = models.ImageField(upload_to='image/')
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    Choice = (('PUBLIC','PUBLIC'),('PRIVATE','PRIVATE'))
    status = models.CharField(choices=Choice, max_length=20)
    slug = models.SlugField()

    def __str__(self):
        return self.title
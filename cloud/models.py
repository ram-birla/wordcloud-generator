from django.db import models

# Create your models here.
class Wrdcloud(models.Model):
    text = models.FileField(upload_to = 'cloud/text/')
    image = models.ImageField(upload_to='cloud/image/',default='',blank=True, null=True)
    cloud = models.CharField(max_length=20,default="")

class Simple(models.Model):
    text = models.FileField(upload_to = 'cloud/stext/')
    cloud = models.CharField(max_length=20,default="")


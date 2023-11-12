from django.db import models

# Create your models here.
class PostContent(models.Model):
            title = models.CharField(max_length = 100)
            author = models.CharField(max_length = 50) 
            description = models.CharField(max_length = 100)
            categories = models.CharField(max_length = 100,default = "general")
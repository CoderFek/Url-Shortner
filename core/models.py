from django.db import models
# Create your models here.

class URL(models.Model):
    original_url = models.URLField(max_length=500)
    alias = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.original_url
    
    

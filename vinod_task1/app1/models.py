from django.db import models

# Create your models here.
class Medician(models.Model):
    des=models.CharField(max_length=50)
    med=models.CharField(max_length=50)

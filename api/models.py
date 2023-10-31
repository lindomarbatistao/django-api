from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    cidade = models.CharField(max_length=50)


#   py manage.py makemigrations
#   py manage.py migrate


from django.db import models

# Create your models here.

class Socios(models.Model):
    num_socio = models.IntegerField()
    dni = models.CharField(max_length=10)
    password = models.CharField(max_length=30)



    def __str__(self):
        return f"{self.num_socio} - {self.dni} - {self.password}"
from django.db import models


class Dashboard (models.Model):
    genero = models.CharField(max_length=100)
    edad = models.IntegerField()
    direccion = models.CharField(max_length=100)
    

    def __str__(self): 
         return '%s %s %s' % (self.genero, self.edad,self.direccion)
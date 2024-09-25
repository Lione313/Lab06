from django.db import models


class Categoria(models.Model):
    nombre=models.TextField(max_length=20)
    pub_date=models.DateTimeField("Fecha de registro ",auto_now=True)


    def __str__ (self):
       return self.nombre
class Producto (models.Model):
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre=models.TextField(max_length=20)
    precio=models.DecimalField(max_digits=10, decimal_places=2)
    stock=models.IntegerField(default=0)
    ub_date=models.DateTimeField("dato publicado")



    def __str__(self):
        return self.nombre

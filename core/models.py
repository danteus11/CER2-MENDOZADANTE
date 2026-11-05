#corazon de la base de datos 
from django.db import models

#Definir en base de datos
class Categoria(models.Model):
    #texto corto
    nombre = models.CharField(max_length=100, verbose_name="Nombre de la Categoría")
    #texto largo
    descripcion = models.TextField(verbose_name="Descripción")

    #cómo se va a mostrar cada registro individual
    def __str__(self):
        return self.nombre


class LugarPatrimonial(models.Model):
    nombre = models.CharField(max_length=150, verbose_name="Nombre del Lugar")
    descripcion = models.TextField(verbose_name="Descripción")
    ubicacion = models.CharField(max_length=200, verbose_name="Ubicación")
    #num enteros
    anio_construccion = models.IntegerField(verbose_name="Año de Construcción")
    #guardar url
    imagen = models.URLField(verbose_name="URL de la Imagen")
    #Llave foránea que vincula cada lugar con una Categoría, elimina los lugares asociados para mantener la integridad de la base de datos
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoría")

    def __str__(self):
        return self.nombre

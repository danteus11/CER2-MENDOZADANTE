from django.db import models

from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre de la Categoría")
    descripcion = models.TextField(verbose_name="Descripción")

    def __str__(self):
        return self.nombre


class LugarPatrimonial(models.Model):
    nombre = models.CharField(max_length=150, verbose_name="Nombre del Lugar")
    descripcion = models.TextField(verbose_name="Descripción")
    ubicacion = models.CharField(max_length=200, verbose_name="Ubicación")
    anio_construccion = models.IntegerField(verbose_name="Año de Construcción")
    # Usamos URLField para las imágenes tal como sugiere el anexo de la pauta
    imagen = models.URLField(verbose_name="URL de la Imagen")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoría")

    def __str__(self):
        return self.nombre

#para que las tablas de base de datos se puedan ver y administrar
from django.contrib import admin
from .models import Categoria, LugarPatrimonial

admin.site.register(Categoria)
admin.site.register(LugarPatrimonial)

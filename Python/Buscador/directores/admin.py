from django.contrib import admin

# Register your models here.
from .models import directores, peliculas, sinopsis

admin.site.register(directores)
admin.site.register(peliculas)
admin.site.register(sinopsis)
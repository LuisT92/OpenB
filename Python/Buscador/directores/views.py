from django.shortcuts import render

from .models import directores, peliculas, sinopsis


def index(request):
    directoresCine = directores.objects.filter(nombre='nombre').order_by('nombre')
    return render(request,
                  'index.html',
                  {'Directores': directoresCine}
                  )

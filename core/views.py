from django.shortcuts import render_to_response

from restaurante.views import get_restaurantes
from cancion.views import get_canciones

def home(request):
	restaurantes = get_restaurantes(3)
	canciones = get_canciones(3)

	return render_to_response('index.html', {'restaurantes': restaurantes, 'canciones': canciones})

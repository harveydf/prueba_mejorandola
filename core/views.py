from django.shortcuts import render_to_response

from restaurante.views import get_restaurantes

def home(request):
	restaurantes = get_restaurantes(3)

	return render_to_response('index.html', {'restaurantes': restaurantes})

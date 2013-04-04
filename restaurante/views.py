import json

from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext

from restaurante.models import Restaurante, RestauranteForm

def get_restaurantes(limit=None):
	restaurantes = Restaurante.objects.all().order_by('-id')
	
	if limit is not None:
		restaurantes = restaurantes[:limit]

	return restaurantes

def show_restaurantes(request):
	if request.method == 'POST':
		form = RestauranteForm(request.POST)

		if form.is_valid():
			form.save()
			form = RestauranteForm()

	else:
		form = RestauranteForm()
		
	restaurantes = get_restaurantes()
	
	return render_to_response(
			'restaurantes.html', 
			{'restaurantes': restaurantes, 'form': form},
			context_instance=RequestContext(request)
		)


def cargar_restaurante(request, id):

	try:
		restaurante = Restaurante.objects.get(id=id)

	except:
		raise Http404

	else:
		if request.method == 'POST':
			form = RestauranteForm(request.POST, instance=restaurante)

			if form.is_valid():
				form.save()
				form = RestauranteForm(instance=restaurante)
		
		else:
			form = RestauranteForm(instance=restaurante)

		return render_to_response(
				'restaurante_id.html', 
				{'restaurante': restaurante, 'form': form},
				context_instance=RequestContext(request)
			)

def eliminar_restaurante(request, id):
	if request.is_ajax():

		try:
			restaurante = Restaurante.objects.get(id=id)

		except:
			return HttpResponse(
					json.dumps({'error': 'Error al eliminar, por favor intente nuevamente'}),
					content_type="application/json; charset=utf8"
				)

		else:
			restaurante.delete()
			return HttpResponse(
					json.dumps({'redirect': '/restaurante/'}),
					content_type="application/json; charset=utf8"
				)

	else:
		raise Http404

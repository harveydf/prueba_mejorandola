import json

from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext

from cancion.models import Cancion, CancionForm

def get_canciones(limit=None):
	canciones = Cancion.objects.all().order_by('-id')
	
	if limit is not None:
		canciones = canciones[:limit]

	return canciones

def show_cancion(request):
	if request.method == 'POST':
		form = CancionForm(request.POST, request.FILES)

		if form.is_valid():
			form.save()
			form = CancionForm()

	else:
		form = CancionForm()
		
	canciones = get_canciones()
	
	return render_to_response(
			'canciones.html', 
			{'canciones': canciones, 'form': form},
			context_instance=RequestContext(request)
		)

def cargar_cancion(request, id):

	try:
		cancion = Cancion.objects.get(id=id)

	except:
		raise Http404

	else:
		if request.method == 'POST':
			form = CancionForm(request.POST, request.FILES, instance=cancion)

			print request.FILES

			if form.is_valid():
				form.save()
				form = CancionForm(instance=cancion)
		
		else:
			form = CancionForm(instance=cancion)

		return render_to_response(
				'cancion_id.html', 
				{'cancion': cancion, 'form': form},
				context_instance=RequestContext(request)
			)


def eliminar_cancion(request, id):
	if request.is_ajax():

		try:
			cancion = Cancion.objects.get(id=id)

		except:
			return HttpResponse(
					json.dumps({'error': 'Error al eliminar, por favor intente nuevamente'}),
					content_type="application/json; charset=utf8"
				)

		else:
			cancion.delete()
			return HttpResponse(
					json.dumps({'redirect': '/cancion/'}),
					content_type="application/json; charset=utf8"
				)

	else:
		raise Http404

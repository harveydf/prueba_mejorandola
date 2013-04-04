from django.forms import ModelForm

from core.models import Core, models

class Restaurante(Core):
	direccion = models.CharField(max_length=255)
	tipo_comida = models.CharField(max_length=255)


	def __unicode__(self):
		return self.titulo

class RestauranteForm(ModelForm):
	
	class Meta:
		model = Restaurante
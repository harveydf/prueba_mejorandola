from core.models import Core, models

class Cancion(Core):
	album = models.CharField(max_length=255)
	foto = models.ImageField(upload_to="media/")
	

	def __unicode__(self):
		return self.titulo

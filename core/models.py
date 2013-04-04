from django.db import models

class Core(models.Model):
	titulo = models.CharField(max_length=255)
	autor = models.CharField(max_length=255)
	contenido = models.TextField()

	class Meta:
		abstract = True
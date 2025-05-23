from django.db import models

# Create your models here.

class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    subtitle = models.CharField(max_length=200, verbose_name="Subtítulo")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(upload_to="services", verbose_name="Imagen")
    created = models.DateTimeField(auto_now=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now_add=True, verbose_name="Última modificación")

    class Meta():
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        ordering = ["created"]

    def __str__(self):
        return self.title 
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User #Es el modelo de usuarios, contiene todos los usuarios registrados en el panel de administrador
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now_add=True, verbose_name="Última modificación")

    class Meta():
        verbose_name = "categoría"
        verbose_name_plural = "categorías"
        ordering = ["-created"]

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido")
    published = models.DateTimeField(verbose_name = "Fecha de publicación", default=now)
    image = models.ImageField(upload_to="blog", verbose_name="Imagen", null=True, blank=True)
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)#on_delete=>Decirle al modelo que hacer en caso de que el campo con el que lo hayamos relacionado sea eliminado(Si el user al que esté enlazado se elimina, "models.CASCADE" eliminará en cascada todos los post cuyo autor sea ese Usuario.)
    categories = models.ManyToManyField(Category, verbose_name="Categorías", related_name="get_posts")
    created = models.DateTimeField(auto_now=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now_add=True, verbose_name="Última modificación")

    class Meta():
        verbose_name = "entrada"
        verbose_name_plural = "entradas"
        ordering = ["created"]

    def __str__(self):
        return self.title


from django import template
from pages.models import Page

register = template.Library()#Para poder devolver un template tag creado por nosotros, tendremos que añadirlo a la librería de templates
@register.simple_tag#Convierto la funcion --get_page_list-- en un tag simple y lo resitro en la librería de templates 
def get_page_list():
    pages = Page.objects.all()
    return pages#Esto será lo que va a devolver el template tags que queremos crear.
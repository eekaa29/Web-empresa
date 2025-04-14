from django.contrib import admin
from .models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display = ("title", "author", "published", "post_categories")
    ordering = ("author", "published")#Se ordena en base al author, y después en base a la fecha de publicación. En caso de querer ordenar solo por un campo hay que poner el campo y después una coma para que entienda que es una tupla. Ejemplo=>("author", )
    search_fields = ("title", "author__username", "categories__name" )#Crea una barra para buscar en base al parametro o parámetros de la tupla. Author y category necesitan una sintaxis especial debido a que son datos relacionales del otro modelo.
    date_hierarchy = "published"#Para jerarquizar por las fechas que haya
    list_filter = ("author__username", "categories__name")#Para flitar en base a lo que queramos.(Lo lógico sería filtar por campos que sean relaciones con otro modelo(en este caso author y category))

    #Crear manualmente una columna para poder "ordenar" los diferentes objetos dentro la app creada en el admin(dicho de otra manera, poder crear una columna para poder añadir al list_display)
    def post_categories(self, obj):
        return ",".join([c.name for c in obj.categories.all().order_by("name")])
    post_categories.short_description = "Categorías"
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
from django.contrib import admin
from .models import Link
# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

    def get_readonly_fields(self, request, obj = None):#Funcion para añadir campos al apartado de readonly_fields
        if request.user.groups.filter(name="Personal").exists():#Comprobar en tiempo de ejecución si el usuario forma parte del grupo "Personal"
            return ("created", "updated", "key", "name")
        else:
            return ("created", "updated")

        

admin.site.register(Link, LinkAdmin)

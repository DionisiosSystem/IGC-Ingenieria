from django.contrib import admin
from .models import Usuario,Contacto


# Register your models here.
# Esto se muestra en el adm de jango

class ContactoAdmin(admin.ModelAdmin):
       list_display = ('Nombre','Apellido','Email','Telefono','Mensaje','Fecha','Estado')
       search_fields = ('Fecha','Estado')  # campo de busqueda en el portad admin
       list_filter = ('Fecha',)
       date_hierarchy = 'Fecha'


class UsuarioAdmin(admin.ModelAdmin):
       list_display = ('Nombre','Apellido','Email')


admin.site.register(Usuario,UsuarioAdmin)
admin.site.register(Contacto,ContactoAdmin)
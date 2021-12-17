#from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from personas.models import Persona, Domicilio

# Create your views here.

#--Personas--#
#Aplicación del patrón de diseño MVT, Model View Template.
#El patrón de diseño MVT es una buena práctica para el desarrollo de aplicaciones web.
def bienvenido(request):
    #Ahora vamos a utilizar la información de modelo de la aplicación de Personas, utilizando lo que tenemos en la tabla de personas.
    numero_personas = Persona.objects.count() #Cada clase de django tiene acceso a un atributo llamado objects. Que nos permite obtener información de la base de datos relacionada con esta clase de modelos
    # personas = Persona.objects.all() #Obtenemos todos los objetos establecidos en el modelo de la app Personas.
    personas = Persona.objects.order_by('id') #Ordenaremos la tabla según el id en orden creciente.
    return render(request, 'bienvenido.html', {'numero_personas':numero_personas, 'personas':personas}) #El render nos permite pasar un diccionario de datos a la plantilla.


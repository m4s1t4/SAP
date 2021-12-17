from django.shortcuts import get_object_or_404, render, redirect
from personas.models import Persona
#from django.forms import modelform_factory
from personas.forms import PersonaForm


#--- Views ---#

#--- Detalles de las personas ---#
def detallePersona(request, id):
    #persona = Persona.objects.get(pk=id)
    persona = get_object_or_404(Persona, pk=id)
    return render(request, 'personas/detalle.html', {'persona':persona})

#---Agregar personas---#
#PersonaForm = modelform_factory(Persona, exclude=[])
def nuevaPersona(request):
    #Ahora utilizaremos una clase de django para crear un nuevo objeto el cual va a tener el objeto de formulario que esta relacionado con la modelo de persona.
    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST)
        if formaPersona.is_valid(): #Validamos el formulario para que se almacene en el servidor
            formaPersona.save() #Si es válido el fomulario se va a guardar en el servidor
            return redirect('index') 
    else:
        formaPersona = PersonaForm()

        return render(request, 'personas/nueva_persona.html', {'formaPersona': formaPersona}) #Si el formulario no es válido nos mostrará los errores que hay, o incluso nos mostrará la infromación colocada en el formulario.

#---Editar personas---#
def editarPersona(request, id):
        persona = get_object_or_404(Persona, pk=id) #Recuperamos la persona que queremos editar
    #Ahora editaremos las personas.
        if request.method == 'POST': #Si hacemos el envio del formulario
            formaPersona = PersonaForm(request.POST, instance=persona) #Entonces recuperamos el formulario
            if formaPersona.is_valid(): #Validamos el formulario para que se almacene en el servidor
                formaPersona.save() #Si es válido el fomulario se va a guardar en el servidor
                return redirect('index') 
        else: 
            formaPersona = PersonaForm(instance=persona) #Le pasamos la persona que queremos editar al formulario
        return render(request, 'personas/editar.html', {'formaPersona': formaPersona}) #Si el formulario no es válido nos mostrará los errores que hay, o incluso nos mostrará la infromación colocada en el formulario.

#---Eliminar personas---#
def eliminarPersona(request, id): #Así sabemos que persona queremos eliminar
    #Ahora eliminaremos las personas.
        persona = get_object_or_404(Persona, pk=id)#Recuperamos la persona que queremos editar
        if persona:
            persona.delete()
        return redirect('index')    



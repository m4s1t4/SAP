from django.db import models

# Create your models here.
class Domicilio(models.Model):
    calle = models.CharField(max_length=255)
    numero_calle = models.IntegerField()
    pais = models.CharField(max_length=255)

    def __str__(self):
        return f'Domicilio {self.id}: {self.calle} {self.numero_calle} {self.pais}'

class Persona(models.Model): #Todas las clases modelos en django deben depender de una clase padre llamada en este caso models.Model, para que el ORM de Django pueda reconmocerla como una clase que va a persistir en la base de datos.
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    domicilio = models.ForeignKey(Domicilio, on_delete=models.SET_NULL, null=True) #Relacino la clase Domicilio con la clase de Persona para hacer una base de datos relacional, y le establezco que pasaría si elimino algún valor de la clase Domicilio.

    def __str__(self):
        return f'Persona {self.id}: {self.nombre} {self.apellido} {self.email}'
        

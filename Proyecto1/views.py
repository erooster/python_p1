from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render
class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido

# Cargar plantillas con cargador importandolo : from django.template import loader
def saludo(request):

    p1=Persona("Emilio", "Rooster")

    ahora=datetime.datetime.now()
    temasDelCurso=["Plantillas","Modelos","Formularios","Vistas","Despliegue"]
    # doc_externo=get_template('saludo.html')
    # documento=doc_externo.render({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"momento_actual":ahora,"temas":temasDelCurso})
    return render(request,"saludo.html",{"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"momento_actual":ahora,"temas":temasDelCurso})


# Cargar plantilla de forma no debida
# def saludo(request):

#     p1=Persona("Emilio", "Rooster")

#     # nombre="Juan"
#     # apellido="Diáz"
#     ahora=datetime.datetime.now()
#     temasDelCurso=["Plantillas","Modelos","Formularios","Vistas","Despliegue"]
#     # temasDelCurso=[]
#  
#     doc_externo=open("/home/shdaemon/Desktop/Deskontop/django/Proyecto1/Proyecto1/views/saludo.html")

#     #Plantilla
#     plt=Template(doc_externo.read())

#     doc_externo.close()

#     #Contexto vacio
#     # ctx=Context({"nombre_persona":nombre,"apellido_persona":"Diáz","momento_actual":ahora})
#     ctx=Context({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"momento_actual":ahora,"temas":temasDelCurso})
#     #renderizar documento

#     documento=plt.render(ctx)
#     return HttpResponse(documento)


# DE ESTA MANERA NO SE DEBE USAR, LA FORMA ADECUADA ES USANDO PLANTILLA (VISTAS)
# def saludo(request):  #Primera Vista / Devuelve una respuesta

#     documento="<html><body><h1>Hi mate, this is my first page with Django</h1></body></html>"

#     return HttpResponse(documento)


def despedida(request):  #Primera Vista / Devuelve una respuesta
    
    documento="""
    <html>
        <body>
            <h1>Good by mate</h1>
        </body>
    </html>
    """

    return HttpResponse(documento)

def dameFecha(request):

    fecha_actual=datetime.datetime.now()
    documento="""
    <html>
        <body>
            <h3>
                Fecha y hora actual %s
            </h3>
        </body>
    </html>""" % fecha_actual

    return HttpResponse(documento)

def calculaEdad(request, edad,agno):

    # edadActual=27
    periodo=agno-2020
    edadFutura=edad+periodo
    documento="<html><body><h3>En el año %s tendrás %s años</h3></body></html>" %(agno, edadFutura)

    return HttpResponse(documento)


    # def despedida(request):  #Primera Vista / Devuelve una respuesta
    # return HttpResponse("Goodbye mate")
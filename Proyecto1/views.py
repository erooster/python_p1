from django.http import HttpResponse
import datetime
from django.template import Template, Context


def saludo(request):

    doc_externo=open("/home/shdaemon/Desktop/Deskontop/django/Proyecto1/Proyecto1/views/saludo.html")
    #Plantilla
    plt=Template(doc_externo.read())

    doc_externo.close()

    #Contexto vacio
    ctx=Context()
    #renderizar documento
    documento=plt.render(ctx)

    return HttpResponse(documento)


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
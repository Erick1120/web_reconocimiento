from django.http import HttpResponse

def saludo(request):

    return HttpResponse("Hola mundo")

def despedida(reques):
    return  HttpResponse("Adios")
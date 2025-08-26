from django.http import HttpResponse

def hello_world_view(request):
    return HttpResponse("Hello World")

def my_name_view(request):
    return HttpResponse("JOAN LENIN VARGAS GUAMAN") 
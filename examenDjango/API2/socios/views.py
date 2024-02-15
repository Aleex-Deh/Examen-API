from django.shortcuts import render
from django.http import JsonResponse
from .models import Socios
from django.views.decorators.csrf import csrf_exempt
import json



#Esta función listará todos el numero de socio y su dni, pero no la contraseña por temas de seguridad
def list_socios(request):
    
    # Vista para obtener todos los socios y devolverlas en formato JSON.
    titulos = Socios.objects.all()    # Le asigno el valor de mostrarlo todo. 
    data = [{'DNI': titulo.dni, 'Socio': titulo.num_socio} for titulo in titulos] # Le asigno el valor del json 
    return JsonResponse({'Socio': data})


@csrf_exempt    # Utilizo el @crsf_exempt, para así poder usarlos mediante el POST
#Esta función añadirá un nuevo socio.
def add_socio(request):
 
    data = request.POST
        
    # Lo convierto a string, ya que me llega en b(bites) y no puedo operar así.
    my_json = json.loads(request.body.decode('utf8').replace("'", '"'))
    
    dni = my_json['dni']
    num_socio = my_json['num_socio']
    password = my_json['password']
    
    # Aqui es donde se listará el dni, el num_socio y la password
    Socios.objects.create(dni=dni, num_socio=num_socio, password=password)
    return JsonResponse({'Su contraseña se ha guardado con exito' : '.'})


@csrf_exempt    # Utilizo el @crsf_exempt, para así poder usarlos mediante el POST
#Esta función modificara la contraseña de un socio ya existente.
def edit_password(request):
    
    data = request.POST
    # Lo convierto a string, ya que me llega en b(bites) y no puedo operar así.
    my_json = json.loads(request.body.decode('utf8').replace("'", '"'))

    num_socio = my_json['num_socio']
    password = my_json['password']

    # Aqui filtro, ya que es un POST para así a ese num_socio asignarle la nueva password
    Socios.objects.filter(num_socio=num_socio).update(password=password)
    return JsonResponse ({'Buenas, esta es su nueva contraseña': password})
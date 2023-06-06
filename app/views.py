from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

teachers = [
    {
        'id': '1',
        'name': 'Raul',
        'surname': 'Rufo',
        'age': 19
    },
    {
        'id': '2',
        'name': 'Luis',
        'surname': 'Garcia',
        'age': 23
    },
     {
        'id': '3',
        'name': 'Garcia',
        'surname': 'Marquez',
        'age': 64
    },
]

alumns = [
    {
        "name": "Alexis",
        "id": "alexis",
        "age": 26,
        "birthplace": "Sonora",
        "status": "active",
        "gendre": "h",
        "bio": "Guapo y sensible, sin embargo sabe que debe confiar mas en si mismo para que no le afecten las opiniones de los demas. Esta soltero y busca a la mujer de su vida. Consentido por su familia y trae lo nortenio en la sangre. Se define como un gran admirador del mitico Joan Sebastian."
    },
    {
        "name": "Azucena",
        "id": "azucena",
        "age": "31",
        "birthplace": "Jalisto",
        "status": "active",
        "gendre": "m",
        "bio": "Mujer luchadora que con esfuerzo y con coraje ha sacado, sola, a sus dos hijos pequenios adelante. No ha tenido suerte en el amor, sin embargo es una chica con muchas amistades. Gracias a la musica ha salido de situaciones dificiles. Le gusta hacer deporte y se identifica con la pelicula de Hercules."
    },
    {
        "name": "Chucho",
        "id": "chucho",
        "age": "14",
        "birthplace": "Mazatlan, Sinaloa",
        "status": "active",
        "gendre": "h",
        "bio": "Es el alumno mas joven en la historia de La Academia. A su corta edad ya es todo un galan que enamora a todas las mujeres. Con su simpatia, ternura y extraordinaria voz conquistara el corazon de la audiencia."
    },
    {
        "name": "Diana",
        "id": "diana",
        "age": "21",
        "birthplace": "Veracruz",
        "status": "active",
        "gendre": "m",
        "bio": "Es una mujer de ideas y metas muy claras. Proviene de una familia de musicos, en donde todo reconocen su talento. Su sonrisa, simpatia y humildad son sus senias de identidad. Consciente de que su voz no sera eterna, quiere sacar su maximo rendimiento dentro de La Academia 10."
    },
    {
        "name": "Erik",
        "id": "erik",
        "age": "26",
        "birthplace": "Puebla",
        "status": "active",
        "gendre": "h",
        "bio": "Se define como el no tipico galan de telenovela. Es de origen humilde, sencilla personalidad y a punto de convertirse en padre por segunda vez en su vida. Pretende que el nacimiento de su hijo y su entrada en La Academia 10, rubriquen un anio de exitos.",
    },
    {
        "name": "Freddy",
        "id": "freddy",
        "age": "35",
        "birthplace": "Michoacan",
        "status": "active",
        "gendre": "h",
        "bio": "Es divertido, sincero, amigable y lleno de energia. En distintas ocasiones ha estado cerca de lograr sus suenios, pero no ha sido hasta su entrada en La Academia 10 que ha podido alcanzarlos.",
    }
]

def home(request):
    return render(request, 'home.html')

def proff(request, tc):
    teachers_Obj = None
    for i in teachers:
        if i['id'] == tc:
            teachers_Obj = i
    context = {'tcs': teachers_Obj}
    return render(request, 'proff.html', context)

def proffs(request):
    context = {'tcs': teachers}
    return render(request, 'proffs.html', context)

def student(request, st):
    alumn_Obj = None
    for i in alumns:
        if i['id'] == st:
            alumn_Obj = i
    context = {'std': alumn_Obj}
    return render(request, 'student.html', context)

def students(request):
    context = {'std': alumns}
    return render(request, 'students.html', context)
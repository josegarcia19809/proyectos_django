from django.http import Http404
from django.shortcuts import render


def index(request):
    return render(request, 'catalogo/index.html')


# MÓDULO 1
# Variables simples

def videojuego(request):
    titulo = "The Legend of Zelda"
    genero = "Aventura"
    plataforma = "Nintendo Switch"
    anio = 2017
    imagen = "zelda.jpg"

    contexto = {
        "titulo": titulo,
        "genero": genero,
        "plataforma": plataforma,
        "anio": anio,
        "imagen": imagen
    }

    return render(request, 'catalogo/videojuego.html', contexto)


# MÓDULO 2 Y 3
# Diccionario y arreglo de diccionarios

def catalogo(request):
    videojuegos = obtener_videojuegos()

    return render(request, "catalogo/catalogo.html", {"videojuegos": videojuegos})


def detalle(request, id):
    try:
        videojuegos = obtener_videojuegos()
        juego_encontrado = videojuegos[id - 1]

        return render(request, "catalogo/detalle.html", {"juego": juego_encontrado})
    except:
        raise Http404


def obtener_videojuegos():
    return [

        {"id": 1, "titulo": "The Legend of Zelda", "genero": "Aventura",
         "plataforma": "Nintendo Switch", "anio": 2017, "imagen": "zelda.jpg"},

        {"id": 2, "titulo": "Halo Infinite", "genero": "Shooter",
         "plataforma": "Xbox Series X", "anio": 2021, "imagen": "halo_infinite.jpg"},

        {"id": 3, "titulo": "Among Us", "genero": "Party", "plataforma": "PC",
         "anio": 2018, "imagen": "among_us.jpg"},

        {"id": 4, "titulo": "Minecraft", "genero": "Sandbox", "plataforma": "PC",
         "anio": 2011, "imagen": "minecraft.jpg"},

        {"id": 5, "titulo": "Fortnite", "genero": "Battle Royale", "plataforma": "PC",
         "anio": 2017, "imagen": "fortnite.jpg"},

        {"id": 6, "titulo": "Super Mario Odyssey", "genero": "Aventura",
         "plataforma": "Nintendo Switch", "anio": 2017,
         "imagen": "super_mario_odyssey.png"},

        {"id": 7, "titulo": "Cyberpunk 2077", "genero": "RPG",
         "plataforma": "PlayStation 4", "anio": 2020, "imagen": "cyberpunk2077.jpg"},

        {"id": 8, "titulo": "The Witcher 3", "genero": "RPG", "plataforma": "PC",
         "anio": 2015, "imagen": "witcher3.png"},

        {"id": 9, "titulo": "Call of Duty: Warzone", "genero": "Shooter",
         "plataforma": "PlayStation 4", "anio": 2020, "imagen": "warzone.jpg"},

        {"id": 10, "titulo": "Animal Crossing", "genero": "Simulación",
         "plataforma": "Nintendo Switch", "anio": 2020, "imagen": "animal_crossing.png"},

        {"id": 11, "titulo": "Resident Evil Village", "genero": "Horror",
         "plataforma": "PlayStation 4", "anio": 2021,
         "imagen": "resident_evil_village.png"},

        {"id": 12, "titulo": "God of War", "genero": "Acción",
         "plataforma": "PlayStation 4", "anio": 2018, "imagen": "god_of_war.jpg"}

    ]

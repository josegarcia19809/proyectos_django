from django.shortcuts import render

meetups = [
        {
            "title": "Python para Ciencia de Datos",
            "slug": "python-ciencia-datos",
            "city": "Ciudad de México",
            "date": "2026-02-10",
            "attendees": 45
        },
        {
            "title": "Introducción a Machine Learning",
            "slug": "introduccion-machine-learning",
            "city": "Guadalajara",
            "date": "2026-02-15",
            "attendees": 60
        },
        {
            "title": "Desarrollo Web con Django",
            "slug": "desarrollo-web-django",
            "city": "Monterrey",
            "date": "2026-02-20",
            "attendees": 38
        }
    ]

# Create your views here.
def index(request):
    return render(request, "meetups/index.html",{
        "show_meetups": True,
        "meetups": meetups
    })

def meetup_details(request, meetup_slug):
    return render(request, "meetups/meetup_details.html", {
        "meetup_slug": meetup_slug
    })
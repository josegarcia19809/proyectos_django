from django.urls import path

from . import views
urlpatterns = [
    path('january', views.january, name='january'),
    path('february', views.february, name='february'),
    path('march', views.march, name='march'),
    path('april', views.april, name='april'),
    path('may', views.may, name='may'),
    path('june', views.june, name='june'),
    path('july', views.july, name='july'),
    path('august', views.august, name='august'),
    path('september', views.september, name='september'),
    path('october', views.october, name='october'),
    path('november', views.november, name='november'),
    path('december', views.december, name='december'),
]
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='all-meetups'),
    path('<slug:meetup_slug>', views.meetup_details, name='meetup-details'),
]

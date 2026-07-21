from django.urls import path

from . import views

urlpatterns = [
    # path('', views.review, name='review'),
    path("", views.ReviewView.as_view()),
    path("agregar", views.ReviewView2.as_view()),
    path("agregar3", views.ReviewView3.as_view()),
    path('thank-you', views.ThankYouView.as_view(), name='thank_you'),
    path('reviews', views.ReviewsListView.as_view(), name='reviews'),
    path('reviews2', views.ReviewsListView2.as_view(), name='reviews2'),
    path('reviews/<int:id>', views.SingleReviewView.as_view(), name='reviews_id'),
    path('reviews2/<int:pk>', views.SingleReviewView2.as_view(), name='reviews_id2'),
]

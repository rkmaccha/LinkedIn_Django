from django.urls import path
from . import views

urlpatterns = [
    #path('',views.home),
    path('',views.HomeView.as_view()),
    path('auth/',views.AuthoriseView.as_view()),
]
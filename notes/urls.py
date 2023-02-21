from django.urls import path
from . import views

urlpatterns = [
    path('all',views.NotesListView.as_view(), name="notes.list"),
    path('all/<int:pk>',views.NotesDetailView.as_view(), name="notes.detail"),
]
from django.shortcuts import render
from .models import Notes
from django.http import Http404

from django.views.generic import ListView,DetailView
from .models import Notes

class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name ="notes/notes.html" 

# Create your views here.
# def list(request):
#     all_notes= Notes.objects.all()
#     return render(request,"notes/notes.html",{'notes' : all_notes})

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'
    template_name ="notes/notes_detail.html" 

# def details(request,pk):
#     try:
#         note= Notes.objects.get(pk = pk)
#         return render(request,"notes/notes_detail.html",{'note' : note})
#     except Notes.DoesNotExist:
#         raise Http404("Note doesnt exist")
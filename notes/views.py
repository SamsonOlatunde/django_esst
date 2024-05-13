from django.shortcuts import render
from notes.models import Note


def home_smart(request):
    allNote = Note.objects.all()
    return render(request, 'notes/note.html', {'notes': allNote})

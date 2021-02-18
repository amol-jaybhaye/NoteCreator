from django.contrib import admin
from .models import Note
from django import forms
from .forms import NoteAddForm

class NoteAdmin(admin.ModelAdmin):
     form = NoteAddForm
     list_display = ('title', 'user', 'note', 'link', 'date')
admin.site.register(Note, NoteAdmin)
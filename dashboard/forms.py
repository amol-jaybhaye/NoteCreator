from django import forms
from .models import Note

class NoteAddForm(forms.ModelForm):
     note = forms.CharField( widget=forms.Textarea(attrs={'cols':40, 'rows':20}))
     class Meta:
          model = Note
          fields = ('title', 'note', 'link')
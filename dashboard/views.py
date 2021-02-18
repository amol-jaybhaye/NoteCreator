from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Note
from .forms import NoteAddForm
from django.db.models import Q

@login_required(login_url='signin')
def dashboard(request):
     if request.method =="POST":
          form = NoteAddForm(request.POST)
          if form.is_valid():
               note = form.save(commit=False)
               note.user = request.user
               note.save()
               return redirect('dashboard')
     else:
          form = NoteAddForm()       

     notes = Note.objects.filter(user=request.user).order_by('-date')

     return render(request, "dashboard.html", {'form':form, 'notes':notes})

def search(request):
     if request.method == "GET":
          search = request.GET.get("search")
          if search is not None:
                search_result = Note.objects.filter(
                     Q(title__icontains=search)| Q(note__icontains=search),
                     user=request.user).order_by('-date') 
                return render(request, "search.html", {'search':search_result})
                
     return render(request, "search.html", {})
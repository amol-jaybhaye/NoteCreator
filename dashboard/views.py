from django.shortcuts import render,redirect, HttpResponse
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

@login_required(login_url='signin')
def search(request):
     if request.method == "GET":
          search = request.GET.get("search")
          if search is not None:
                search_result = Note.objects.filter(
                     Q(title__icontains=search)| Q(note__icontains=search),
                     user=request.user).order_by('-date') 
                return render(request, "search.html", {'search':search_result})
                
     return render(request, "search.html", {})

@login_required(login_url='signin')
def update(request, pk):
     note = Note.objects.get(id=pk)
     form = NoteAddForm(instance=note)
     if request.user == note.user:
          if request.method == 'POST':
               form = NoteAddForm(request.POST, instance=note)
               if form.is_valid():
                    form.save()
                    return redirect("dashboard")
          else:
               form = NoteAddForm(instance=note)
     else:
          return HttpResponse("404 -page doesn't exist")
     return render(request, "update.html", {'form':form})

@login_required(login_url='signin')
def delete(request, pk):
     note = Note.objects.get(id=pk)
     if request.user == note.user:
          if request.method == 'POST':    
               note.delete()
               return redirect("dashboard")
     else:
          return HttpResponse("404 -page doesn't exist")
     return render(request, "delete.html", {'note':note})

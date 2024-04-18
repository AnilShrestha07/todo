from pyexpat.errors import messages
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Todolist

from .forms import TodoForm

# Create your views here.
@login_required
def handle_todolist(request):
      
    todos = Todolist.objects.filter(user=request.user)
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            
            return redirect('/todolist')
    else:
        form = TodoForm()
        
    context = {'form': form, 
               'todos': todos
               }
    return render(request, 'todo.html', context)
 # todos = Todolist.objects.all()
    # if request.method == 'POST':
    #     title = request.POST.get('title')
    #     description = request.POST.get('description')
    #     todo = Todolist(title=title, description=description)
    #     todo.save()
    #     return redirect('/todolist')
    # else:
    #     form = TodoForm()
    # context = {'form': form, 'todos': todos}
    # return render(request, 'todo.html', context) 

def update(request, pk):
   
    todo = Todolist.objects.get(id=pk)
    # form = TodoForm()
    # if request.method == 'POST':
    #     title = request.POST.get('title')
    #     description = request.POST.get('description')
    #     todo = Todolist(title=title, description=description)
    #     todo.save()
    #     return redirect('/todolist')
    form = TodoForm(instance=todo)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('/todolist')
    
    context = {'form': form}
    return render(request, 'todo.html', context)

def delete(request,pk):
    todo = Todolist.objects.get(id=pk)
    todo.delete()
    return redirect('/todolist')
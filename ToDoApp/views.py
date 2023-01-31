from django.shortcuts import render, redirect
from .models import Todo
# Create your views here.

def index(request):
    todo = Todo.objects.all()
    context = {'todos': todo}

    if request.method == 'POST': 
        new_todo =Todo(
            title = request.POST['title']
        )
        new_todo.save()
        return redirect('/')      

    return render(request, 'index.html', context)

def delete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('/')
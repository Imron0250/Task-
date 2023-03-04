from django.shortcuts import render, redirect
from .models import *

def home(request):
    context = {
        'task' : Task.objects.all(),

    }
    return render(request, 'index.html', context)

def create_task(request):
    if request.method == "POST":
        task = request.POST.get('task')
        Task.objects.create(task=task)
        return redirect('home', )
    return redirect('home', )

def finish_task(request):
    if request.method == "POST":
        id = request.POST.get("id")
        print(id)
        t = Task.objects.get(id=id)
        if t.done:
            t.done = False
        else:
            t.done = True
        t.save()
        return redirect('home')
    return redirect('home')

def active(request):
    context = {
        'task' : Task.objects.filter(done=True)
    }
    return render(request, 'completed.html', context)


def completed(request):
    context = {
        'task' : Task.objects.filter(done=True)
    }    
    return render(request, 'active.html', context)

def controller(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        print(name)
        if int(name) == 1:
            return redirect('home')
        elif int(name) == 2:
            return redirect('completed')
        else: 
            return redirect('active')


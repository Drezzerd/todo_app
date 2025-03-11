from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Task
import subprocess

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user).order_by('-priority', 'completed', 'title')
    return render(request, 'todo/task_list.html', {'tasks': tasks})

@login_required
def add_task(request):
    if request.method == "POST":
        title = request.POST.get("title")
        priority = request.POST.get("priority", 2)  # Par défaut : Moyenne
        if title:
            Task.objects.create(title=title, priority=int(priority), user=request.user)
    return redirect("task_list")

def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect("task_list")

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect("task_list")

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'todo/register.html', {'form': form})

def home(request):
    return render(request, 'todo/home.html')

def run_tests(request):
    """Exécute les tests Django dans un sous-processus et affiche le résultat"""
    try:
        result = subprocess.run(
            ['python', 'manage.py', 'test', '-v', '2'],  # Lancer les tests avec verbosity=2
            capture_output=True,
            text=True
        )
        test_output = result.stdout + result.stderr  # Concatène stdout et stderr
    except Exception as e:
        test_output = f"Erreur lors de l'exécution des tests : {str(e)}"

    return render(request, 'todo/tests.html', {'test_output': test_output})
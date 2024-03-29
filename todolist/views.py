from django.http import HttpResponse
from django.shortcuts import redirect, render
from todolist.models import Todo
from django.views.decorators.http import require_http_methods

# Create your views here.

def index(request):
    todos = Todo.objects.all()
    return render(request, "base.html", {"todo_list": todos})
    # return HttpResponse("hello")

@require_http_methods(["POST"])
def add(request):
    title = request.POST["title"]
    todo = Todo(title=title)
    todo.save()
    return redirect("index")

def update(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.complete = not todo.complete
    todo.save()
    return redirect("index")

def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect("index")
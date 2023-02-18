import django.http
from django.core.handlers.asgi import ASGIRequest
from django.shortcuts import render

from apps.todo.models import Todo


def todo(request):
    todo_list = Todo.objects.all().order_by('-created_at')

    return render(
        request=request,
        template_name='todo_list.html',
        context={"todo_list": todo_list},
    )


def add_new_todo(request: ASGIRequest):
    data = request.POST
    todo_var = Todo()
    todo_var.name = data['name']
    todo_var.save()
    return django.shortcuts.redirect('todo')


def delete_todo(request: ASGIRequest, todo_id):
    todo_var = Todo.objects.get(pk=todo_id)
    todo_var.delete()
    return django.shortcuts.redirect('todo')


def clear_completed(request: ASGIRequest):
    pass


def change_status(request: ASGIRequest, todo_id):
    todo_var = Todo.objects.get(pk=todo_id)
    todo_var.checked = not bool(todo_var.checked)
    todo_var.save()
    return django.shortcuts.redirect('todo')

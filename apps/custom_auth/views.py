import django.http
from django.core.handlers.asgi import ASGIRequest
from django.shortcuts import render, redirect
from django.contrib.auth.backends import BaseBackend

from django.contrib.auth import authenticate, login

def auth(request: ASGIRequest):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if request.user.is_staff:
                return redirect('admin:index')
            else:
                return redirect
        else:
            return django.http.HttpResponseForbidden()

    if request.method == 'GET':
        return render(
            request=request,
            template_name='auth_page.html',
            context={"test": []},
    )


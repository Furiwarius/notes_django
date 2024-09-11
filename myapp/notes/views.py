from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .forms import RegisterForm, LoginForm



def home(request:HttpRequest):
    '''
    Начальная страница
    '''
    return render(request, "notes/index.html")



def user_login(request:HttpRequest):
    '''
    Аутентификация
    '''

    if request.method == "POST":

        user = authenticate(request=request, 
                             username=request.POST["username"], 
                             password=request.POST["password"])
           
        if user is not None:
            # В случае удачи переадресуем на страницу с заметками пользователя
            login(request=request, user=user)

            return redirect("notes")
    
    else:
        return render(request, "notes/login.html", {"form": LoginForm()})



def user_logout(request:HttpRequest):
    '''
    Выход пользователя из аккаунта
    
    При выходе происходит переадресация на главную страницу
    '''
    logout(request)

    return render(request, "notes/index.html")



def user_register(request:HttpRequest):
    '''
    Регистрация пользователя
    '''

    if request.method == 'POST':
        user_form = RegisterForm(request.POST)

        if user_form.is_valid():
            # Создайте новый объект пользователя, но пока не сохраняйте его.
            new_user: User = user_form.save(commit=False)
            # Установите выбранный пароль
            new_user.set_password(user_form.cleaned_data['password'])
            # Сохраните объект пользователя.
            new_user.save()

            return render(request, 'notes/register_done.html')
    else:
        user_form = RegisterForm()

    return render(request, 'notes/register.html', {'user_form': user_form})
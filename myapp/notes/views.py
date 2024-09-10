from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth import aauthenticate, login, logout

from .forms import RegisterForm, LoginForm



def user_login(request:HttpRequest):
    '''
    Аутентификация
    '''

    if request.method == "POST":

        user = aauthenticate(request=request, 
                             username=request.POST["username"], 
                             password=request.POST["password"])
           
        if user is not None:
            # В случае удачи переадресуем на страницу с заметками пользователя
            login(request=request, user=user)

            return redirect("notes")
    
    else:
        return render(request, "login.html", {"form": LoginForm()})



def user_logout(request:HttpRequest):
    '''
    Выход пользователя из аккаунта
    
    При выходе происходит переадресация на главную страницу
    '''
    logout(request)

    return render(request, "index.html")



def user_register(request:HttpRequest):
    '''
    Регистрация пользователя
    '''

    if request.method == "POST":
        # Производим манипуляции с данными

        # В случае удачи переадресуем на страницу авторизации
        if True:
            return redirect("login")
    
    else:
        return render(request, "register.html", {"form": RegisterForm()})
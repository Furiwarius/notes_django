from django import forms



class RegisterForm(forms.Form):
    '''
    Класс формы для регистрации
    '''
    username = forms.CharField()
    password = forms.IntegerField()



class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.IntegerField()
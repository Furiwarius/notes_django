from django import forms
from django.contrib.auth.models import User



class LoginForm(forms.Form):
    username = forms.CharField(label="Логин", min_length=6, max_length=20)
    password = forms.CharField(label="Пароль", max_length=20)



class RegisterForm(forms.ModelForm):
    '''
    Форма для регистрации
    '''

    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ('username', 'first_name',)


    def clean_password2(self) -> str:
        '''
        Сравнение дубликата пароля на совпадение
        '''
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают.')
        return cd['password2']



class NoteForm(forms.Form):
    '''
    Форма для новой заметки
    '''
    name = forms.CharField(label="Название заметки", min_length=2, max_length=20)
    text = forms.CharField(label="Содержимое заметки", widget=forms.Textarea)
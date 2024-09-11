from django.db import models
from django.contrib.auth.models import User



class Notes(models.Model):
    '''
    Модель таблицы для хранения аккаунтов
    '''

    # Название заметки
    name = models.CharField(max_length=20)
    # Содержание заметки
    text = models.TextField()
    # Дата создания
    create = models.DateTimeField(auto_now_add=True)
    # Дата обновления
    update = models.DateTimeField(auto_now=True)
    # автор заметок
    author = models.ForeignKey(User, on_delete=models.CASCADE)
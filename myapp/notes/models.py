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
    create = models.DateTimeField()
    # Дата обновления
    update = models.DateTimeField()
    # автор заметок
    author = models.ForeignKey(User, on_delete=models.CASCADE)
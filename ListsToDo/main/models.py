from django.db import models


class List(models.Model):
    title = models.CharField('Название списка', max_length=50)
    list = models.TextField('Список')

    def __str__(self):
        return self.title

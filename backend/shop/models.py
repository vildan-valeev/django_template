from django.db import models


class Item(models.Model):
    title = models.CharField(max_length=100, )
    created = models.DateTimeField(verbose_name='Создан')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Запись'
        verbose_name = 'Записи'
        ordering = ['id']

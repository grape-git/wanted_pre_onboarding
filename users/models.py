from django.db import models

# Create your models here.
from core.models import HistoryModel


class User(HistoryModel):
    name = models.CharField(
        verbose_name='이름',
        max_length=100
    )

    class Meta:
        db_table = 'user_tb'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'

    def __str__(self):
        return f'{self.name}'

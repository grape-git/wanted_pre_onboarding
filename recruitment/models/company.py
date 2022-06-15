from core.models import HistoryModel
from django.db import models


class Company(HistoryModel):
    name = models.CharField(
        max_length=100,
        verbose_name='회사이름'
    )

    nation = models.CharField(
        max_length=100,
        verbose_name='국가이름'
    )

    area = models.CharField(
        max_length=100,
        verbose_name='지역'
    )

    class Meta:
        db_table = 'company_tb'
        verbose_name = '회사'
        verbose_name_plural = '회사'

    def __str__(self):
        return f'{self.name}'

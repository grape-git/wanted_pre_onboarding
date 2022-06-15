from core.models import HistoryModel
from django.db import models


class JobOpening(HistoryModel):
    company = models.ForeignKey(
        verbose_name='회사',
        to='recruitment.Company',
        on_delete=models.CASCADE,
        related_name='%(class)s_company'
    )

    position = models.CharField(
        verbose_name='포지션',
        max_length=100
    )

    compensation = models.PositiveIntegerField(
        verbose_name='채용 보상금',
        default=0
    )

    content = models.TextField(
        verbose_name='채용 내용'
    )

    skill = models.TextField(
        verbose_name='사용 기술'
    )

    class Meta:
        db_table = 'job_opening_tb'
        verbose_name = '채용공고'
        verbose_name_plural = '채용공고'

    def __str__(self):
        return f'{self.company.name}'

from core.models import HistoryModel
from django.db import models


class SupportDetail(HistoryModel):
    job_opening = models.ForeignKey(
        verbose_name='채용공고',
        to='recruitment.JobOpening',
        on_delete=models.CASCADE,
        related_name='%(class)s_job_opening'
    )

    users = models.ForeignKey(
        verbose_name='사용자',
        to='users.User',
        on_delete=models.CASCADE,
        related_name='%(class)s_users'
    )

    class Meta:
        db_table = 'support_detail_tb'
        verbose_name = '지원내역'
        verbose_name_plural = '지원내역'

    def __str__(self):
        return f'{self.job_opening.company.name}/{self.users.name}'

from django.db import models


# Create your models here.


class HistoryModel(models.Model):
    created_at = models.DateTimeField(
        verbose_name='생성일',
        auto_now_add=True,
        editable=False,
        blank=True,
        help_text='데이터가 생성된 일자입니다.',
    )

    updated_at = models.DateTimeField(
        verbose_name='수정일',
        auto_now=True,
        editable=False,
        blank=True,
        null=True,
        help_text='데이터를 수정한 일자입니다.',
    )

    class Meta:
        abstract = True

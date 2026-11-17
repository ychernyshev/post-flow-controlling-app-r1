from django.conf import settings
from django.db import models

class RecipientStreetModel(models.Model):
    street = models.CharField(
        max_length=100,
        unique=True,
        db_index=True,
        verbose_name='Street'
    )

    def __str__(self):
        return f'Street: {self.street}'

    class Meta:
        ordering = ['street']
        verbose_name = 'recipient street'
        verbose_name_plural = 'Recipient streets'

class PostageModel(models.Model):
    track_number = models.CharField(
        max_length=13,
        unique=True,
        db_index=True,
        verbose_name='Track number'
    )
    recipient_street = models.ForeignKey(
        RecipientStreetModel,
        db_index=True,
        on_delete=models.PROTECT,
        verbose_name='Recipient street')
    delivered_date = models.DateTimeField(
        verbose_name='Delivered date'
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        verbose_name='Created by (Operator)'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Log timestamp'
    )

    def __str__(self):
        return f'{self.track_number} -> {self.recipient_street}'

    class Meta:
        ordering = ['-delivered_date']
        verbose_name = 'postage item'
        verbose_name_plural = 'Postage items'

from django.db import models

class Payload(models.Model):

    head = models.CharField(max_length=64)
    body = models.CharField(max_length=256)
    icon = models.CharField(max_length=256)
    url = models.CharField(max_length=256)

    class Meta:
        verbose_name = 'Payload'
        verbose_name_plural = 'Payloads'

    def __str__(self):
        return self.name

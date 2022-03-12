from django.db import models

# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=14)
    email = models.EmailField()
    message = models.TextField()

    class Meta(object):
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return f'{self.name}'

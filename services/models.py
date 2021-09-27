from django.db import models

# Create your models here.
class ServiceComputer (models.Model):
    name = models.CharField (max_length=200, verbose_name= 'Заголовок', blank=True,)
    description = models.TextField (verbose_name='Описание', blank=True, )
    date = models.DateTimeField (verbose_name='Дата',)

    def __unicode__(self):
        return self.name

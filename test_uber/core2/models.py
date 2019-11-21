from django.db import models


class Test_model1(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Название'
    )
    count = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='Описание'
    )

    def __str__(self):
        return "%s. %s" % (self.id, self.name)

    class Meta:
        verbose_name_plural = 'TEST1'
        verbose_name = 'Test1'
    # Create your models here.

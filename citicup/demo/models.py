from operator import mod
from tabnanny import verbose
from django.db import models

# Create your models here.
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20,verbose_name='name')
    bpub_data = models.DateField(verbose_name='pub date')
    bread = models.IntegerField(default=0, verbose_name='read num')
    bcomment = models.IntegerField(default=0, verbose_name='comment num')
    is_delete = models.BooleanField(default=False, verbose_name='deleted')

    class Meta:
        db_table = 'tb_books'
        verbose_name = 'book'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.btitle


from django.db import models

from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Titlul')
    content = models.TextField(max_length=1500, verbose_name='Contentul')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data-postarii')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data-editarii')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Pozele', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Confirmarea-publicarii')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Denumirea catogoriilor')
    views = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('view_news', kwargs={"pk": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Știri'
        verbose_name_plural = 'Stirile'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Denumirea catogoriilor')

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categoriile'
        ordering = ['title']

# Create your models here.

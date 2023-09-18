from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    def str(self):
        return self.name


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    teg = models.ManyToManyField(Tag, verbose_name='Тег', related_name='tags', blank=True, through='scope')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def str(self):
        return self.title


class Scope(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name='Раздел')

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тематика'

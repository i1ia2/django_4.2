from django.db import models

class Tag(models.Model):
    name = models.ManyToManyField('Article', related_name='tegs')

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
    tags = models.ManyToManyField(Tag, related_name='articles')

    #scopes

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def str(self):
        return self.title


class Scope(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, default=None,  related_name='scopes')

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тематика'

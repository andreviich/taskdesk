import datetime
from django.db import models
from django.utils import timezone
# Create your models here.
class Article(models.Model):
    article_title = models.CharField('Название статьи', max_length=300)
    article_text = models.TextField('Текст статьи')
    pub_date = models.DateTimeField('Дата публикации')
    def __str__(self):
        return self.article_title
    def wasPublishedRecently(self):
        return self.pub_date >= (timezone.now()-datetime.timedelta(days=7))
    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField('Имя комментаторы', max_length=300)
    comment_text = models.TextField('Текст комментария')
    def __str__(self):
        return self.author_name
    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

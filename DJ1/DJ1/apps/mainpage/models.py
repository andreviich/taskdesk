from django.db import models

class MainSection(models.Model):
    def __str__(self):
        return self.article_title
    class Meta:
        verbose_name = "Главная"
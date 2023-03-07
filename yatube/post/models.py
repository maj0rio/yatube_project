from django.contrib.auth import get_user_model
from django.db import models
from datetime import datetime


User = get_user_model()


class Post(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    text = models.TextField('Текст')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    date = models.DateTimeField('Дата публикации',default=datetime.now, blank=True)
    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.title


from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from likes.models import Like
from django.utils import timezone
import pytz


User = get_user_model()


class Post(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    text = models.TextField('Текст')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    date = models.DateTimeField('Дата публикации', default=timezone.now, blank=True)

    likes = GenericRelation(Like)

    def save(self, *args, **kwargs):
        if not self.date.tzinfo:
            self.date = timezone.localtime(self.date, pytz.timezone('Europe/Moscow'))
        super().save(*args, **kwargs)


    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.title

    @property
    def total_likes(self):
        return self.likes.count()





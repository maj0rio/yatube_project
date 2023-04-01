from django.db import models
from users.models import CustomUser
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

User = get_user_model()


class Like(models.Model):

    user = models.ForeignKey(CustomUser,
                             related_name='likes',
                             on_delete=models.CASCADE,
                             )

    content_type = models.ForeignKey(ContentType,
                                     on_delete=models.CASCADE,
                                     )

    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')










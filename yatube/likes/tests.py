from django.contrib.contenttypes.models import ContentType
from post.models import Post
from likes.models import Like

from django.contrib.auth import get_user_model

User = get_user_model()

user = User.objects.create_user(email='ttttt@tt.ru', password='12345')
post = Post.objects.create(title='Урок', author=user, text='BLBLBLBLBLBLBLLBLBLBLBLBL')

# Create your tests here.

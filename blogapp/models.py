from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    avatar = models.ImageField(upload_to="user/avatar/")

    def __str__(self):
        return self.username


class Category(models.Model):
    category_name = models.CharField(verbose_name='Category name', max_length=50)

    def __str__(self):
        return self.category_name


class Comments(models.Model):
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.PROTECT)
    post = models.ForeignKey('Post', verbose_name='Comments', on_delete=models.CASCADE)
    message = models.TextField(verbose_name='Comments')
    best_comment = models.BooleanField(verbose_name='Best Comment', default=False)
    created = models.DateTimeField(verbose_name='Created', auto_now_add=True)

    def __str__(self):
        return self.message[:20]


class Post(models.Model):
    title = models.CharField(verbose_name='Title', max_length=200)
    content = models.TextField(verbose_name='Content')
    category = models.ManyToManyField(Category, verbose_name='Category')
    image = models.ImageField(verbose_name='Image', upload_to='blog/')
    likes = models.IntegerField(verbose_name='Likes', default=0)
    created = models.DateTimeField(verbose_name='Created', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Updated', auto_now=True)

    def __str__(self):
        return self.title

    def get_absolut_url(self) -> object:
        return reverse('single-blog', kwargs={'pk': str(self.pk)})


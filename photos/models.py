from django.db import models
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
#from jsonfield import JSONField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Photo(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30,  null=True, blank=True, default='')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, default='')
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        default = None,
        on_delete=models.CASCADE,
    )


    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('photo', args=[str(self.id)])



class Comment(models.Model):
    photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    email = models.CharField(max_length=100)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        default=1
    )
    comment = models.TextField(default=False)
    body = models.TextField(default=False)
    url = models.TextField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    

    class meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.author)


    def get_absolute_url(self):
        return reverse('photo')


    
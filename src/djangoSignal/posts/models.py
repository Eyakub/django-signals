from django.db import models
from django.db.models.signals import post_save, pre_save, post_delete


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 50)

    def __str__(self):
        return self.title


def save_post(sender, instance, **kwargs):
    print('something from save_post using post_save signals')


def after_delete_post(sender, instance, **kwargs):
    print('you deleted something')


pre_save.connect(save_post, sender=Post)
post_save.connect(save_post, sender=Post)
post_delete.connect(after_delete_post, sender=Post)
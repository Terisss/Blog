from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from article.models import Article
from django.utils import timezone
import datetime
# Create your models here.


class Comments(models.Model):
    body = models.TextField(max_length=2000)
    author = models.ForeignKey(User, blank=True)
    article = models.ForeignKey(Article)
    enable = models.BooleanField(default=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    patch_date = models.DateTimeField(auto_now=True)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(minutes=30)

    def __unicode__(self):
        return "Comment to %s" % self.article.title

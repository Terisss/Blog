#-*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length = 100, unique = True)
	parent_category = models.ForeignKey('self', blank = True, null = True)
	def __unicode__(self):
		return self.name


class Article(models.Model):
	title = models.CharField(max_length = 100)
	body = models.TextField()
	pub_date = models.DateTimeField(auto_now_add = True)
	patch_date = models.DateTimeField(auto_now = True)
	category = models.ForeignKey(Category)
	is_active = models.BooleanField(default = False)
	def __unicode__(self):
		return self.title



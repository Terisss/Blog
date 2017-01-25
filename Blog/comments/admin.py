from django.contrib import admin

from .models import Comments
# Register your models here.


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('article', 'author', 'pub_date', 'enable', 'was_published_recently')
    list_filter = ['article', 'pub_date', 'enable']

admin.site.register(Comments, CommentsAdmin)

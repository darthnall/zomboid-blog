from django.contrib import admin

from . import models


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(models.BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    pass

from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth import get_user_model


class Post(models.Model):
    """Blog post."""

    user = models.ForeignKey(
        get_user_model(), on_delete=models.PROTECT, related_name="posts"
    )
    title = models.CharField(max_length=64)
    subtitle = models.CharField(blank=True, max_length=128)
    desc = models.TextField(blank=True, max_length=2048)
    slug = models.SlugField(blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    mod_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    def save(self, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(**kwargs)

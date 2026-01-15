from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class BlogPost(models.Model):
    """Blog post."""

    class BlogPostStatus(models.TextChoices):
        PUBLIC = "public", _("Public")
        PRIVATE = "private", _("Private")
        HIDDEN = "hidden", _("Hidden")

    user = models.ForeignKey(
        get_user_model(), on_delete=models.PROTECT, related_name="posts"
    )
    title = models.CharField(max_length=64)
    subtitle = models.CharField(blank=True, max_length=128)
    content = models.TextField(blank=True)
    slug = models.SlugField(blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    mod_date = models.DateTimeField(auto_now=True)
    status = models.CharField(
        choices=BlogPostStatus.choices, default=BlogPostStatus.HIDDEN
    )

    def __str__(self) -> str:
        return self.title

    def save(self, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(**kwargs)

    def get_absolute_url(self) -> str:
        return reverse(
            "blogpost detail", kwargs={"pk": self.pk, "slug": self.slug}
        )

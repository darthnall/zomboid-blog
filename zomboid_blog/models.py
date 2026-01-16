from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Author(models.Model):
    """Battle-hardened Kentuckian survior."""

    name = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.name


class BlogPost(models.Model):
    """Blog post."""

    class BlogPostStatus(models.TextChoices):
        PUBLIC = "public", _("Public")
        PRIVATE = "private", _("Private")
        HIDDEN = "hidden", _("Hidden")

    author = models.ForeignKey(
        "zomboid_blog.Author", on_delete=models.CASCADE, related_name="posts"
    )
    title = models.CharField(max_length=64)
    subtitle = models.CharField(blank=True, max_length=128)
    content = models.TextField(blank=True)
    slug = models.SlugField(blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    mod_date = models.DateTimeField(auto_now=True)
    status = models.CharField(
        choices=BlogPostStatus.choices, default=BlogPostStatus.PUBLIC
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

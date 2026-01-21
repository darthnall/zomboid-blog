from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Moodle(models.TextChoices):
    ANGRY = "Angry", _("Angry")
    BORED = "Bored", _("Bored")
    CONCENTRATING = "Concentrating", _("Concentrating")
    DEAD = "Dead", _("Dead")
    DISCOMFORT = "Discomfort", _("Discomfort")
    DIZZY = "Dizzy", _("Dizzy")
    DRUNK = "Drunk", _("Drunk")
    EXHAUSTED = "Exhausted", _("Exhausted")
    HAPPY = "Happy", _("Happy")
    HUNGOVER = "Hungover", _("Hungover")
    ILL = "Ill", _("Ill")
    NAUSEOUS = "Nauseous", _("Nauseous")
    NOXIOUS_SMELL = "NoxiousSmell", _("Noxious Smell")
    PAINED = "Pained", _("Pained")
    PANICKED = "Panicked", _("Panicked")
    SAD = "Sad", _("Sad")
    SCARED = "Scared", _("Scared")
    SLEEPY = "Sleepy", _("Sleepy")
    STRESSED = "Stressed", _("Stressed")
    ZOMBIFIED = "Zombified", _("Zombified")


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
    mood = models.CharField(choices=Moodle.choices, default=Moodle.BORED)
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

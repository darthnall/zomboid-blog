from django.views.generic import DetailView, ListView
from django.db.models import QuerySet

from . import models, mixins

PUBLIC = models.BlogPost.BlogPostStatus.PUBLIC


class BlogPostDetailView(mixins.HtmxTemplateResponseMixin, DetailView):
    content_type = "text/html"
    http_method_names = ["get"]
    model = models.BlogPost
    queryset = models.BlogPost.objects.filter(status=PUBLIC)


class BlogPostListView(mixins.HtmxTemplateResponseMixin, ListView):
    allow_empty = True
    content_type = "text/html"
    http_method_names = ["get"]
    model = models.BlogPost
    ordering = "-pub_date"
    paginate_by = 50
    queryset = models.BlogPost.objects.filter(status=PUBLIC)

    def get_queryset(self) -> QuerySet:
        qs = super().get_queryset()
        return qs

from django.views.generic import DetailView, ListView, TemplateView
from django.db.models import QuerySet

from . import mixins, models

PUBLIC = models.BlogPost.BlogPostStatus.PUBLIC


class HomeView(mixins.HtmxTemplateResponseMixin, TemplateView):
    content_type = "text/html"
    http_method_names = ["get"]
    template_name = "zomboid_blog/home.html"


class BlogPostDetailView(mixins.HtmxTemplateResponseMixin, DetailView):
    content_type = "text/html"
    http_method_names = ["get"]
    model = models.BlogPost
    queryset = models.BlogPost.objects.filter(status=PUBLIC)
    template_name = "zomboid_blog/blogpost/detail.html"


class BlogPostListView(mixins.HtmxTemplateResponseMixin, ListView):
    allow_empty = True
    content_type = "text/html"
    http_method_names = ["get"]
    model = models.BlogPost
    ordering = "-pub_date"
    paginate_by = 50
    queryset = models.BlogPost.objects.filter(status=PUBLIC)
    template_name = "zomboid_blog/blogpost/list.html"

    def get_queryset(self) -> QuerySet:
        qs = super().get_queryset()
        return qs

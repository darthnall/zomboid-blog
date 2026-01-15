from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateResponseMixin

from . import models


class HtmxTemplateResponseMixin(TemplateResponseMixin):
    partial_template_name = None

    def render_to_response(self, context, **response_kwargs):
        htmx_request = self.request.headers.get("HX-Request")
        boosted = self.request.headers.get("HX-Boosted")

        if htmx_request and not boosted:
            self.template_name = (
                self.partial_template_name
                if self.partial_template_name is not None
                else f"{self.template_name}#partial"
            )
        return super().render_to_response(context, **response_kwargs)


class BlogPostDetailView(HtmxTemplateResponseMixin, DetailView):
    content_type = "text/html"
    http_method_names = ["get"]
    model = models.BlogPost
    queryset = models.BlogPost.objects.filter(status="public")


class BlogPostListView(HtmxTemplateResponseMixin, ListView):
    allow_empty = True
    content_type = "text/html"
    http_method_names = ["get"]
    model = models.BlogPost
    ordering = "-pub_date"
    paginate_by = 50
    queryset = models.BlogPost.objects.filter(status="public")

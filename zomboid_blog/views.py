from django.views.generic import DetailView


class PostDetailView(DetailView):
    content_type = "text/html"
    http_method_names = ["get"]
    template_name = "zomboid_blog/posts/detail.html"

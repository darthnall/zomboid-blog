from django.views.generic.base import TemplateResponseMixin


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

from django.urls import path

from . import views

urlpatterns = [
    path("", views.BlogPostListView.as_view(), name="blogpost list"),
    path(
        "posts/<str:slug>-<int:pk>/",
        views.BlogPostDetailView.as_view(),
        name="blogpost detail",
    ),
]

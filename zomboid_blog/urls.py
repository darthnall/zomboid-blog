from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path(
        "posts/list/", views.BlogPostListView.as_view(), name="blogpost list"
    ),
    path(
        "posts/<str:slug>-<int:pk>/",
        views.BlogPostDetailView.as_view(),
        name="blogpost detail",
    ),
]

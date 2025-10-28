from django.urls import path
from . import views


urlpatterns = [
    path("posts/", views.PostsListCreate.as_view(), name="blog-post-view")
]

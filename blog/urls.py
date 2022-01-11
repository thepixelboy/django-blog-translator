from django.urls import path

from . import views

urlpatterns = [
    path("<slug:slug>", views.BlogView.as_view(), name="blog_view"),
    path("", views.HomeView.as_view(), name="home_view"),
]

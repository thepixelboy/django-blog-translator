from django.urls import path

from . import views

urlpatterns = [path("<slug:slug>", views.BlogView.as_view(), name="blog_view")]
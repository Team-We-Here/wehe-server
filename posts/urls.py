from django.urls import path

from blogs.views import PostView

urlpatterns = [path("", PostView.as_view())]

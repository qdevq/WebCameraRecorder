from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("upload_video", views.upload_video, name="upload_video"),
    path("last_video", views.last_video, name="last_video"),
]

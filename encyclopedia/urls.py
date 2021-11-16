from django.urls import path

from . import views

import encyclopedia

app_name = "encyclopedia"

urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.create, name="create"),
    path("random", views.random, name="random"),
    path("edit/", views.edit, name="edit"),
    path("wiki/<str:title>", views.article, name="article")
]

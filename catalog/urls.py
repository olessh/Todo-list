from django.urls import path
from .views import (
    TaskListView,
    TagListView,
    TaskCreateView,
    TagCreateView,
    TaskToggleView,
    TaskUpdateView,
    TaskDeleteView,
    TagUpdateView,
    TagDeleteView,
)

app_name = "catalog"

urlpatterns = [
    path("", TaskListView.as_view(), name="home"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("tag/create/", TagCreateView.as_view(), name="tag-create"),
    path("task/<int:pk>/toggle/", TaskToggleView.as_view(), name="task-toggle"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("tag/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tag/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
]

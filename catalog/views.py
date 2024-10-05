from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import TaskCreateForm, TaskUpdateForm, TagForm
from .models import Task, Tag


class TaskListView(ListView):
    model = Task
    template_name = "catalog/task_list.html"
    context_object_name = "tasks"
    ordering = [
        "is_done",
        "-created_at",
    ]
    paginate_by = 10


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskCreateForm
    template_name = "catalog/task_form.html"
    success_url = reverse_lazy(
        "catalog:home"
    )


class TaskToggleView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_done = not task.is_done
        task.save()
        return redirect("catalog:home")


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskUpdateForm
    template_name = "catalog/task_form.html"
    success_url = reverse_lazy("catalog:home")


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "catalog/task_confirm_delete.html"
    success_url = reverse_lazy("catalog:home")


class TagListView(ListView):
    model = Tag
    template_name = "catalog/tag_list.html"
    context_object_name = "tags"
    paginate_by = 10


class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    template_name = "catalog/tag_form.html"
    success_url = reverse_lazy(
        "catalog:tag-list"
    )


class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    template_name = "catalog/tag_form.html"
    success_url = reverse_lazy("catalog:tag-list")


class TagDeleteView(DeleteView):
    model = Tag
    template_name = "catalog/tag_confirm_delete.html"
    success_url = reverse_lazy("catalog:tag-list")

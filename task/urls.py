from django.urls import path
from .views import TaskView

urlpatterns = [
    path('task/', TaskView.as_view(), name="task"),
    path('task/<int:pk>/', TaskView.as_view(), name="task_with_id")
]
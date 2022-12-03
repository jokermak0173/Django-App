from django.urls import path

from .views import TaskAPIView, TaskDetailAPIView, GetTasksByUserIdView

urlpatterns = [
    path('', TaskAPIView.as_view()),
    path('<int:pk>', TaskDetailAPIView.as_view()),
    path('by-user', GetTasksByUserIdView.as_view()),
]
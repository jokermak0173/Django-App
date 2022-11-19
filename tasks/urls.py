from django.urls import path

from .views import TaskAPIView, TaskDetailAPIView

urlpatterns = [
    path('', TaskAPIView.as_view()),
    path('<int:pk>', TaskDetailAPIView.as_view())
]
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from .models import Task
from .serializers import TaskSerializer

class TaskAPIView(APIView):
    serializer_class = TaskSerializer
    
    def get(self, request):
        tasks = Task.objects.all()
        tasks_serializer = self.serializer_class(tasks, many=True)
        return Response(tasks_serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request):
        task_serializer = self.serializer_class(data=request.data)

        if task_serializer.is_valid():
            message = "Task successfully created"
            task_serializer.save()
            return Response({'message': message}, 
                            status=status.HTTP_201_CREATED)
        else:
            return Response(
                task_serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
            
class TaskDetailAPIView(APIView):
    
    serializer_class = TaskSerializer
    
    def get(self, request, pk):
        task = get_object_or_404(Task, id=pk)
        task_serializer = self.serializer_class(task)
        return Response(task_serializer.data, status=status.HTTP_200_OK)
    
    def patch(self, request, pk):
        task = get_object_or_404(Task, id=pk)
        task_serializer = self.serializer_class(task, data=request.data)
        if task_serializer.is_valid():
            task_serializer.save()
            return Response(task_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                task_serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def delete(self, request, pk):
        task = get_object_or_404(Task, id=pk)
        task.delete()
        message = 'Tarea eliminada correctamente'
        return Response(
                {'message': message}, 
                status = status.HTTP_200_OK
        )

class GetTasksByUserIdView(generics.ListAPIView):
    serializer_class = TaskSerializer
    
    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        queryset = Task.objects.filter(user = user_id)
        return queryset
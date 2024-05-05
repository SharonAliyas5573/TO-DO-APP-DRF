from rest_framework import viewsets
from .models import Task
from auth.models import User
from rest_framework.exceptions import ValidationError
from .serializers import TaskSerializer
from auth.authenticate import JwtTokensAuthentication
from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response
from django.utils.timezone import make_aware

class TaskViewSet(viewsets.ModelViewSet):
    
    serializer_class = TaskSerializer
    authentication_classes = [JwtTokensAuthentication]
    
    def get_queryset(self):
        queryset = Task.objects.filter(user=self.request.user["user_id"])
        status = self.request.query_params.get('status', None)
        priority = self.request.query_params.get('priority', None)
        if status is not None:
            if status == 'completed':
                queryset = queryset.filter(completed=True)
            elif status == 'expired':
                queryset = queryset.filter(deadline__lt=timezone.now())
            elif status == 'active':
                queryset = queryset.filter(completed=False, deadline__gte=timezone.now())
        if priority is not None:
            priorities = priority.split(',')
            queryset = queryset.filter(priority__in=priorities)

        return queryset.order_by('-deadline')

    def perform_create(self, serializer):
        User_obj = User.objects.get(id=self.request.user["user_id"])
        serializer.save(user=User_obj)
        
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.deadline < timezone.now():
            raise ValidationError('Cannot edit an expired task')
        serializer = self.get_serializer(instance, data=request.data, partial=True)  # Set `partial=True` to make all fields optional
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': 'Task deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()
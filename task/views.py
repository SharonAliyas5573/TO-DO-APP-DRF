from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from auth.authenticate import JwtTokensAuthentication
from django.utils import timezone

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = [JwtTokensAuthentication]

    def get_queryset(self):
        queryset = Task.objects.filter(user=self.request.user)
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
            queryset = queryset.filter(priority=priority)

        return queryset.order_by('deadline')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
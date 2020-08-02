from rest_framework import viewsets
from .models import Dashboard
from .serializers import DashboardSerializer

class DashboardViewset(viewsets.ModelViewSet):
    serializer_class = DashboardSerializer
    queryset = Dashboard.objects.all()
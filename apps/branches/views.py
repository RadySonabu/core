from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from apps.branches.api import BranchSerializer
from apps.branches.models import Branch


# Create your views here.
class BranchViewset(ModelViewSet):
    model = Branch
    serializer_class = BranchSerializer
    queryset = Branch.objects.all()

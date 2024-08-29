from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.branches.views import BranchViewset

rides_router = DefaultRouter()
rides_router.register(r"branch", BranchViewset, "branch")

urlpatterns = [
    path("api/branch/", include(rides_router.urls)),
]

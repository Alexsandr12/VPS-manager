from django.urls import path, include
from rest_framework import routers

from .views import VpsViewSet

router = routers.DefaultRouter()
router.register("vps", VpsViewSet, basename="vps")

app_name = "api_vps_crud"
urlpatterns = [
    path('', include(router.urls))
]

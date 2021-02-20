from django.urls import path, include
from rest_framework import routers

from .views import DocumentoViewSet

router = routers.DefaultRouter()
router.register(r'docs', DocumentoViewSet)

urlpatterns = [
    path('', include(router.urls))
]
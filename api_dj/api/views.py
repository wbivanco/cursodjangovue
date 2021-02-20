from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Documento

from .serializer import DocuemntoSerializer


class DocumentoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Documento.objects.all().order_by('id')
    serializer_class = DocuemntoSerializer

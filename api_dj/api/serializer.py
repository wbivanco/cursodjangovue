from rest_framework import serializers

from .models import Documento


class DocuemntoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documento
        fields = '__all__'

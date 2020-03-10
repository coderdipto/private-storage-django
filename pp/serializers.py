from rest_framework import serializers

from pp.models import PrivateFile, PrivateFile2


class PrivateFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivateFile
        fields = "__all__"


class PrivateFile2Serializer(serializers.ModelSerializer):
    class Meta:
        model = PrivateFile2
        fields = "__all__"

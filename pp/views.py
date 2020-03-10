from private_storage.views import PrivateStorageDetailView
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from pp.models import PrivateFile, PrivateFile2
from pp.serializers import PrivateFileSerializer, PrivateFile2Serializer


class MyDocumentDownloadView(PrivateStorageDetailView):
    model = PrivateFile
    model_file_field = 'file'

    def get_queryset(self):
        # Make sure only certain objects can be accessed.
        return super().get_queryset()

    def can_access_file(self, private_file):
        # When the object can be accessed, the file may be downloaded.
        # This overrides PRIVATE_STORAGE_AUTH_FUNCTION
        return True


class PrivateFileViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny, ]
    serializer_class = PrivateFileSerializer
    queryset = PrivateFile.objects.all()


class PrivateFileViewSet2(viewsets.ModelViewSet):
    permission_classes = [AllowAny, ]
    serializer_class = PrivateFile2Serializer
    queryset = PrivateFile2.objects.all()

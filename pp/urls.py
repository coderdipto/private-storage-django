from django.urls import path, include
from pp import views
from rest_framework import routers

from pp.views import PrivateFileViewSet, PrivateFileViewSet2

router = routers.DefaultRouter()

router.register(r'private', PrivateFileViewSet)
router.register(r'private2', PrivateFileViewSet2)

app_name = 'pp'

urlpatterns = [
    path('secret-file/<int:pk>/', views.MyDocumentDownloadView.as_view()),
    path('', include(router.urls))
]

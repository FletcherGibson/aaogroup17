from django.conf.urls import include, url
from rest_framework import routers

from . import views

router = routers.DefaultRouter()

router.register('RemoteImagingMicroService', views.CutoutQueryView)

urlpatterns = [
    url(r'^', include(router.urls))
]

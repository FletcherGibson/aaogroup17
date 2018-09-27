from django.conf.urls import include, url
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register('CutoutQuery', views.CutoutQueryView)

urlpatterns = [
    url('', include(router.urls))
]

from django.conf.urls import url
from django.urls import path, include
from .views import SignUpView , AlphaVantageServiceViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'api', AlphaVantageServiceViewSet, basename='api')

urlpatterns = [
    path('register', SignUpView.as_view()),
    path('', include(router.urls)),
]
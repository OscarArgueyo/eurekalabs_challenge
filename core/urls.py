from django.conf.urls import url
from django.urls import path, include
from .views import SignUpView , AlphaVantageServiceViewSet , IndexView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', AlphaVantageServiceViewSet, basename='api')

urlpatterns = [
    path('register', SignUpView.as_view()),
    path('', IndexView.as_view()),
    path('api/', include(router.urls)),
]
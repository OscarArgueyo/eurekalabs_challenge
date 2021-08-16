from rest_framework import generics
from .serializer import RegisterSerializer , UserSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .mixins.views import AlphaVantageServiceMixinsView
from django.views.generic import TemplateView
import os



class SignUpView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User Created Successfully. Login for get auth token and make requests",
        })


class AlphaVantageServiceViewSet(viewsets.GenericViewSet,
                                 viewsets.mixins.RetrieveModelMixin,
                                 AlphaVantageServiceMixinsView):
    permission_classes = (IsAuthenticated,)

    lookup_field = 'symbol'

    def retrieve(self, request, *args, **kwargs):
        results = self.process_request(symbol=kwargs.get('symbol') , params=request.GET)
        return Response(results.json(), results.status_code )


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        markdowntext = open(os.path.join(os.path.dirname(__file__),'..','readme.md')).read()

        context = super().get_context_data(**kwargs)
        context['markdowntext'] = markdowntext

        return context


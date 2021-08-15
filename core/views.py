from rest_framework import generics
from rest_framework.response import Response
from .serializer import RegisterSerializer , UserSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

import requests



class SignUpView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Login for get auth token and make requests",
        })


class AlphaVantageServiceViewSet(viewsets.GenericViewSet,
                                 viewsets.mixins.RetrieveModelMixin):
    permission_classes = (IsAuthenticated,)

    lookup_field = 'symbol'

    def alpha_vantage_service_request(self , symbol, params):
        url = 'https://www.alphavantage.co/query'
        params = dict(params)
        params.setdefault('apikey', 'X86NOH6II01P7R24')
        params.setdefault('symbol', symbol)
        r = requests.get(url, params=params)
        data = r.json()
        return data

    def retrieve(self, request, *args, **kwargs):
        results = self.alpha_vantage_service_request(symbol=kwargs.get('symbol') , params=request.GET)
        return Response(results)


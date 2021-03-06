import requests
from django.conf import settings


class AlphaVantageServiceMixinsView(object):

    def process_request(self , symbol, params):
        url = settings.ALPHAVANTAGEAPI_API_QUERY_URL
        params = dict(params)
        params.setdefault('apikey', settings.ALPHAVANTAGEAPI_API_KEY)
        params.setdefault('symbol', symbol)
        r = requests.get(url, params=params)
        return r
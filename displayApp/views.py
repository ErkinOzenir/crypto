import requests
from django.http import JsonResponse
from django.views import View

class CryptoTableView(View):
    def get(self, request):
        api_url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
        api_key = "972ad641-aad3-4b50-99c7-8a3659bdae50"

        params = {
            "start": 1,
            "limit": 5,
            "convert": "USD",
        }

        headers = {
            "Accepts": "application/json",
            "X-CMC_PRO_API_KEY": api_key,
        }


        response = requests.get(api_url, params=params, headers=headers)
        data = response.json()

        filtered_data = []
        for item in data["data"]:
            filtered_item = {
                "id": item["id"],
                "name": item["name"],
                "price": item["quote"]["USD"]["price"],
                "change_1h": item["quote"]["USD"]["percent_change_1h"],
                "change_24h": item["quote"]["USD"]["percent_change_24h"],
                "change_7d": item["quote"]["USD"]["percent_change_7d"],
            }
            filtered_data.append(filtered_item)

        response_data = {
            "crypto_data": filtered_data
        }

        return JsonResponse(response_data, safe=False)


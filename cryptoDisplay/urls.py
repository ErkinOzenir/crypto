from django.contrib import admin
from django.urls import path
from displayApp.views import CryptoTableView

urlpatterns = [
    path('crypto/', CryptoTableView.as_view(), name='crypto_table'),
    path('admin/', admin.site.urls),
]

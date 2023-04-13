
from django.urls import path
from . import views



urlpatterns = [
    path('vpn/' , views.vpnapi_view)
]
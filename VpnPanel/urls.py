"""
URL configuration for VpnPanel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from VpnApi import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('' , views.signin_view , name='signin'),
    path('dashboard/' , views.dashboard_view , name='dashboard'),
    path('addvpn/' , views.addvpn_view , name='addvpn'),
    path('update/<int:id>/' , views.update_view , name = 'update'),
    path('delete/<int:id>/' , views.delete_view , name = 'delete'),
    path('signout/' , views.signout_view , name='signout'),

    path('api/' , include('VpnApi.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

"""first_django_proyect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from shipping_addresses import urls as addresses_url
from main import urls as main_urls




urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include(main_urls, namespace='user')),
    path('addresses/', include(addresses_url, namespace='addresses'))
     
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

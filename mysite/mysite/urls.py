"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include, path
from polls.controllers import index
from polls.controllers import userorder
from polls.views import add_image, image_list
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
#    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('', index.index),
    path('index/', index.index),
    path('lesson4/', index.lesson4),
    path('order/', index.order),
    path('catalog/', index.catalog),
    path('news/', image_list, name='image_list'),
    path('order/userorder/ok', index.ok),
    path('order/userorder/', userorder.create),
    path('add_image/', add_image, name='add_image'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

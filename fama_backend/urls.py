"""fama_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from users.views import (
    FacebookLogin,
    GoogleLogin,
    users_list,
    user_detail,
    user_create,
    user_update,
    user_delete
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest-auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('rest-auth/google/', GoogleLogin.as_view(), name='google_login'),
    path('api/users_list', users_list, name='users_list'),
    path('api/user_detail/<str:pk>', user_detail, name='user_detail'),
    path('api/user_create', user_create, name='user_create'),
    path('api/user_update/<str:pk>', user_update, name='user_update'),
    path('api/user_delete/<str:pk>', user_delete, name='user_delete'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

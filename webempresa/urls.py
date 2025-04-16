
"""
URL configuration for webempresa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from core import urls
from django.conf import settings
from services import urls 
from blog import urls 
urlpatterns = [
    #Paths admin
    path('admin/', admin.site.urls),
    #Path blogs
    path('blog/', include('blog.urls')),
    #Paths core
    path('', include('core.urls')),
    #Path services
    path('services/', include('services.urls')),
    #Path pages
    path('page/', include('pages.urls')),
    
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
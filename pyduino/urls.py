"""pyduino URL Configuration

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
from django.urls import path 
from APP import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('news',views.news,name="news"),
    path('signup',views.signup,name="signup"),
    path('intern',views.intern,name="intern"),
    path("deleteAPI/<int:id>",views.deleteAPI,name="deleteAPI"),
    path("communityBE",views.communityBE,name="communityBE"),
    path("community",views.community,name="community"),
    path('get_messages', views.get_messages, name='get_messages'),
    path('sendMail', views.sendMail, name='sendMail'),
    path('tools', views.tools, name='tools'),
    path('otp', views.otp, name='otp'),
    path('contact', views.contact, name='contact'),
    path('demo', views.demo, name='demo'),
    path("apiCall",views.apiCall,name="apiCall"),
    path("internlogin",views.internlogin,name="internlogin"),
    path("internregister",views.internregister,name="internregister"),
    path('internship_application', views.internship_application, name='internship_application'),


    
    
    
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


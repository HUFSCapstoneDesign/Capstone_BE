"""
URL configuration for capstone_ project.

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
from django.urls import path, include

# http://localhost:8000/templates -> views.index -> def index(request):
# casptone_ -> 프로젝트 성격의 파일이므로 이 곳에는 프로젝트 성격의 url 매핑만 추가 되어야 함.
urlpatterns = [
    path("admin/", admin.site.urls),
    path("templates/", include("templates.urls")),  # templates 앱의 urls.py
# templates/으로 시작하는 페이지를 요청하면 templates.urls 파일의 매핑 정보를 얽어서 처리
]

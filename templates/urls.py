from django.urls import path

from . import views

urlpatterns = [
    # path("url", 메소드) -> "url" 이 생략된 이유는 capstone_ urls.py 에서 이미 매핑되었기 때문
    path('', views.index)
]

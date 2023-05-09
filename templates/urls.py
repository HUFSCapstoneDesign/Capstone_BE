from django.urls import path

from . import views

app_name = "templates"

urlpatterns = [
    path("", views.index, name="index"),  # 템플릿 전체 보여 주기
    path("<int:category_id>/", views.category_get, name="category_get"),  # 카테 고리 선택 조회
]

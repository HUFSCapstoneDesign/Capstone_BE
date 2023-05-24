from django.urls import path
from . import views

app_name = "templates"

urlpatterns = [
    path("", views.index, name="index"),  # 템플릿 전체 보여 주기
    path("<int:category_id>/", views.get_templates_by_category_id, name="category_get"),  # 카테고리 선택 조회
    path("search/", views.template_search, name="template_search"),  # 카테고리 이름 조회 # /templates/search/
    path("<int:template_id>/explain", views.show_template_explain, name="template_show"),  # 템플릿 설명(팝업창)
    path("template_save/", views.template_save, name="template_save")  # 템플릿 저장  # /templates/template_save
]

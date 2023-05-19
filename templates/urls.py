from django.urls import path
from . import views

app_name = "templates"

urlpatterns = [
    path("", views.index, name="index"),  # 템플릿 전체 보여 주기
    path("<int:category_id>/", views.get_templates_by_category_id, name="category_get"),  # 카테고리 선택 조회
    path("search/", views.template_search, name="template_search"),  # 카테고리 이름 조회 # /templates/search/
    path("edit/", views.template_text_edit, name="text_edit"),  # 템플릿 편집창  # /templates/edit
    # path("edit/<int:image_id>>", views.template_image_edit, name="image_edit")  # 템플릿 편집창  # /templates/edit
]

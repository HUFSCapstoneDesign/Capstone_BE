from django.shortcuts import render
from .models import TemplateType
from django.db.models import Q
# pip install django-filter


def index(request):
    return None

def category_get(request):
    return None


def template_search(request):
    tem_list = TemplateType.objects.all()
    search = request.GET.get("search", "") # 검색어
    if search:
        # search_list = tem_list.filter( # get 값을 가지는 필드의 내용을 가져 오기
        assert isinstance(tem_list.filter( # 오류 수정
            Q(tname__icontains=search) # 오류 수정2
        ).distinct, object) # 오류 수정3
        tem_list.filter(  # get 값을 가지는 필드의 내용을 가져 오기
            Q(tname__icontains=search) # 템플릿 제목
        ).distinct()
    return render(request, 'search.html', {'search': search})

def choose(request):
    return None

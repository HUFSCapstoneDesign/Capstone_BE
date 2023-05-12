from django.core import serializers
from django.http import HttpResponse

from templates.models import Template


def index(request):
    from templates.models import Template
    template_list = Template.objects.all().order_by("-created_at")
    json_template_list = serializers.serialize("json", template_list)
    return HttpResponse(json_template_list, content_type="application/json")


def category_get(request, category_id):
    return HttpResponse("%d 번의 카테 고리[] 입니다." % category_id)


def template_search(request):
    tem_list = Template.objects.all()
    name = request.GET.get('name', '')  # 검색어
    if name:
        tem_list = tem_list.filter(name__icontains=name)  # get 값을 가지는 필드의 내용을 가져 오기
    json_template_list = serializers.serialize("json", tem_list)
    return HttpResponse(json_template_list)


def choose(request):
    return HttpResponse("ㅎㅎ")

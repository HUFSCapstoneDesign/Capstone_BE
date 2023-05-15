from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, get_list_or_404

from templates.models import Template, TemplateCategory


def index(request):
    template_list = Template.objects.all().order_by("-created_at")
    return HttpResponse(serializers.serialize("json", template_list), content_type="application/json")


def get_templates_by_category_id(request, category_id):
    template_category = get_object_or_404(TemplateCategory, pk=category_id)
    template_list = Template.objects.filter(template_category__exact=template_category)
    return HttpResponse(serializers.serialize("json", template_list), content_type="application/json")


def template_search(request):
    tem_list = Template.objects.all()
    name = request.GET.get('name', '')  # 검색어
    if name:
        tem_list = tem_list.filter(name__icontains=name)  # get 값을 가지는 필드의 내용을 가져 오기
    json_template_list = serializers.serialize("json", tem_list)
    return HttpResponse(json_template_list, content_type="application/json")


def choose(request):
    return HttpResponse("ㅎㅎ")


def show_template_explain(request, template_id):
    template = get_list_or_404(Template, id=template_id)
    return HttpResponse(serializers.serialize("json", template), content_type="application/json")

from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from templates.models import Template, TemplateCategory
from templates.template_serializer import TemplateSerializer, TemplateCategorySerializer


@api_view(['GET'])
def index(request):
    templates = Template.objects.all().order_by("-created_at")
    template_category = TemplateCategory.objects.all()
    return Response(
        [TemplateSerializer(templates, many=True).data,
         TemplateCategorySerializer(template_category, many=True).data]
    )


def get_templates_by_category_id(request, category_id):
    template_category = get_object_or_404(TemplateCategory, pk=category_id)
    template_list = Template.objects.filter(template_category__exact=template_category)
    return HttpResponse(serializers.serialize("json", template_list), content_type="application/json")


def template_search(request):
    tem_list = Template.objects.all()
    name = request.GET.get('name')  # 검색어
    tem_list = tem_list.filter(name__icontains=name)  # get 값을 가지는 필드의 내용을 가져 오기
    json_template_list = serializers.serialize("json", tem_list)
    return HttpResponse(json_template_list, content_type="application/json")


def show_template_explain(request, template_id):
    template = get_list_or_404(Template, id=template_id)
    return HttpResponse(serializers.serialize("json", template), content_type="application/json")

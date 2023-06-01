from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from templates.models import Template, TemplateCategory
from templates.serializer import TemplateSerializer, TemplateCategorySerializer, TemplateTagSerializer, \
    TemplateImageSerializer, TemplateTextSerializer, TemplateEditSerializer, TemplateSaveSerializer


# 템플릿 선택창
@api_view(['GET'])
def index(request):
    templates = Template.objects.all().order_by("-created_at")
    templates_categories = TemplateCategory.objects.all()
    return Response([TemplateSerializer(templates, many=True).data,
                     TemplateCategorySerializer(templates_categories, many=True).data])


@api_view(['GET'])
def get_templates_by_category_id(request, category_id):
    template_category = get_object_or_404(TemplateCategory, pk=category_id)
    template_list = Template.objects.filter(template_category=template_category)
    return Response(TemplateSerializer(template_list, many=True).data)


@api_view(['GET'])
def template_search(request):
    name = request.GET.get('name')  # 검색어
    tem_list = Template.objects.filter(name__icontains=name)  # get 값을 가지는 필드의 내용을 가져 오기
    return Response(TemplateSerializer(tem_list, many=True).data)


# 템플릿 설명창
@api_view(['GET'])
def show_template_explain(request, template_id):
    template = get_object_or_404(Template, pk=template_id)
    template_tag_list = template.templatetag_set.all()
    return Response([TemplateSerializer(template).data,
                     TemplateTagSerializer(template_tag_list, many=True).data])


# 템플릿 편집창
@api_view(['GET'])
def template_edit(request, template_id):
    template = get_object_or_404(Template, pk=template_id)
    image_list = template.image_set.all()
    text_list = template.text_set.all()

    return Response(
        [TemplateImageSerializer(image_list, many=True).data, TemplateEditSerializer(template).data,
         TemplateTextSerializer(text_list, many=True).data])

# 템플릿 미리보기
class TemplateCreateAPIView(generics.CreateAPIView):
    queryset = Template.objects.all()
    serializer_class = TemplateSaveSerializer


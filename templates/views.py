import json
from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from templates.models import Template, TemplateCategory, Text, Image
from django.views.decorators.csrf import csrf_exempt
# from django.views.decorators.http import require_POST


# 템플릿 선택창
def index(request):
    from templates.models import Template
    template_list = Template.objects.all().order_by("-created_at")
    return HttpResponse(serializers.serialize("json", template_list), content_type="application/json")


def get_templates_by_category_id(request, category_id):
    template_category = get_object_or_404(TemplateCategory, pk=category_id)
    template_list = Template.objects.filter(template_category__exact=template_category)
    return HttpResponse(serializers.serialize("json", template_list), content_type="application/json")


def template_search(request):
    tem_list = Template.objects.all()
    name = request.GET.get('name')  # 검색어
    tem_list = tem_list.filter(name__icontains=name)  # get 값을 가지는 필드의 내용을 가져 오기
    json_template_list = serializers.serialize("json", tem_list)
    return HttpResponse(json_template_list)

# 템플릿 설명창


# 템플릿 편집창
@csrf_exempt
def template_text_edit(request):
    # if request.method == 'POST' or request.method == 'GET':
    if request.method == 'POST':
        template_id = request.POST.get('template_id')
        template_category_id = request.POST.get('category_id')
        text_id = request.POST.get('text_id')
        try:
            template = Template.objects.get(id=template_id)
            template_category = TemplateCategory.objects.get(id=template_category_id)
            text = Text.objects.get(id=text_id)
        except (Template.DoesNotExist, TemplateCategory.DoesNotExist):
            return JsonResponse({'error': 'Template or Template Category not found'}, status=404)

        data = [
            {
                'model': 'templates.template',
                'pk': template.id,
                'fields': {
                    'name': template.name,
                    'member': template.member.id,
                    'template_category': template.template_category.id,
                    'created_at': template.created_at,
                    'update_at': template.update_at,
                }
            },
            {
                'model': 'templates.templatecategory',
                'pk': template_category.id,
                'fields': {
                    'name': template_category.name,
                }
            },
            {
                'model': 'templates.text',
                'pk': text.id,
                'fields': {
                    'content': text.content,
                    'size': text.size,
                    'pont': text.pont,
                    'x': text.x,
                    'y': text.y,
                    'angle': text.angle,
                    'text_color': text.text_color,
                    'back_color': text.back_color,
                    'cursive': text.cursive,
                    'align': text.align,
                    'line': text.line,
                    'textopa': text.textopa,
                    'backopa': text.backopa,
                    'zindex': text.zindex,
                    'template': text.template.id,
                }
            }
        ]

        response_data = json.dumps(data)
        return JsonResponse(response_data, safe=False)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def template_image_edit(request):
    if request.method == 'POST' or request.method == 'GET':
        template_id = request.GET.get('template_id')
        template_category_id = request.GET.get('category_id')
        image_id = request.GET.get('image_id')
        try:
            template = Template.objects.get(id=template_id)
            template_category = TemplateCategory.objects.get(id=template_category_id)
            image = Image.objects.get(id=image_id)
        except (Template.DoesNotExist, TemplateCategory.DoesNotExist):
            return JsonResponse({'error': 'Template or Template Category not found'}, status=404)

        data = [
            {
                'model': 'templates.template',
                'pk': template.id,
                'fields': {
                    'name': template.name,
                    'member': template.member.id,
                    'template_category': template.template_category.id,
                    'created_at': template.created_at,
                    'update_at': template.update_at,
                }
            },
            {
                'model': 'templates.templatecategory',
                'pk': template_category.id,
                'fields': {
                    'name': template_category.name,
                }
            },
            {
                'model': 'templates.image',
                'pk': image.id,
                'fields': {
                    'x': image.x,
                    'y': image.y,
                    'height': image.height,
                    'width': image.width,
                    'cursive': image.cursive,
                    'transparency': image.transparency,
                    'angle': image.angle,
                    'template': image.template.id,
                }
            }
        ]

        response_data = json.dumps(data)
        return JsonResponse(response_data, safe=False)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
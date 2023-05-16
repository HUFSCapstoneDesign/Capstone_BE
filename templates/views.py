from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from templates.models import Template, TemplateCategory
from django.views.decorators.csrf import csrf_exempt



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

@csrf_exempt
def template_choose(request):
    if request.method == 'POST':
        tem_id = request.POST.get('tem_id')
        tem = Template.objects.filter(pk=tem_id)
        json_template_list = serializers.serialize("json", tem)
        return JsonResponse(json_template_list)
    else:
        return JsonResponse({'error': 'Invalid request method.'})
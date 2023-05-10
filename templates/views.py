from django.core import serializers
from django.http import HttpResponse


def index(request):
    from templates.models import Template
    template_list = Template.objects.all().order_by("-created_at")
    json_template_list = serializers.serialize("json", template_list)
    return HttpResponse(json_template_list, content_type="application/json")
    # return HttpResponse("인덱스 입니다.")


def category_get(request, category_id):
    return HttpResponse("%d 번의 카테고리[] 입니다." % category_id)

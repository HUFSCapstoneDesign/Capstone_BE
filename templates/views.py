from django.http import HttpResponse


def index(request):
    return HttpResponse("인덱스 입니다.")


def category_get(request, category_id):
    return HttpResponse("%d 번의 카테고리 입니다." % category_id)

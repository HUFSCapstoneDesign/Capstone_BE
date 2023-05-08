from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("안녕하세요 12팀 에너 자이조입니다.")

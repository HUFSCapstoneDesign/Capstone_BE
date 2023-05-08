from django.shortcuts import render, get_object_or_404

from templates.models import Question


# Create your views here.
def index(request):
    question_list = Question.objects.order_by('-create_date')  # 내림 차순
    context = {'question_list': question_list}
    # templates/question_list.html -> 프로젝트 하위 존재
    return render(request, 'templates/question_list.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'templates/question_detail.html', context)

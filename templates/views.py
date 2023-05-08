from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from templates.models import Question, Answer


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


def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # 방법2. question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    answer = Answer(question=question, content=request.POST.get('content'), create_date=timezone.now())
    answer.save()
    return redirect('templates:detail', question_id=question.id)

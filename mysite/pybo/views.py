from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

# Create your views here.

def index(request):
    # pybo 목록 출력
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return HttpResponse("안녕하세요 pybo입니다. 반갑습니다.")
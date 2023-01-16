from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Question
from django.http import Http404

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

## The view raises the Http404 exception if a question with the requested ID doesn’t exist.

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id) ## Used get_object_or_404 insted of using both get and Http404
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
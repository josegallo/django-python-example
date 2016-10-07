from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question
# Create your views here.

def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    #better option to render the template
    context = {'latest_questions':latest_questions}
    #make a dictionary with the object to render
    return render(request,'polls/index.html',context)
    #render the objects

def detail(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    context = {'question': question}
    return render(request, 'polls/detail.html', context)

def results(request, question_id):
    return HttpResponse('This are the results of the question: %s' % question_id)

def vote(request, question_id):
    return HttpResponse("Vote on question: %s" % question_id)


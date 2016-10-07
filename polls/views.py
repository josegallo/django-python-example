from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader, RequestContext
# Create your views here.

def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    #First option to render the template
    #Throw the lastest question ordered by date of publication
    template = loader.get_template('polls/index.html')
    #loads our template
    context = RequestContext(request, {'latest_questions':latest_questions})
    #define the context to be rendered with the latest_questions objects

    return HttpResponse(template.render(context))

def detail(request, question_id):
    return HttpResponse('This is the detail view of the question: %s' % question_id)

def results(request, question_id):
    return HttpResponse('This are the results of the question: %s' % question_id)

def vote(request, question_id):
    return HttpResponse("Vote on question: %s" % question_id)

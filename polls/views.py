from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Question, Choice
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
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        # request.POST[choice] retrieves the value of choice, that's the id. (see
        # form in the detail.html template
    except:
        context = {'question': question, 'error_message': 'Please select a choice'}
        return render(request, 'polls/detail.html', context)
    # if try works
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:result', args=(question_id,)))
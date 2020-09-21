from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse
# Create your views here.


def index(reqeust):
    q = get_list_or_404(Question)
    return render(reqeust, 'polls/index.html', {'q': q})


def details(request, q_id):
    q = Question.objects.get(pk=q_id)
    choices = q.choice_set.all()
    context = {
        'question': q,
        'choices': choices
    }
    return render(request, 'polls/details.html', context)


def results(request, q_id):
    q = Question.objects.get(pk=q_id)
    selected_choice = q.choice_set.get(pk=request.POST['choice'])
    print(selected_choice)
    selected_choice.votes += 1
    print(selected_choice.votes)
    selected_choice.save()

    return HttpResponseRedirect(reverse('final', args=(q.id,)))


def final(request, q_id):

    q = get_object_or_404(Question, pk=q_id)
    return render(request, 'polls/votes.html', {'q': q})

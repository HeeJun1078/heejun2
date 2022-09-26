from django.http import HttpResponse
from django.shortcuts import render
from .models import Question, Choice


def index(request):
    questions = Question.objects.all()
    output = ", ".join([q.question_text for q in questions])
    choices = Choice.objects.all()
    output2 = ", ".join([c.choice_text for c in choices])
    return HttpResponse(output + output2)


def study(request):
    return HttpResponse("오늘부터 공부해야지")


def sleep(request):
    return HttpResponse("자야지")


def question(request, qid):
    q = Question.objects.get(id=qid)
    choices = Choice.objects.filter(question=q)
    output2 = ", ".join([c.choice_text for c in choices])
    # for choice in choices:
    #     print(choice.choice_text)
    # return HttpResponse(f"You're looking at question {qid}, {q.question_text}, {q.pub_date}, {output2}")
    context = {"question": q, "choices": choices}
    return render(request, 'question.html', context)

def add(request, a, b):
    return HttpResponse(a + b)


def mul(request, a, b):
    return HttpResponse(a * b)

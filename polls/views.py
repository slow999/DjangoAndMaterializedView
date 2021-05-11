from django.shortcuts import render
from polls.models import Question, Question2021


def index(request):
    questions = Question.objects.all()
    print('Origin table returns {} questions'.format(questions.count()))

    questions_2021 = Question2021.objects.all()
    print('Materialized view returns {} questions.'.format(questions_2021.count()))

    return render(request, 'polls/index.html')


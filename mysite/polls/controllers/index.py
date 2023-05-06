from django.http import HttpResponse
from django.shortcuts import redirect, render
from polls.models import Feedback

def index(request):
    feedback = Feedback.objects.create()
    feedback.email = '123123@mail.ru'
    feedback.text = '123123'
    feedback.save()
    return render(request, 'index.html', {})


def about(request):
    return render(request, 'catalog.html', {})

def lesson4(request):
    name = request.GET.get('name')
    return render(request, 'lesson4.html', {'name' : name,
                                            'title':'lesson4'})

def about_work(request):
    return HttpResponse('Im LOX')
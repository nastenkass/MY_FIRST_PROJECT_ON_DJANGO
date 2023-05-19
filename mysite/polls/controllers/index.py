from django.http import HttpResponse
from django.shortcuts import redirect, render
from polls.models import Feedback

def index(request):
    #feedback = Feedback.objects.create()
    #feedback.email = '123123@mail.ru'
    #feedback.text = '123123'
    #feedback.save()
    return render(request, 'index.html', {'title':'Главная страница'})

def order(request):
    return render(request, 'order.html', {'title':'Заказ'})

def catalog(request):
    return render(request, 'catalog.html', {'title':'Каталог магазина'})

def ok(request):
    return render(request, 'ok.html', {'title':'Каталог магазина'})


def lesson4(request):
    name = request.GET.get('name')
    return render(request, 'lesson4.html', {'name' : name,
                                            'title':'lesson4'})

from django.http import HttpResponse
from django.shortcuts import redirect, render
from polls.models import UserOrder


def create(request):

    userorder = UserOrder()
    userorder.firstname = request.POST.get('firstname')
    userorder.phone = request.POST.get('phone')
    userorder.lastname = request.POST.get('lastname')
    userorder.email = request.POST.get('email')
    userorder.region = request.POST.get('region')
    userorder.adres = request.POST.get('adres')
    userorder.city = request.POST.get('city')
    userorder.index = request.POST.get('index')
    userorder.delivery = request.POST.get('delivery')
    userorder.credit = request.POST.get('credit_1')
    userorder.accept = request.POST.get('accept')

    userorder.save()

    return render(request, 'ok.html')

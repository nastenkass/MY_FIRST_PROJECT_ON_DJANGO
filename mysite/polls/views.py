from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ImageRecordForm
from .models import ImageRecord

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def add_image(request):
    if request.method == 'POST':
        form = ImageRecordForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_list')
    else:
        form = ImageRecordForm()
    return render(request, 'add_image.html', {'form': form})

def image_list(request):
    images = ImageRecord.objects.all()
    return render(request, 'image_list.html', {'images': images})
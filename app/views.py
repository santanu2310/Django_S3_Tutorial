from django.shortcuts import render
from .models import Image

# Create your views here.

def home(request):
    data_set = Image.objects.all()
    context = {'data_set':data_set,}
    return render(request, 'app/index.html', context)
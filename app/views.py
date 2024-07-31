from django.shortcuts import render
from .models import Index

def index(request):
    salom = Index.objects.all()

    context = {
        'index': salom
    }
    return render (request, 'home_list.html', context)


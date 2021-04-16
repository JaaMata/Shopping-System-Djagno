from django.shortcuts import render
from .models import *
# Create your views here.


def home(request):
    return render(request, "index.html")


def items(request):
    items = Item.objects.all()

    context = {'items': items}
    return render(request, "items.html", context)


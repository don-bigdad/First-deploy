from django.shortcuts import render
from .models import *
# Create your views here.
def response_customer(request):
    categories = Category.objects.all()
    dish = Dish.objects.all()
    events = Event.objects.all()
    data ={"categories":categories,"dish":dish,"events":events}
    return render(request,"index.html",context=data)
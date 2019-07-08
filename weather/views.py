from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'weather/home.html')

def item(request):
    return render(request, 'weather/item.html')

def about(request):
    return render(request, 'weather/about.html')

def items(request):
    return render(request, 'weather/items.html')

def plan(request):
    return render(request, 'weather/plan.html')

def plans(request):
    return render(request, 'weather/plans.html')
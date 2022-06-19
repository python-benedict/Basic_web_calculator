from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'myAddApp/home.html')

def add(request):
    cal = request.GET['cal']
    value1 = int(request.GET['num1'])
    value2 = int(request.GET['num2'])

    if cal == 'add':
        res = value1 + value2
    elif cal == 'sub':
        res = value1 - value2
    elif cal == 'div':
        res = value1 / value2
    else:
        res = 'Please enter a valid value inside the box'

    context = {
        'res':res
    }


    return render(request, 'myAddApp/result.html', context)
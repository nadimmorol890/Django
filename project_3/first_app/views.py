from django.shortcuts import render
import datetime

# Create your views here.

def home(request):
    d = {'author' : 'Nadim', 'age' : 20, 'birthday' : datetime.datetime.now(), 'val' : ' ', 'list' : ['python', 'is', 'best'], 'courses' : [
        {
            'id': 1,
            'name': 'Python',
            'fee': 2000
        },
        {
            'id': 2,
            'name': 'Java',
            'fee': 2500
        },
        {
            'id': 3,
            'name': 'C++',
            'fee': 3000
        }
    ]}
    return render(request, 'home.html', d)
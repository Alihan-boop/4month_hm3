from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    products = [
        {"name": "Телефон", "price": 10000},
        {"name": "Ноутбук", "price": 50000},
        {"name": "Наушники", "price": 2000}
    ]
    
    context = {
        'products': products,
        'message': None
    }
    
    if request.method == 'POST':
        context['message'] = "Спасибо за отзыв!"
        
    return render(request, 'index.html', context)

def profile(request):
    context = {
        'username': 'Иван Иванов',
        'email': 'ivan@example.com',
        'is_active': True,
        'score': 85
    }
    return render(request, 'profile.html', context)
from django.shortcuts import render, HttpResponse

def index(request) -> HttpResponse:
    context: dict = {
        'title': 'Home',
        'content': 'Главная страница магазина - VLASO SHOP'
    }

    return render(request, 'main/index.html', context)

def about(request) -> HttpResponse:
    context: dict = {
        'title': 'About Us',
        'content': 'Страница магазина - О НАС'
    }
    return render(request, 'about-us/about.html', context)
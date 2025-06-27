from django.shortcuts import render

def index(request):
    return render(request, 'landing_page/index.html')

def home(request):
    return render(request, 'landing_page/index.html')

def about(request):
    return render(request, 'landing_page/about_section.html')

def services(request):
    return render(request, 'landing_page/services.html')

def portfolio(request):
    return render(request, 'landing_page/portfolio_section.html')

def contact(request):
    return render(request, 'landing_page/contact.html')
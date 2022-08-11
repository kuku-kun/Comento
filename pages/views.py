from django.shortcuts import render

# Create your views here.
def mainpage(request):
    return render(request, 'pages/mainpage.html')

def company(request):
    return render(request, 'pages/company_info.html')

def MAIN(request):
    return render(request, 'pages/MAIN.html')

def ABOUTUS(request):
    return render(request, 'pages/ABOUTUS.html')

def GOODS(request):
    return render(request, 'pages/GOODS.html')

def EVENT(request):
    return render(request, 'pages/EVENT.html')

def CONTACT(request):
    return render(request, 'pages/CONTACT.html')

def QUESTION(request):
    return render(request, 'pages/QUESTION.html')

def EVENT_P(request):
    return render(request, 'pages/EVENT_GET.html')
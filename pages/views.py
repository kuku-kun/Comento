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

def REVIEW(request):
    return render(request, 'pages/REVIEW.html')

def CONTACT(request):
    return render(request, 'pages/CONTACT.html')

def QUESTION(request):
    return render(request, 'pages/QUESTION.html')

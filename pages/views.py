from django.shortcuts import render

def index(request):
    return render(request,'main_page/index.html')

def login(request):
    return render(request,'login_page/login.html')
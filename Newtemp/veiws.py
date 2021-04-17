from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'home.html')
def admin(request):
    return render(request,'admin.html')
def account(request):
    return render(request,'account.html')
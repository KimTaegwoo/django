from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>안녕하세요. pybo에 오신 것을 환영합니다.</h1>")
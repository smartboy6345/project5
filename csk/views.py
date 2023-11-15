from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def rohit(request):
    return render(request,'rohit.html')

def sky(request):
    return HttpResponse('<h1><marquee>sky stands for surya kumar yadav</h1></marquee>')
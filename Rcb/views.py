from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def siraj(request):
    return HttpResponse('<h1><marquee>This is one of the team memeber of royal challenges banglore</marquee></h1>')
def siraj1(request):
    return render(request,'siraj.html')
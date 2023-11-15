from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def mumbai(request):
    return HttpResponse('<h1>the team was opperated byt RELIANCE CEO MR.MUKAISHAMBANI GARU</h1>')
def raina(request):
    return render(request,'raina.html')
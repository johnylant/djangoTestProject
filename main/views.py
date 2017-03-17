from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

'''
def home(request):
    return HttpResponse("Hello man!")
'''

def home(request):
    return render(request, "main/home.html", {'message':"Hello, come and play some ticktacktoe!"})

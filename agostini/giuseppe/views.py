# Create your views here.
from django.http import HttpResponse
from pif import get_public_ip
import time
from datetime import date


def home(request):
    return HttpResponse("Hello, world!")
    
def myip(request):
    return HttpResponse("Welcome, my ip is: "+ get_public_ip())
    
def year(request):
    d=date.today()
    b="Welcome, the year is: %s" % d.year
    return HttpResponse(b)
    
def month(request):
    d=date.today()
    b="Welcome, the month is: %s" % d.month
    return HttpResponse(b)

def day(request):
    d=date.today()
    b="Welcome, the day is: %s" % d.day
    return HttpResponse(b)
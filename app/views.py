from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def silk(request):
    return HttpResponse('<H1><marquee>we are not talking about dairymilk silk</marquee></H1><H1><marquee> we are talking about silk smitha</marquee></H1>')
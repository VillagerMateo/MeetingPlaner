from django.db import connection
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

from meetings.models import Meeting

# Create your views here.

def welcome(request):

    months = []
    posts = Meeting.objects.raw("SELECT id, data FROM meetings_meeting ORDER BY data")
    for s in posts:
        
        month = s.data.strftime("%B")
        if month not in months:
        # print(month)
            months.append(month)
    # print(connection.queries)
    # maslo = posts.strftime("%B")
    
    print(months)
    # return render(request, 'website/welcome.html', {'niewiem': months})
    
    return render(request, 'website/welcome.html',{"meetings": Meeting.objects.all(), 'niewiem': months})

def date(request):
    return HttpResponse('Ta strona otworzyła się o' + str(datetime.now()))

def about(request):
    return HttpResponse('Jakieś tekst')

# def showMonth(request):
#     months = []
#     posts = Meeting.objects.raw("SELECT id, data FROM meetings_meeting ORDER BY data")
#     for s in posts:
        
#         month = s.data.strftime("%B")
#         if month not in months:
#         # print(month)
#             months.append(month)
#     # print(connection.queries)
#     # maslo = posts.strftime("%B")
    
#     print(months)
#     return render(request, 'website/welcome.html', {'niewiem': months})

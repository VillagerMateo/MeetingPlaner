from turtle import title
from django.db import connection
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

from meetings.models import Meeting


def welcome(request):

    n = request.GET.get('n') if request.GET.get('n') != None else ''
    print(n)
    q = request.GET.get('q') #if request.GET.get('q') != None else ''
    print(q)
    

    meetings = []
    months = []

    posts = Meeting.objects.raw("SELECT id, data FROM meetings_meeting ORDER BY data")
    
    for s in posts:
        nr_id = s.id
        month = s.data.strftime("%B")
            
        if month not in months:
            months.append(month)

        if q == month:
            meetings.append(Meeting.objects.get(id=nr_id))
            
    if n != '' or n != None and q == '' or q == None:
        meetings = Meeting.objects.filter(title__contains=n)

    elif q == '' or q == None and n == '' or n == None:
        meetings = Meeting.objects.all()
    
    
    return render(request, 'website/welcome.html', {"meetings": meetings, 'months': months})


def date(request):
    return HttpResponse('Ta strona otworzyła się o' + str(datetime.now()))


def about(request):
    return HttpResponse('Jakieś tekst')

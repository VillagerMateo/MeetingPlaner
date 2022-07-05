from datetime import date
from django.shortcuts import redirect, render, get_object_or_404, redirect
# modelform_factory tworzy formularz na podstawie danej klasy/modelu
from django.forms import modelform_factory
# from .forms import MeetingForm
from .models import Meeting, Room
# from django.db.models.functions import ExtractMonth


def detail(request, id):
    # Jeśli nie ma pożądanego obiektu w bazie, wyświetli się błąd 404
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, 'meetings/detail.html', {"meeting": meeting})

def rooms_list(request):
    return render(request, "meetings/rooms_list.html",
        {"rooms": Room.objects.all()})

# Stworzy formularz HTML na podstawie modelu Meeting
MeetingForm = modelform_factory(Meeting, exclude=[])


def new(request):
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = MeetingForm
    return render(request, "meetings/new.html", {'form': form})

def updateMeeting(request, pk):
    meeting = Meeting.objects.get(id=pk)
    form = MeetingForm(instance=meeting)

    if request.method == 'POST':
        form = MeetingForm(request.POST, instance=meeting)
        if form.is_valid():
            form.save()
            return redirect('welcome')

    return render(request, 'meetings/new.html', {'form': form})

def deleteMeeting(request, pk):
    meeting = Meeting.objects.get(id=pk)
    if request.method == 'POST':
        meeting.delete()
        return redirect('welcome')
    return render(request, 'meetings/delete.html', {'obj': meeting})
    
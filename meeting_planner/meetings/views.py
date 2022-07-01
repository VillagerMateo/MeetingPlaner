from django.shortcuts import redirect, render, get_object_or_404, redirect
# modelform_factory tworzy formularz na podstawie danej klasy/modelu
from django.forms import modelform_factory
# from .forms import MeetingForm
from .models import Meeting, Room

# Create your views here.
def detail(request, id):

    # meeting = Meeting.objects.get(pk=id)
    # Jeśli nie ma pożądanego obiektu w bazie, wyświetli się błąd 404
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, 'meetings/detail.html', {"meeting": meeting})

def rooms_list(requeste):
    return render(requeste, "meetings/rooms_list.html",
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
from django.shortcuts import render
from .models import MyEvent, Guest
from .forms import EventForm

# Create your views here.

def start(request):
	if request.method == 'POST':		
		form = EventForm(request.POST)
		if form.is_valid():
			new_event = form.save()
			number_of_guests = new_event.number_of_guests
			return render (request, 'goha/guests.html', {'number_of_guests': number_of_guests})
		else: 
			form = EventForm()
			return render(request, 'goha/start.html', {'form': form})
	else: 
		form = EventForm()
		return render(request, 'goha/start.html', {'form': form})

def guests(request):
	return render(request,'goha/guests.html', {} )


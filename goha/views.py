from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from .models import MyEvent, Guest
from .forms import EventForm, GuestForm
from django.forms.models import inlineformset_factory
import random 



# Create your views here.

def start(request):
	if request.method == 'POST':		
		form = EventForm(request.POST)
		if form.is_valid():
			new_event = form.save()
			new_event.number_of_guests = range(new_event.number_of_guests)
			return redirect ('guests', pk = new_event.pk)
		else: 
			form = EventForm()
			return render(request, 'goha/start.html', {'form': form})
	else: 
		form = EventForm()
		return render(request, 'goha/start.html', {'form': form})

def guests(request, pk):
	my_event = get_object_or_404(MyEvent, pk=pk)
	number_of_guests = my_event.number_of_guests
	GuestInlineFormSet = inlineformset_factory(MyEvent, Guest, fields = ('guest_name', 'guest_email'), labels = {'guest_name' : ('Name'), 'guest_email' : ('E-Mail Address'),}, extra = number_of_guests, can_delete = False)
	if request.method == 'POST':
		formset = GuestInlineFormSet(request.POST, instance = my_event)
		if formset.is_valid():		
			new_guest = formset.save()
			return redirect('assignments', pk = my_event.pk )
			#return render (request, 'goha/assignments.html', {})
	else: 
		formset = GuestInlineFormSet(instance = my_event)
		return render(request, 'goha/guests.html', {'formset': formset})
		#return render_to_response('goha/guests.html', {'formset': formset}, context = RequestContext(request))


# def host_choice(request,pk):
# 	task_set = {'Salty', 'Sweet', 'Drink'}

def assignments(request, pk):
	my_event = get_object_or_404(MyEvent, pk=pk)
	my_guests = Guest.objects.filter(related_event = my_event)
	number_of_guests = range(my_event.number_of_guests)
	
	task_list = ['salty', 'sweet', 'to drink']
	
	assignments = {}
	
	host_assignment = random.choice(task_list)
	assignments[host_assignment] = str(my_event.host_name)
	
	for guest in number_of_guests:
		guest_assignment = random.choice(task_list)
		#if str(my_guests[guest].guest_name) not in assignments:
		assignments[guest_assignment] = str(my_guests[guest].guest_name)
		
		#return redirect('result', pk = my_event.pk, assignments = assignments)

# def result(request, pk, assignments):
# 	my_event = get_object_or_404(MyEvent, pk=pk)
# 	guests = Guest.objects.filter(related_event = my_event)
# 	number_of_guests = range(my_event.number_of_guests)
	return render(request, 'goha/assignments.html', {'assignments': assignments}, )




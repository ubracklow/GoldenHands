import random 
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.core.mail import send_mail
from django.forms.models import inlineformset_factory
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.core.mail import EmailMessage
from .models import Event, Guest, Host
from .forms import EventForm, GuestForm, HostForm

# Create your views here.

def event(request):
	''' takes number of guests, date and location for the event'''
	if request.method == 'POST':		
		form = EventForm(request.POST)
		if form.is_valid():
			new_event = form.save()
			return redirect ('host', pk = new_event.pk)
		else: 
			form = EventForm()
			return render(request, 'goha/event.html', {'form': form})
	else: 
		form = EventForm()
		return render(request, 'goha/event.html', {'form': form})


def host(request, pk):
	''' takes host info '''
	event = get_object_or_404(Event, pk=pk)
	if request.method == 'POST':		
		form = HostForm(request.POST)
		if form.is_valid():
			new_host = form.save(commit = False)
			related_event = Event.objects.filter(pk=pk)
			new_host.related_event=related_event[0]
			new_host.save()
			return redirect ('guests', pk = event.pk)
		else: 
			form = HostForm()
			return render(request, 'goha/host.html', {'form': form})
	else: 
		form = HostForm()
		return render(request, 'goha/host.html', {'form': form})


def guests(request, pk):
	''' takes guest info with a formset depending on number of guests entered for the event'''
	event = get_object_or_404(Event, pk=pk)
	number_of_guests = event.number_of_guests
	GuestInlineFormSet = inlineformset_factory(Event, Guest, fields = ('guest_name', 'guest_email'), labels = {'guest_name' : ('Enter the name of your guest'), 'guest_email' : ('Enter his/ her E-Mail Address'),}, extra = number_of_guests, can_delete = False)
	if request.method == 'POST':
		formset = GuestInlineFormSet(request.POST, instance = event)
		if formset.is_valid():		
			new_guest = formset.save()
			return redirect('assignment_email', pk = event.pk )
			#return render (request, 'goha/assignments.html', {})
	else: 
		formset = GuestInlineFormSet(instance = event)
		return render(request, 'goha/guests.html', {'formset': formset})
		#return render_to_response('goha/guests.html', {'formset': formset}, context = RequestContext(request))


def assignment_email(request, pk):
	''' collates information of event, guests, host
		assigns tasks depending on host choice, 
		sends email to guests and host'''

	event = get_object_or_404(Event, pk=pk)
	guests = Guest.objects.filter(related_event = pk)
	host = Host.objects.get(related_event = pk)

	tasks = ['salty', 'sweet', 'to drink']

	if host.host_choice == "IDC":		
		task_list = ['salty', 'sweet', 'to drink']
		host_assignment = random.choice(task_list)
		task_list.remove(host_assignment)

		while len(task_list) < (event.number_of_guests + 1):
			task_list.append(random.choice(tasks))

		for guest in guests:
			guest_assignment = random.choice(task_list)
			task_list.remove(guest_assignment)
			guest.guest_task = guest_assignment
			guest.save()

		to = []
		to.append(host.host_email)
		for guest in guests:
			to.append(guest.guest_email)
		
		from_email = 'golden.hands.berlin@gmail.com'
		subject = 'Our next Meeting'
		ctx = {'event' : event, 'guests' : guests, 'host' : host, 'host_assignment' : host_assignment }	
		message = get_template('goha/email_template.html').render(Context(ctx)) 	
		
		
		msg = EmailMessage(subject, message, to = to, from_email = from_email)	
		msg.content_subtype = 'html'
		msg.send()

		return render (request, 'goha/assignment_email.html', {'event' : event, 'guests' : guests, 'host' : host, 'host_assignment' : host_assignment})

	else:
		task_list = ['salty', 'sweet', 'to drink']
		if host.host_choice == 'SA':
			host_assignment = 'salty'
			task_list.remove('salty')			
		elif host.host_choice == 'SW':
			host_assignment = 'sweet'
			task_list.remove('sweet')
		elif host.host_choice == 'DR':
			host_assignment = 'to drink'
			task_list.remove('to drink')

		while len(task_list) < (event.number_of_guests):
			task_list.append(random.choice(tasks))
	
		for guest in guests:
			guest_assignment = random.choice(task_list)
			task_list.remove(guest_assignment)
			guest.guest_task = guest_assignment
			guest.save()
		
		to = []
		to.append(host.host_email)
		for guest in guests:
			to.append(guest.guest_email)
		
		from_email = 'golden.hands.berlin@gmail.com'
		subject = 'Our next Meeting'
		ctx = {'event' : event, 'guests' : guests, 'host' : host, 'host_assignment' : host_assignment }	
		message = get_template('goha/email_template.html').render(Context(ctx)) 	
		
		
		msg = EmailMessage(subject, message, to = to, from_email = from_email)	
		msg.content_subtype = 'html'
		msg.send()

		return render (request, 'goha/assignment_email.html', {'event' : event, 'guests' : guests, 'host' : host, 'host_assignment' : host_assignment})



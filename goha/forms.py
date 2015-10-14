from django import forms
from .models import Event, Guest, Host
from datetimewidget.widgets import DateTimeWidget


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('location', 'date_time', 'number_of_guests')
        labels = {'location' : ('Where?'), 'date_time' : ('When?'), 'number_of_guests' : ('How many guests are you inviting?'), }
    date_time = forms.DateTimeField(widget=DateTimeWidget(usel10n=True, bootstrap_version=3))


class HostForm(forms.ModelForm):

    class Meta:
        model = Host
        fields = ('host_name', 'host_email', 'host_choice')
        labels = {'host_name' : ('Your Name'), 'host_email' : ('Your E-Mail Address'), 'host_choice' : ('What would you like to bring?')}

class GuestForm(forms.ModelForm):

	class Meta:
		model = Guest
		fields = ('guest_name', 'guest_email')
		labels = {'guest_name' : ('Name of the guest'), 'guest_email' : ('E-Mail Address'),}



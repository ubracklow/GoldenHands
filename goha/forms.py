from django import forms
from .models import MyEvent, Guest
from datetimewidget.widgets import DateTimeWidget


class EventForm(forms.ModelForm):

    class Meta:
        model = MyEvent
        fields = ('host_name', 'host_email', 'date_time', 'location', 'number_of_guests')
        labels = {'host_name' : ('Who are you - hostess with the mostess?'), 'host_email' : ('Your E-Mail Address'), 'date_time' : ('When?'), 'location' : ('Where?'), 'number_of_guests' : ('How many guests are you inviting?'), }
    date_time = forms.DateTimeField(widget=DateTimeWidget(usel10n=True, bootstrap_version=3))

class GuestForm(forms.ModelForm):

	class Meta:
		model = Guest
		fields = ('guest_name', 'guest_email')
		labels = {'guest_name' : ('Name'), 'guest_email' : ('E-Mail Address'),}


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
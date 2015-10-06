from django import forms
from .models import MyEvent, Guest
from datetimewidget.widgets import DateTimeWidget

class EventForm(forms.ModelForm):

    class Meta:
        model = MyEvent
        fields = ('host_name', 'host_email', 'date_time', 'location', 'number_of_guests')
        labels = {'host_name' : ('What\'s your name - hostess with the mostess?'), 'host_email' : ('Your E-Mail Address'), 'date_time' : ('When?'), 'location' : ('Where?'), 'number_of_guests' : ('How many guests are you inviting?'), }
    date_time = forms.DateTimeField(widget=DateTimeWidget(usel10n=True, bootstrap_version=3))

   
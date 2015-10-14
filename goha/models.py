from django.db import models

# Create your models here.
class Event(models.Model):
	date_time = models.DateTimeField()
	location = models.CharField(max_length=250)
	number_of_guests = models.IntegerField()

	def __str__(self):
		return self.location

class Host(models.Model):
	related_event = models.ForeignKey(Event)
	host_name = models.CharField(max_length=50)
	host_email =  models.EmailField(max_length=254)
	TASK_CHOICES = (
		("SA", "Salty"),
		("SW", "Sweet"),
		("DR", "Drink"),
		("IDC", "I dont care"),
		)
	host_choice = models.CharField(max_length=3, choices=TASK_CHOICES)
	
def __str__(self):
		return self.host_name

class Guest(models.Model):
	related_event = models.ForeignKey(Event)
	guest_name = models.CharField(max_length=50)
	guest_email = models.EmailField(max_length=254)
	guest_task = models.CharField(max_length=50, blank = True)
	
	def __str__(self):
		return self.guest_name


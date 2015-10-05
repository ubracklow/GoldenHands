from django.db import models

# Create your models here.
class MyEvent(models.Model):
	event_name = models.CharField(max_length=200)
	date_time = models.DateTimeField()
	location = models.CharField(max_length=250)
	number_of_guests = models.IntegerField()

	def __str__(self):
		return self.event_name

class Host(models.Model):
	related_event = models.ForeignKey(MyEvent)
	host_name = models.CharField(max_length=50)
	host_email =  models.EmailField(max_length=254)

	def __str__(self):
		return self.host_name

class Guest(models.Model):
	related_event = models.ForeignKey(MyEvent)
	guest_name = models.CharField(max_length=50)
	guest_email = models.EmailField(max_length=254)

	def __str__(self):
		return self.guest_name

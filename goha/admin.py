from django.contrib import admin
from .models import MyEvent, Guest, Host

admin.site.register(MyEvent)

admin.site.register(Guest)

admin.site.register(Host)

# Register your models here.

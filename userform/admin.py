from django.contrib import admin

# Register your models here.
from .models import Hotelinfo
from .models import Roominformation,Bookingdetails1

admin.site.register(Hotelinfo)
admin.site.register(Roominformation)
admin.site.register(Bookingdetails1)

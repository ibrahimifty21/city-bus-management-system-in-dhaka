from django.contrib import admin
from django.contrib.admin.decorators import action
from django.http import HttpResponse

from .models import Album, Announcement, ApplyHalf, Blog, BusCompany, Bus, Fileup, Review, Route, RouteDetails, StaffInfo, Ticket, TimeSlot, Track, User, UserEmail  
# Register your models here.


admin.site.register(User)
admin.site.register(BusCompany)
admin.site.register(Route)



admin.site.register(Bus)


class TicketAdmin(admin.ModelAdmin):
    search_fields = ("pickup__startswith","destination__startswith" )
    list_filter = ("created","time","busname")
     
class TimeSlotAdmin(admin.ModelAdmin):
    search_fields = ("bus_name__name__startswith","bus_at_now__name__startswith" )
    list_filter = ("time","bus_name","bus_at_now")

admin.site.register(Ticket,TicketAdmin)


admin.site.register(TimeSlot,TimeSlotAdmin)
admin.site.register(RouteDetails)
admin.site.register(Fileup)
admin.site.register(ApplyHalf)
admin.site.register(Review)
admin.site.register(Announcement)
admin.site.register(UserEmail)
admin.site.register(Blog)
admin.site.register(StaffInfo)



admin.site.site_header = "CityBus Management System"
admin.site.site_title = "CityBus Admin Portal"
admin.site.index_title = "Welcome to CityBus Management System Portal"












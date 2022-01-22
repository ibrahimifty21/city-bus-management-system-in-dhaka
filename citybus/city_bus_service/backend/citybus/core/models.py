from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.base import Model
from geopy.geocoders import Nominatim
from django.db.models import Q
from django.conf import settings
from django.core.mail import send_mail

from django.dispatch import receiver
from django.db.models.signals import post_save
from django.dispatch import receiver
from tinymce.models import HTMLField

geolocator = Nominatim(user_agent="city_bus")

class UserEmail(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
# Create your models here.
class User(AbstractUser):
    def save(self,*args,**kwargs):
        UserEmail.objects.create(email = self.email)
        subject = 'welcome to Sohochor'
        message = f'Hi 🙋 {self.username}, Thank you for registering in Sohochor. We always wish you safe journey . Please stay with us 🥰'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [self.email, ]
        send_mail( subject, message, email_from, recipient_list )
        super().save(*args,**kwargs) 

class BusCompany(models.Model):
    company_name = models.CharField(max_length=30)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,null=True,default='')
    market_value = models.FloatField(null=True,blank=True)
    description = models.TextField(default='')

    def __str__(self):
        return self.company_name


    
class Route(models.Model):
    name = models.CharField(max_length=300,blank=True,editable=False)
    longitude = models.CharField(max_length=50,null=True,blank=True)
    latitude = models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return f'{self.id} | {self.name}|{self.latitude}|{self.latitude}'

    def save(self,*args,**kwargs):
        location = geolocator.reverse(f'{self.longitude},{self.latitude}',language='en')
        
        self.name = location.address
        super().save(*args,**kwargs)

class Bus(models.Model):
    name = models.CharField(max_length=30)
    available_seat = models.IntegerField(default=0)
    seat_each_row = models.IntegerField(default=0)
    description = models.TextField(blank=True,null=True)
    owner = models.ForeignKey('BusCompany',on_delete=models.CASCADE)
    stuff = models.ManyToManyField(User)
    license_number = models.CharField(max_length=30,unique=True)


    def __str__(self):
        return self.name




class TimeSlot(models.Model):
    bus_name = models.ForeignKey('Bus',on_delete=models.CASCADE,related_name='bus_name')
    bus_at_now = models.ForeignKey('Route',on_delete=models.CASCADE,related_name='route_name')
    station_serial = models.IntegerField()
    trip_number = models.IntegerField()
    time = models.TimeField()

    class Meta:
        ordering = ['bus_name','trip_number','station_serial','time']

    def save(self,*args,**kwargs):
        
        check = TimeSlot.objects.filter(
            Q(bus_name__name__exact = self.bus_name) & Q(time__exact = self.time) 
        )
        if check:
            print('wrong')
        else:        
            super().save(*args,**kwargs)
    def __str__(self):
        return f'{self.bus_name} | station serial:{self.station_serial} | trip_number {self.trip_number} |{self.time} |  {self.bus_at_now}'
            

        
        
        
       

class Ticket(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    pickup = models.CharField(max_length=500)
    destination = models.CharField(max_length=500)
    busname = models.CharField(default='',max_length=500)
    time = models.TimeField()
    created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'{self.id} | {self.pickup} | {self.destination}'



class Album(models.Model):
    album_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)

class Track(models.Model):
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)
    order = models.IntegerField()
    title = models.CharField(max_length=100)
    duration = models.IntegerField()

    class Meta:
        unique_together = ['album', 'order']
        ordering = ['order']

    def __str__(self):
        return f'{self.order} : {self.title}'


class RouteDetails(models.Model):
    route = models.ManyToManyField(TimeSlot)

class Fileup(models.Model):
    files = models.FileField(blank=False,null=False)

class ApplyHalf(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    message = models.TextField(null=True,blank=True)
    file = models.FileField(blank=False,null=False)
    created = models.DateTimeField(auto_now=True,blank=True)
    confirm = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created']


class Review(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    review = models.TextField()
    created = models.DateTimeField(auto_now=True,blank=True)

    class Meta:
        ordering = ['-created']


from django.template.loader import render_to_string  
from django.core.mail import EmailMultiAlternatives  
class Announcement(models.Model):
    message = models.TextField(null=True,blank=True)
    created = models.DateTimeField(auto_now=True)

    def save(self,*args,**kwargs):
        recievers = []
        for user in UserEmail.objects.all():
            recievers.append(user.email)
        
        subject, from_email, to ='Announcement from Sohochor', settings.EMAIL_HOST_USER, recievers
        message = self.message
        
        
        msg = EmailMultiAlternatives(subject,message,from_email, to)
        
        msg.send()
        super().save(*args,**kwargs) 
    

    class Meta:
        ordering = ['-created']


class Blog(models.Model):
    title = models.CharField(max_length=300)
    short_description = models.TextField()
    content = HTMLField()
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']


class StaffInfo(models.Model):
    user = models.ForeignKey('User',on_delete=models.CASCADE)
    bus_company = models.ForeignKey('Bus',on_delete=models.CASCADE)
    salary = models.IntegerField()
    description = HTMLField()

    def __str__(self):
        return self.user.username


    
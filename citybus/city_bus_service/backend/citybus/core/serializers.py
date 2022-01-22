from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import ApplyHalf, Blog, Bus, Fileup, Review, RouteDetails, Ticket, TimeSlot,Route,Album,Track,StaffInfo



class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = ['name']
class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = '__all__'



class TimeSlotSerializer(serializers.ModelSerializer):
    bus = BusSerializer(read_only=True)
    route = RouteSerializer(many=True,read_only=True)
    bus_id = serializers.SerializerMethodField()
    name_of_bus = serializers.SerializerMethodField()
    route_id = serializers.SerializerMethodField()
    longitude = serializers.SerializerMethodField()
    latitude = serializers.SerializerMethodField()
    name_of_route = serializers.SerializerMethodField()
    time = serializers.TimeField(format="%I:%M %p")

    def get_name_of_bus(self,obj):
        return obj.bus_name.name
    def get_name_of_route(self,obj):
        return obj.bus_at_now.name
    def get_route_id(self,obj):
        return obj.bus_at_now.id
    def get_bus_id(self,obj):
        return obj.bus_name.id
    def get_longitude(self,obj):
        return obj.bus_at_now.longitude
    def get_latitude(self,obj):
        return obj.bus_at_now.latitude
        

    class Meta:
        model = TimeSlot
        fields = ['route','bus','id','bus_id','name_of_bus','route_id','name_of_route','longitude','latitude','station_serial','trip_number','time']


class RouteDetailsSerializer(serializers.ModelSerializer):
    
    
    
    class Meta:
        model = RouteDetails
        fields = ['id','route']
        depth=1
        
class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['order', 'title', 'duration']

class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ['album_name', 'artist', 'tracks']

class TicketSerializer(serializers.ModelSerializer):
    time = serializers.TimeField(format="%I:%M %p")
    class Meta:
        model = Ticket
        fields = ['id','user','busname','pickup','destination','time',]

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fileup
        fields = '__all__'

class ApplyHalfSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplyHalf
        fields = ['user','message','file',]


class ReviewSerializer(serializers.ModelSerializer):
    
    user_name = serializers.SerializerMethodField()

    def get_user_name(self,obj):
        return obj.user.username
    class Meta:
        model = Review
        fields = ['id','user','user_name','review',]


class BlogViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields=['id','title','short_description',]

class BlogDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id','title','short_description','content']

class StaffInfoSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    bus_company = serializers.SerializerMethodField()


    def get_name(self,obj):
        return obj.user.username

    def get_bus_company(self,obj):
        return obj.bus_company.name
    
    class Meta:
        model = StaffInfo
        fields = ['id','name','bus_company','salary','description']


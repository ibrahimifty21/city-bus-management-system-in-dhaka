from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser

from core import serializers
from .models import Album, Blog, Review, Route, RouteDetails, StaffInfo, Ticket, TimeSlot
from django.db.models import Q
from rest_framework import status,viewsets
from .serializers import AlbumSerializer, ApplyHalfSerializer, BlogDetailsSerializer, BlogViewSerializer, FileSerializer, ReviewSerializer, RouteSerializer, StaffInfoSerializer, TicketSerializer, TimeSlotSerializer,RouteDetailsSerializer
from geopy import distance
import datetime
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

@api_view(['GET'])
def home(request,**kwargs):
    if request.method == 'GET':
        album = Album.objects.all()
        print(kwargs)
        serializer_context = {
            'request': request,
        }
        serializers = AlbumSerializer(album,many=True, context=serializer_context)
    return Response(serializers.data)

@api_view(['POST'])
def pickup(request):

    location = request.data['pickup']
    
    try:
        result = TimeSlot.objects.filter(

            Q(bus_at_now__name__icontains = location) & Q(station_serial__exact=1)).distinct()
        print(result)
        serializers = TimeSlotSerializer(result,many=True)
        return Response({"status": "success", "data": serializers.data}, status=status.HTTP_200_OK)
    except TimeSlot.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def destination(request):
    bus_id = request.data['bus_id']
    serial_number = int(request.data['serial_number'])
    trip_number = request.data['trip_number']

    
    try:
        obj = TimeSlot.objects.filter(
            Q(bus_name__id__exact=bus_id) & Q(station_serial__gt=serial_number) &  Q(trip_number__exact = trip_number)
            #Q(bus_at_now__id = bus_id) and Q(station_serial__gt=2) and Q(trip_number__exact = trip_number)
        ).order_by('station_serial')
        
        serializers = TimeSlotSerializer(obj,many=True)
        return Response({"status": "success", "data": serializers.data}, status=status.HTTP_200_OK)

        
    except TimeSlot.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)




@api_view(['GET'])
def check(request):
    pickup_longitude = request.GET.get('pickup_longitude',None)
    pickup_latitude = request.GET.get('pickup_latitude',None)
    destination_longitude = request.GET.get('destinantion_longitude',None)
    destination_latitude = request.GET.get('destinantion_latitude',None)

    pickup = (pickup_longitude,pickup_latitude)
    destination = (destination_longitude,destination_latitude)

    km = int(distance.distance(pickup,destination).km)/10000

    return JsonResponse({
        'distance':km
    })

@api_view(['GET'])
def route_details(request):
    obj = RouteDetails.objects.all()
    
    
    serializers = RouteDetailsSerializer(obj,many=True)
    return Response({"status": "success", "data": serializers.data}, status=status.HTTP_200_OK)


@api_view(['GET'])
def route_name(request):
    obj = Route.objects.all().order_by('name')
    
    serializers = RouteSerializer(obj,many=True)
    return Response({"status": "success", "data": serializers.data}, status=status.HTTP_200_OK)

@api_view(['GET'])
def signle_ticket(request,user_id):
    if request.method == 'GET':

        
        print(user_id)
        obj = Ticket.objects.filter(user_id__id = user_id )
        print(obj)
        if obj:
            serializers = TicketSerializer(obj,many=True)
            return Response({"status": "success", "data":serializers.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "success", "data":"There is no ticket yet"}, status=status.HTTP_200_OK)
from django.template.loader import render_to_string 

@api_view(['POST','PUT'])
def ticket(request):

    
    if request.method == 'POST':
        serializers = TicketSerializer(data=request.data)
        if serializers.is_valid():
            print(request.user.email)
            pickup = request.data['pickup']
            destination = request.data['destination']
            busName = request.data['busname']
            time = request.data['time']
            # serializers.save()
            # subject, from_email, to = 'Your purchashed ticket information', settings.EMAIL_HOST_USER, request.user.email
            # message = "<p>This is an <strong>important</strong> message.</p>"

            # html_content = message
            # msg = EmailMultiAlternatives(subject,from_email, [to])
            # msg.attach_alternative(html_content, "text/html")
            # msg.send()
            subject, from_email, to = 'Ticket information from Sohochor', settings.EMAIL_HOST_USER, request.user.email
            html = './ticket.html'
            html_msg = render_to_string(html,{
                'pickup':pickup,
                'destination':destination,
                'busname':busName,
                'time':time
            })
            
            
            msg = EmailMultiAlternatives(subject,html_msg,from_email, [to])
            msg.content_subtype = 'html'
            msg.send()
            print('email_send')
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        else:
          return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


    if request.method == 'PUT':
        now = datetime.datetime.now().strftime('%I:%M %p')
        ticket_id = request.data['id']
        time = request.data['time']
        obj = Ticket.objects.get(id=ticket_id)
        print(time>now)
        if(time>now):
            return Response("It can't be done now", status=status.HTTP_400_BAD_REQUEST)
        else:

            if request.user.is_authenticated:
                obj.delete()
                return Response("ok_clear", status=status.HTTP_200_OK)
            else:
                return Response("you have to be logged in ", status=status.HTTP_200_OK)


class FileUpload(APIView):
    parser_class = (FileUploadParser,)
    def post(self,request,*args,**kwargs):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def apply_half(request):
    if request.method == 'POST':
        serializer = ApplyHalfSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def review_limit(request):
    if request.method == 'GET':
        obj = Review.objects.all()[:5]
        if obj:
            serializers = ReviewSerializer(obj,many=True)
            return Response(serializers.data, status=status.HTTP_200_OK)
        else:
            return Response('Sorry,nothing found', status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def review_all(request):
    if request.method == 'GET':
        obj = Review.objects.all()
        if obj:
            serializers = ReviewSerializer(obj,many=True)
            return Response(serializers.data, status=status.HTTP_200_OK)
        else:
            return Response('Sorry,nothing found', status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def review_post(request):
    if request.method == 'POST':
        serializers = ReviewSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET'])
def blogview(request):
    if request.method == 'GET':
        obj = Blog.objects.all()
        if obj:
            serializers = BlogViewSerializer(obj,many=True)
            return Response(serializers.data, status=status.HTTP_200_OK)
        else:
            return Response('Sorry,nothing found', status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def blogDetails(request,id):
    if request.method == 'GET':
        obj = Blog.objects.get(id=id)
        if obj:
            serializers = BlogDetailsSerializer(obj)
        
            return Response(serializers.data,status=status.HTTP_200_OK)
        else:
            return Response('Sorry,nothing found', status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def staffInfo(request):
    if request.method == 'GET':
        obj = StaffInfo.objects.all()
        serializers = StaffInfoSerializer(obj,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)
import requests

def verification(request,uid,token):
    print('hi')
    protocol = 'https://' if request.is_secure() else 'http://'
    web_url = protocol + request.get_host()
    post_url = web_url + "api/auth/users/activate/"
    post_data = {'uid': uid, 'token': token}
    result = requests.post(post_url, data = post_data)
    print('hi')
    return JsonResponse(result)





    




        



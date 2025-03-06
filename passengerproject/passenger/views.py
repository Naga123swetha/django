from django.shortcuts import render
from .models import *
from rest_framework import status
from rest_framework.decorators import api_view
from .serializer import *
from rest_framework.response import Response
# Create your views here.


@api_view(['GET','POST'])
def passenger_list(request):
    if request.method=='GET':
     passengers=Passenger.objects.all()
     serializer=PassengerSerializer(passengers,many=True)
     return Response(serializer.data)
    elif request.method=='POST':
       passengers=request.data
       serializer=PassengerSerializer(data=passengers)
       if serializer.is_valid():
          serializer.save()
          return Response(serializer.data,status=status.HTTP_201_CREATED)
       return Response(serializer.error,status=status.HTTP_404_BAD_REQUEST)

   
@api_view(['GET','PUT','DELETE'])
def passenger_detail(request,pk):
   try:
      passenger=Passenger.objects.get(pk=pk)
   except Passenger.DoesNotExistS:
      return Response(status=status.HHTP_404_NOT_FOUND)
   if request.method=='GET':
      serializer=PassengerSerializer(passenger)
      return Response(serializer.data)
   elif request.method=='PUT':
      serializer=PassengerSerializer(passenger,data=request.data)
      if serializer.is_valid():
         serializer.save()
      return Response(serializer.data)
   elif request.method=='DELETE':
       serializer=PassengerSerializer(passenger,data=request.data)
       if serializer.is_valid():
         passenger.delete()
       return Response(serializer.data)
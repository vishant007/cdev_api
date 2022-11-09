from urllib import response
from django.shortcuts import render,redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Q
import socket
from .models import Advocate,company
from .serializers import AdvocateSerializer, companySerializer
from base import serializers



@api_view(['GET'])
def endpoints(request):
    data = ['/advocates', '/advocates/:username']
    return Response(data)

@api_view(['GET','POST'])
# for the authentication purpose 
# @permission_classes([IsAuthenticated])
def advocates_list(request):
 
    if request.method=='GET':
        query = request.GET.get('query')
   
        if query == None:
            query = ''

        advocates = Advocate.objects.filter(Q(username__icontains=query) | Q(bio__icontains=query))
        serializer = AdvocateSerializer(advocates, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        advocate = Advocate.objects.create(
            username=request.data['username'],
            bio=request.data['bio']
        )

        serializer=AdvocateSerializer(advocate,many=False)

        return response(serializer.data)
   




@api_view(['GET','PUT','DELETE'])
def advocate_details(request, username):
    advocate=Advocate.objects.get(username=username)
    if request.method=='GET':
        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)

    if request.method=='PUT':
        advocate.username = request.data['username'],
        advocate.bio = request.data['bio']

        advocate.save()

        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)    

    if request.method == 'DELETE':
        advocate.delete()
        return Response('user was deleted')


@api_view(['GET'])
def companies_lists(request):
    companies = company.objects.all()
    serializer = companySerializer(companies,many=True)
    return Response(serializer.data)
from django.urls import path
from . import models
from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.urls import path
from django.conf.urls import url, include
from django.views import generic
from django.core import serializers
from . import views
import json

@api_view(['GET'])
def allData(request):
    qs = models.Site.objects.all()
    print(qs)
    return Response({"data":serializers.serialize('json',list(qs),)})

@api_view(['POST'])
def Complexes(request):
    qs = models.Complex.objects.all()
    print(qs)
    input = json.loads(request.body)
    print(input)
    print(input['xid'])
    return Response({"data":serializers.serialize('json',list(qs),)})

@api_view(['POST'])
def Facilities(request):
    qs = models.Facility.objects.all()
    print(qs)
    input = json.loads(request.body)
    print(input)
    print(input['xid'])
    return Response({"data":serializers.serialize('json',list(qs),)})

@api_view(['POST'])
def Equipment(request):
    qs = models.Equipment.objects.all()
    print(qs)
    input = json.loads(request.body)
    print(input)
    print(input['xid'])
    return Response({"data":serializers.serialize('json',list(qs),)})

@api_view(['POST'])
def Details(request):
    qs = models.Detail.objects.all()
    print(qs)
    input = json.loads(request.body)
    print(input)
    print(input['xid'])
    return Response({"data":serializers.serialize('json',list(qs),)})

@api_view(['POST'])
def WorkItems(request):
    qs = models.WorkItem.objects.all()
    print(qs)
    input = json.loads(request.body)
    print(input)
    print(input['xid'])
    return Response({"data":serializers.serialize('json',list(qs),)})

urlpatterns = [
    url('all/$', allData),
    url('complexes/$', Complexes),
    url('facilities/$', Facilities),
    url('equipment/$', Equipment),
    url('details/$', Details),
    url('workitems/$', WorkItems)
    #path('', views.index, name='index'),
    #path('<int:FacilityID_id>/', views.detail, name='detail'),
]

from django.shortcuts import render, redirect

from .models import Location
from .models import Camera
from .models import Camerachoose


def index(request):
    return (render(request, 'index.html'))


def addlocation(request):
    return (render(request, 'newlocation.html'))


def addcamera(request):
    return (render(request, 'newcamera.html'))


def do_location(request):
    form = Location(Loc_Name=request.GET['name'], Loc_Address=request.GET['add'], Loc_Survelliance=request.GET['sur'],
                    Loc_Area=request.GET['area'])
    form.save()
    return redirect('/showlocation')


def showlocation(request):
    form = Location.objects.order_by('id')
    return (render(request, 'showlocation.html', {'form': form}))

def do_camera(request):
    form= Camera(Camera_Name=request.GET['name'],Camera_Brand=request.GET['brand'],Camera_Details=request.GET['detail'])
    form.save()
    form1=Camerachoose(Cameraname=request.GET['name'])
    form1.save()
    return (redirect('/showcamera'))

def showcamera(request):
    form = Camera.objects.order_by('id')
    return (render(request, 'showcamera.html', {'form': form}))

def assigncamera(request):
    form=Camerachoose.objects.order_by('id')
    form1=Location.objects.order_by('id')
    return (render(request,'assigncamera.html',{'form':form,'form1':form1}))

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .forms import containerForm
from .models import Container
import json

def index(request):
    return render(request, 'templates/smain.html')


@csrf_exempt
def container_input(request):
    form = containerForm(request.POST)
    ContainerID = request.POST['ContainerID']
    print(ContainerID)

    if form.is_valid():
        print(ContainerID)
        upda = Container.objects.filter(ContainerID=request.POST['ContainerID'])
        print(upda)
        if len(upda) == 0:
            form.save()
        else:
            upda = Container.objects.get(ContainerID=request.POST['ContainerID'])
            upda.ContainerID = request.POST['ContainerID']
            upda.PortID = request.POST['PortID']
            upda.PortName = request.POST['PortName']
            upda.PortExportDate = request.POST['PortExportDate']
    return HttpResponse("success")

@csrf_exempt
def sensor(request):
    print("sex")
    han = request.POST.dict()


    return HttpResponse("seccess")









def container_list(request):
    cons = Container.objects.all()
    return render(request, 'templates/detail222.html',{'cons':cons})

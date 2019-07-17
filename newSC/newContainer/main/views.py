from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .forms import containerForm
from .models import Container

def index(request):
    return render(request, 'templates/main.html')


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
def containerdetail(request):
    form = containerForm(request.POST)
    ContainerID = request.POST["ContainerID"]
    print(ContainerID)

    return HttpResponse("success")
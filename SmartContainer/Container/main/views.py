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
            upda.SizeType = request.POST['SizeType']
            upda.TotalWeight = request.POST['TotalWeight']
            upda.Section = request.POST['Section']
            upda.MBLNum = request.POST['MBLNum']
            upda.Msn = request.POST['Msn']
            upda.GoodsClassfiy = request.POST['GoodsClassfiy']
            upda.Pol = request.POST['Pol']
            upda.LeavePlace = request.POST['LeavePlace']
            upda.LeaveClassfiy = request.POST['LeaveClassfiy']
            upda.LoadID = request.POST['LoadID']
            upda.GoodsName = request.POST['GoodsName']
    return HttpResponse("success")

@csrf_exempt
def sensor(request):
    han = request.POST.dict()


    return HttpResponse("success")









def container_list(request):
    cons = Container.objects.all()
    return render(request, 'templates/detail222.html',{'cons':cons})

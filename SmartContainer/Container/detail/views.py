from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from main.models import Container
from . import models
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


# def ContainerDetail(request):
#    template = 'detail222.html'
#    Detail_data = Detail.objects.all()
#
#    return render(request, template)

@csrf_exempt
def ContainerDetail(request):
    Detail_data = Container.objects.all()
    upupda = {'Detail_data': Detail_data}
    return render(request, 'templates/detail222.html', upupda)

@csrf_exempt
def DetailTest(request):
    Num = request.POST['ConID']
    print(Num)
    return render(request, 'Detail.html', {'ConID': Num})




#@csrf_exempt
#def containerdetail(request):
#    if request.method == 'GET':
#        Container_list = ContainerDetail.objects.all()
#        Containers=[]
#        for cont in Container_list:
#            Containers.append({"ContainerID": cont.ContainerID, "PortID": cont.PortID, "PortName": cont.PortName,
#                               "PortExportDate": cont.PortExportDate})

#    return JsonResponse(Containers)
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.



@csrf_exempt
def Control(request):
    Num = request.POST['ConID']
    return render(request, 'Control.html', {'ConID': Num})




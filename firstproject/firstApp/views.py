from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from .models import *

def employeeView(request):
    emp={
        'id':123,
        'name':'John',
        'sal':100000
    }
    data=Employee.objects.all();
    response={'employees':list(data.values('name','sal'))}

    return JsonResponse(response)
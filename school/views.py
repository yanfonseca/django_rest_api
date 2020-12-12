# from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse


def students(request):
    if request.method == 'GET':
        student = {
            'id':1, 
            'name':'Yan'
        }

        return JsonResponse(student)
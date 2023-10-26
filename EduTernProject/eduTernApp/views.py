from django.shortcuts import render
from django.http import JsonResponse
from .models import StudentDetail
from .serializers import StudentDetailSerilizer
from rest_framework.decorators import api_view

# Create your views here.

def studentList(request):
    students=StudentDetail.objects.all()
    serialize=StudentDetailSerilizer(students,many=True)
    return JsonResponse(serialize.data,safe=False)

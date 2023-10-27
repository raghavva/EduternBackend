from django.shortcuts import render
from django.http import JsonResponse
from .models import StudentDetail
from .serializers import StudentRegisterSerializer,StudentDetailSerilizer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

def studentList(request):
    students=StudentDetail.objects.all()
    serialize=StudentDetailSerilizer(students,many=True)
    return JsonResponse(serialize.data,safe=False)


@api_view(['POST'])
def studentRegister(request):
    serializer=StudentRegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)


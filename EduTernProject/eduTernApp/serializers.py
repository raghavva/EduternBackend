from rest_framework import serializers
from .models import StudentInformation,StudentDetail

class StudentDetailSerilizer(serializers.ModelSerializer):
    class Meta:
        model=StudentDetail
        fields=['email','password','studentDOB']

class StudentRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentInformation
        fields=['studentName','studentEmail','studentPassword','studentDOB','studentPhoneNumber','collegeName','fieldOfStudy','yearOfStudy']
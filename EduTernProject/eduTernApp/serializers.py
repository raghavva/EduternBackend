from rest_framework import serializers
from .models import StudentDetail 

class StudentDetailSerilizer(serializers.ModelSerializer):
    class Meta:
        model=StudentDetail
        fields=['email','password']
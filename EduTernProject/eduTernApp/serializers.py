from rest_framework import serializers
from .models import StudentInformation,StudentDetail,RegistrationInfo,CourseDetails,CoursePricing

class StudentDetailSerilizer(serializers.ModelSerializer):
    class Meta:
        model=StudentDetail
        fields=['email','password','studentDOB']

class StudentRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentInformation
        fields=['studentName','studentEmail','studentPassword','studentDOB','studentPhoneNumber','collegeName','fieldOfStudy','yearOfStudy']

class RegistrationInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=RegistrationInfo
        fields=['studentId','courseId','courseEnrolled','paymentDate','paymentTransactionId','ammountPaid']
        

class CourseDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=CourseDetails
        fields=['courseTitle','courseObjectives','courseDescription','courseOverview','courseRequirements','courseDescription']
    
class CoursePricingSerializer(serializers.ModelSerializer):
    class Meta:
        model=CoursePricing
        fields=['courseId','courseTitle','originalCost','discountPercentage','discountedPrice']

class OrderSerializer(serializers.Serializer):
    amount = serializers.IntegerField()
    currency = serializers.CharField(max_length=3, default="INR")
    receipt = serializers.CharField(max_length=255, default="order_rcptid_11")

class VerifyPaymentSerializer(serializers.Serializer):
    payment_id = serializers.CharField()
    order_id = serializers.CharField()
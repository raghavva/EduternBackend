from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from .models import StudentDetail
from .serializers import StudentRegisterSerializer,StudentDetailSerilizer,CourseDetailsSerializer,RegistrationInfoSerializer,CoursePricingSerializer
from .serializers import OrderSerializer
from .serializers import VerifyPaymentSerializer 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
import razorpay

# Create your views here.
client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

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
    

@api_view(['POST'])
def registrationInfo(request):
    serializer=RegistrationInfoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
@api_view(['POST'])
def courseDetails(request):
    serializer=CourseDetailsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
@api_view(['POST'])
def coursePricing(request):
    serializer=CoursePricingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    

@api_view(['POST'])
def create_order(request):
    serializer = OrderSerializer(data=request.data)

    if serializer.is_valid():
        data = serializer.validated_data
        try:
            order = client.order.create(data)
            return Response(order, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"message": "Order creation failed", "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def verify_payment(request):
    serializer = VerifyPaymentSerializer(data=request.data)

    if serializer.is_valid():
        data = serializer.validated_data
        payment_id = data["payment_id"]
        student_id=data["student_id"]
        course_id=data["course_id"]
        course_enrolled=data["course_enrolled"]
        payment_date=timezone.now().date()

        try:
            payment_info = client.payment.fetch(payment_id)
            ammount=payment_info["amount"]
            if payment_info["status"] == "captured":
                payment_data = {
                    'studentId':student_id,
                    'courseId':course_id,
                    'courseEnrolled':course_enrolled,
                    'paymentDate':payment_date,
                    'paymentTransactionId':payment_id,
                    'ammountPaid':ammount
                }
                payment_serializer = RegistrationInfoSerializer(data=payment_data)
                if payment_serializer.is_valid():
                    payment_serializer.save()
                    return Response({"message": "Payment successful"}, status=status.HTTP_200_OK)
                else:
                    return Response(payment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                # Payment failed
                 return Response({"message": "Payment failed"}, status=status.HTTP_400_BAD_REQUEST)
        except razorpay.errors.BadRequestError:
            return Response({"message": "Payment failed"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

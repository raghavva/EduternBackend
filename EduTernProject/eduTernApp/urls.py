
from django.urls import path
from .views import studentRegister,studentList,courseDetails,registrationInfo,coursePricing,create_order,verify_payment


urlpatterns = [
    path('students/',studentList),
    path('studentRegister/',studentRegister),
    path('courseDetails/',courseDetails),
    path('registrationInfo/',registrationInfo),
    path('coursePricing/',coursePricing),
    path('createOrder/',create_order),
    path('verifyPayment/',verify_payment)
]

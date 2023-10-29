
from django.urls import path
from .views import studentRegister,studentList,courseDetails,registrationInfo,coursePricing


urlpatterns = [
    path('students/',studentList),
    path('studentRegister/',studentRegister),
    path('courseDetails/',courseDetails),
    path('registrationInfo/',registrationInfo),
    path('coursePricing/',coursePricing)
]


from django.urls import path
from .views import studentRegister,studentList
#,

urlpatterns = [
   path('students/',studentList),
    path('studentRegister/',studentRegister)
]

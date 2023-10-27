from django.contrib import admin
from .models import CourseDetails,CoursePricing,StudentInformation,RegistrationInfo,StudentDetail

 

# Register your models here.
admin.site.register(StudentDetail)
admin.site.register(CourseDetails)
admin.site.register(CoursePricing)
admin.site.register(StudentInformation)
admin.site.register(RegistrationInfo)

from django.db import models

# Create your models here.

class StudentDetail(models.Model):
    studentId=models.AutoField(primary_key=True)
    email=models.CharField(max_length=1000)
    password=models.CharField(max_length=1000)
    studentDOB=models.DateField(null=True)

class CourseDetails(models.Model):
    courseId=models.AutoField(primary_key=True)
    courseTitle=models.CharField(max_length=1000)
    courseObjectives=models.TextField()
    courseDescription=models.TextField()
    courseOverview=models.TextField()
    courseRequirements=models.TextField()
    courseDescription=models.TextField()

    def __str__(self) -> str:
        return str(self.courseTitle)
    
#One mistake in coursepricing table - coursetitle must be Foregn key
class CoursePricing(models.Model):
    coursePricingId=models.AutoField(primary_key=True)
    courseId=models.ForeignKey(CourseDetails, on_delete=models.CASCADE)
    courseTitle=models.TextField()
    originalCost=models.IntegerField()
    discountPercentage=models.FloatField()
    discountedPrice=models.FloatField()

    def __str__(self) -> str:
        return str(self.courseTitle)


class StudentInformation(models.Model):
    studentId=models.AutoField(primary_key=True)
    studentName=models.CharField(max_length=1000)
    studentEmail=models.CharField(max_length=1000)
    studentPassword=models.CharField(max_length=1000)
    studentDOB=models.DateField()
    studentPhoneNumber=models.CharField(max_length=12)
    collegeName=models.TextField()
    fieldOfStudy=models.TextField()
    yearOfStudy=models.IntegerField()

    def __str__(self) -> str:
        return str(self.studentName)


class RegistrationInfo(models.Model):
    registrationInfoId=models.AutoField(primary_key=True)
    studentId=models.ForeignKey(StudentInformation, on_delete=models.CASCADE) 
    courseId=models.ForeignKey(CourseDetails, on_delete=models.CASCADE)
    courseEnrolled=models.TextField()
    paymentDate=models.DateField()
    paymentTransactionId=models.TextField()
    ammountPaid=models.IntegerField()

    def __str__(self) -> str:
        return str(self.studentId)




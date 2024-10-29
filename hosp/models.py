from django.db import models

# Create your models here.


class doctor(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.IntegerField()
    special = models.CharField(max_length=100)

    def _str_(self):
        return self.name

class patient(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    mobile = models.IntegerField(null=True)
    address = models.TextField(null=True)

    def _str_(self):
        return self.name

class Appointment(models.Model):
    Doctor = models.ForeignKey(doctor,on_delete=models.CASCADE)
    Patient = models.ForeignKey(patient,on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    disease = models.CharField(max_length=255,null=True)

    def __str__(self):
        return self.Doctor.name+"__"+self.Patient.name
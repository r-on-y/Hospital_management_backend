from django.db import models
from patient.models import Patient
from doctor.models import Doctor,AvailableTime


# Create your models here.

Appointment_Status=[
    ('Completed','Completed'),
    ('Pending','Pending'),
    ('Running','Running')
]

Appointment_Types=[
    ('Offline','Offline'),
    ('Online','Online')
]

class Appoitnment(models.Model):
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)

    appointment_type=models.CharField(choices=Appointment_Types,max_length=10)
    appointment_status=models.CharField(choices=Appointment_Status,max_length=10,default="Pending")

    symptom=models.TextField()

    time=models.OneToOneField(AvailableTime,on_delete=models.CASCADE)

    cancel=models.BooleanField(default=False)

    def __str__(self):
        return f"Doctor {self.doctor.user.first_name}, Patient {self.patient.user.first_name}"





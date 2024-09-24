from django.db import models

# Create your models here.
class PatientData(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=[
        ('M', 'Male'),
        ('F', 'Female'),
    ])
    YELLOW_FINGERS = models.IntegerField()
    ANXIETY = models.IntegerField()
    PEER_PRESSURE = models.IntegerField()
    CHRONIC_DISEASE = models.IntegerField()
    FATIGUE = models.IntegerField()
    ALLERGY = models.IntegerField()
    WHEEZING = models.IntegerField()
    ALCOHOL_CONSUMING = models.IntegerField()
    COUGHING = models.IntegerField()
    SWALLOWING_DIFFICULTY = models.IntegerField()
    CHEST_PAIN = models.IntegerField()
    ANXYELFIN = models.IntegerField()
    probability = models.CharField(null=True, blank=True,max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
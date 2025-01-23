from django.db import models

class EventRegistration(models.Model):
    timestamp = models.DateTimeField()
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    interest_level = models.CharField(max_length=50)
    feedback = models.TextField()

    def __str__(self):
        return self.name
    
    
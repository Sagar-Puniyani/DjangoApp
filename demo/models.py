from django.db import models
from django.utils import timezone

# Create your models here.

class Varitey(models):
    VARITRY_OF_CHOICE = [
        ('DL','DEEP_LEARNING'),
        ('ML','MACHINE_LEARNING')
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Images/')
    date = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2,choices=VARITRY_OF_CHOICE)

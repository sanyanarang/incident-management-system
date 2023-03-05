from django.db import models
# importing user model, signal and dispatcher
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
from datetime import datetime
PRIORITY_CHOICES = [
    ('low', 'Low'),
    ('medium', 'Medium'),
    ('high', 'High'),
]
STATUS_CHOICES = [
    ('open', 'Open'),
    ('in_progress', 'In Progress'),
    ('closed', 'Closed'),
]
class Incident(models.Model):
    reporter_name = models.ForeignKey(User, on_delete=models.CASCADE)
    incident_detail = models.TextField(max_length=1024, blank=False, null=False)
    reported_date = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(choices=PRIORITY_CHOICES, blank=False, null=False, max_length=20)
    status = models.CharField(choices=STATUS_CHOICES, blank=False, null=False,max_length=20)
    incident_id = models.CharField(max_length=12, blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Call the "real" save() method.
        # now we have id generated, use id to get unique incident no
        self.incident_id = generate_unique_incident_id(str(self.id))
        super().save(*args, **kwargs)  # Call the "real" save() method.
    
    def __str__(self) -> str:
        return str(self.id);

def generate_unique_incident_id(id:str):
    # RMG, ID, year
    if(len(id)>5):
        # meaning we already have enough data
        id = id[:5]
    else:
        id = '00000'[:5-len(id)]+id
    year = datetime.now().year
    # print(f'RMG{id}{year}', 'final val')
    return f'RMG{id}{year}'
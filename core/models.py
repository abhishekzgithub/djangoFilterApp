from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from localflavor.in_.models import INStateField
import datetime
# Create your models here.

CLASS_CHOICES = (
    ('low','A'),
    ('moderate', 'B'),
    ('high','C'))

USER_CHOICES = (
    ('user','USER'),
    ('admin','ADMIN'),
    ('guest','GUEST'),
    ('user1','USER1'),
    
)
class Rating(models.Model):
    classtype=models.CharField(max_length=10, choices=CLASS_CHOICES, default='HIGH')
    rate=models.FloatField(
        validators=[MinValueValidator(0.1), MaxValueValidator(1.0)],help_text="Input should be in range of 0.1 to 1.0 only")
    exposure_unit=models.PositiveIntegerField(null=False,blank=False,default=0)
    date=models.DateField(auto_now_add=False, null=False,default=datetime.date.today,
                          help_text="Input should be in YYYY-MM-DD format")
    state = INStateField(null=False,blank=False,default="Goa")
    user = models.CharField(max_length=6, choices=USER_CHOICES, default='GUEST')
    
    @property
    def calculate_premium(self):
        return (self.rate)*(self.exposure_unit)
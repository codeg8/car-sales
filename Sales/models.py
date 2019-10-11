from django.db import models
from django.core.validators import MaxValueValidator
# Create your models here.

MAX_SELLING_PRICE = 100000
class Sale(models.Model):

    FUEL_CHOICES = (('CNG', 'CNG'), ('Petrol', 'Petrol'), ('Diesel', 'Diesel'))
    VEHICLE_SEGMENT_CHOICES = (('A', 'A'), ('B', 'B'), ('C', 'C'))
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'))
    CUSTOMER_INCOME_GROUP_CHOICES = (('0- $25K', '0- $25K'), ('$25-$70K', '$25-$70K'), ('>$70K', '>$70K'))
    REGION_CHOICES = (('N', 'North'), ('S', 'South'), ('E', 'East'), ('W', 'West'))
    CUSTOMER_MARITAL_STATUS_CHOICES = (('1', 'Married'), ('0', 'Unmarried'))

    id = models.fields.BigIntegerField(primary_key=True, verbose_name="Sale ID", auto_created=True)
    dop = models.fields.DateField(verbose_name='Date of Purchase')
    customer_id = models.fields.BigIntegerField()
    fuel = models.fields.CharField(max_length=10, choices=FUEL_CHOICES)
    vehicle_segment = models.fields.CharField(max_length=1, choices=VEHICLE_SEGMENT_CHOICES)
    selling_price = models.fields.FloatField(validators=[MaxValueValidator(MAX_SELLING_PRICE)])
    power_steering = models.fields.BooleanField()
    airbags = models.fields.BooleanField()
    sunroof = models.fields.BooleanField()
    matt_finish = models.fields.BooleanField()
    music_system = models.fields.BooleanField()
    customer_gender = models.fields.CharField(max_length=10, choices=GENDER_CHOICES)
    customer_income_group = models.fields.CharField(max_length=10, choices=CUSTOMER_INCOME_GROUP_CHOICES)
    customer_region = models.fields.CharField(max_length=10, choices=REGION_CHOICES)
    customer_marital_status = models.fields.CharField(max_length=1, choices=CUSTOMER_MARITAL_STATUS_CHOICES)

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AmsUserProfile(models.Model):
    date_of_birth = models.DateField(null=True)
    mobile_number = models.CharField(null=True, max_length=15)
    phone_number = models.CharField(null=True, max_length=15)
    address_line_1 = models.CharField(null=True, max_length=255)
    address_line_2 = models.CharField(null=True, max_length=255)
    city = models.CharField(null=True, max_length=100)
    state = models.CharField(null=True, max_length=100)
    postal_code = models.CharField(null=True, max_length=15)
    country = models.CharField(null=True, max_length=100)
    profile_picture = models.TextField(null=True)
    belongs_to_ams_user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "ams_user_profiles"



class AmsCompanyProfile(models.Model):
    name = models.CharField(null=True, max_length=255)
    pan = models.CharField(null=True, max_length=20)
    gstin = models.CharField(null=True, max_length=30)
    registration_number = models.CharField(null=True, max_length=100)
    phone_number_1 = models.CharField(null=True, max_length=15)
    phone_number_2 = models.CharField(null=True, max_length=15)
    business_email_1 = models.EmailField(null=True, max_length=100)
    business_email_2 = models.EmailField(null=True, max_length=100)
    website = models.CharField(null=True, max_length=100)
    address_line_1 = models.CharField(null=True, max_length=255)
    address_line_2 = models.CharField(null=True, max_length=255)
    city = models.CharField(null=True, max_length=100)
    state = models.CharField(null=True, max_length=100)
    country = models.CharField(null=True, max_length=100)
    logo = models.TextField(null=True)
    is_branch = models.BooleanField(default=False)
    belongs_to_ams_user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "ams_company_profiles"



class AmsLog(models.Model):
    changes = models.TextField(null=True)
    made_by = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "ams_logs"
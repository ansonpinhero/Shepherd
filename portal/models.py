from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils.timezone import now
user_levels = (
    ('l0','level-1-SuperAdmin'),
    ('l2','level-2-Manager '),
    ('l3','level-3-Volunteers'),
    ('l4','level-4-Normal Users'),
    
)
status_codes = (
    ('s1','Case Resolved'),
    ('s2','Case Assigned to a volunteer '),
    ('s3','Case under process'),
    ('s4','Case Open'),
    
)
class CustomUser(AbstractUser):
    
    first_name = models.CharField(max_length=100, default=" ")
    last_name = models.CharField(max_length=100, default=" ")
    user_type = models.CharField(
        max_length = 15,
        choices = user_levels,
        verbose_name='Type of User',
        null=False,blank=False,
        default='l4'
    )
    
    def __str__(self):
        full_name = str(self.first_name + " " +self.last_name)
        return full_name
    def save(self, *args, **kwargs):
        super(CustomUser, self).save(*args, **kwargs)
        profile = Profile(uid=self)
        profile.save()
class Request(models.Model):
    first_name = models.CharField(max_length=100, default=" ")
    last_name = models.CharField(max_length=100, default=" ")
    loc_latlong = models.CharField(max_length=100,verbose_name="Coordinates",blank=False)
    loc_latlong_accurate = models.CharField(max_length=100,verbose_name="Coordinates Accurate",blank=True)
    uid = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    is_requesting_for_others = models.BooleanField(
        verbose_name='Requesting for others', default=False)
    req_description = models.TextField(max_length=500,verbose_name="Description")
    phone_number_regex = RegexValidator(regex='^((\+91|91|0)[\- ]{0,1})?[456789]\d{9}$')
    phoneno = models.CharField(max_length=14,verbose_name='Phone Number', validators=[phone_number_regex],error_messages={'invalid': 'Please Enter 10/11 digit mobile number or landline as 0<std code><phone number>'})
    timestamp = models.DateTimeField(default=now)
    status = models.CharField(
        max_length = 15,
        choices = status_codes,
        verbose_name='Current Status',
        null=False,blank=False,
        default='s4'
    )
    def __str__(self):
        full_name = "Request by " +str(self.uid) + " for " + str(self.first_name) + " "+str(self.last_name)
        return full_name

class Profile(models.Model):
    uid = models.OneToOneField(CustomUser,on_delete=models.CASCADE,primary_key=True)
    
    phone_number_regex = RegexValidator(regex='^((\+91|91|0)[\- ]{0,1})?[456789]\d{9}$')
    phoneno = models.CharField(max_length=14,verbose_name='Phone Number', validators=[phone_number_regex],error_messages={'invalid': 'Please Enter 10/11 digit mobile number or landline as 0<std code><phone number>'})
    def __str__(self):
        full_name = str(self.uid)
        return full_name


class volunteer_invitations(models.Model):
    uid = models.OneToOneField(CustomUser,on_delete=models.CASCADE,primary_key=True)
    status = models.CharField(
        max_length = 15,
        choices = status_codes,
        verbose_name='Current Status',
        null=False,blank=False,
        default='s4'
    )
    def __str__(self):
        full_name = str(self.uid)
        return full_name
    
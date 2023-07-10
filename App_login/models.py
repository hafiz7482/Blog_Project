from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user_profile', on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics')

STATE_CHOICES = (
    ('Dhaka','Dhaka'),
    ('Barishal','Barishal'),
    ('Khulna','Khulna'),
    ('Chittagong','Chittagong'),
    ('Sylhet','Sylhet'),
    ('Rajshahi','Rajshahi'),
    )

class ProfileInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(choices= STATE_CHOICES, max_length=100)

    def __str__(self):
        return self.name
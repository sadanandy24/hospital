from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class Address(models.Model):
    id_address = models.AutoField(primary_key=True)
    address_line = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    code_postal = models.CharField(max_length=50)
    
    class Meta:
      verbose_name = "Address"
      verbose_name_plural = "Addresses"
      
    def __str__(self):
      return self.address_line



class Users(AbstractUser):
    email = models.CharField(max_length=50,unique=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=200)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender_choices = (("Male", "Male"), ("Female", "Female"))
    gender = models.CharField(max_length=10, choices=gender_choices, default="not_known")
    birthday = models.DateField(null=True, blank=True)
    is_doctor = models.BooleanField(default=False)
    profile_avatar = models.ImageField(upload_to="users/profiles", blank=True, default="doctor/profiles/download.png")
    id_address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    
    class Meta:
      verbose_name = "User"
      verbose_name_plural = "Users"
      
    def __str__(self):
      return self.username

class Reste_token(models.Model):
   user = models.ForeignKey(Users,on_delete=models.CASCADE)
   email = models.CharField(max_length = 50,unique=True)
   token = models.CharField(max_length = 50)

class Specialty(models.Model):
    name = models.CharField(max_length=25 , unique=True)
    description = models.TextField()
    
    class Meta:
      verbose_name = "Specialty"
      verbose_name_plural = "Specialty"
    
    def __str__(self):
      return self.name
    
class Doctors(models.Model):
  user = models.OneToOneField(Users, on_delete=models.CASCADE, primary_key=True)
  specialty = models.ForeignKey(Specialty,on_delete=models.CASCADE)
  bio = models.TextField()
  
  class Meta:
    verbose_name = "Doctor"
    verbose_name_plural = "Doctors"
    
  def __str__(self):
      return self.user.get_full_name() or self.user.username

      
class Patients(models.Model):
  user = models.OneToOneField(Users, on_delete=models.CASCADE, primary_key=True)
  insurance = models.CharField(max_length=50)
  
  class Meta:
    verbose_name = "Patient"
    verbose_name_plural = "Patients"
  
  def __str__(self):
      return self.user.get_full_name() or self.user.username


from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin,AbstractUser
from django.core.validators import RegexValidator
from django.db.models.signals import pre_save
from django.dispatch import receiver


class CustomUserManager(BaseUserManager):
    def create_user(self, phone_no, password=None, **extra_fields):
        if not phone_no:
            raise ValueError('The Phone number field must be set.')
        user = self.model(phone_no=phone_no, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_no, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(phone_no, password, **extra_fields)




class CustomUser(AbstractBaseUser, PermissionsMixin):
    phone_no = models.CharField(max_length=11, unique=True, validators=[
        RegexValidator(
            regex=r'^\+?1?\d{9,11}$',
            message="Phone number must be in the format: '0999999999'. Up to 11 digits allowed."
        ),
    ])
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_driver=models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'phone_no'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.first_name+' '+self.last_name


class DriverInfo(models.Model):
    user=models.OneToOneField('CustomUser',on_delete=models.CASCADE)
    email=models.EmailField(null=True,blank=True)
    nationalId=models.CharField(max_length=10, unique=True, validators=[
        RegexValidator(
            regex=r'^\+?1?\d{10,10}$',
            message="just numbers Up to 10 digits allowed."
        ),
    ])
    address=models.ForeignKey('pages.Address',on_delete=models.SET_NULL,null=True)
    experience=models.CharField(max_length=255,null=True,blank=True)
    avatar=models.ImageField()
    licence=models.ImageField()
    accepted=models.BooleanField(null=True, blank=True,default=None)
    def __str__(self):
        return str(self.user)
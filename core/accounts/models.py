from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)
from django.utils.translation import gettext_lazy as _

from django.db.models.signals import post_save
from django.dispatch import receiver

class MyUserManager(BaseUserManager):
    def create_user(self, email:str, password:str, **extra_fields):
        """
        Creates and saves a User with the given email and password.            
        """

        if not email:
            raise ValueError(_("The Email must be set."))
 
        user = self.model(
            email=self.normalize_email(email),**extra_fields
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email:str, password:str, **extra_fields):
        """
        Creates and saves a superuser with the given email and password.
        """
        extra_fields.setdefault("is_superuser",True)
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_active",True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)



# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = MyUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربرها"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, primary_key= True, related_name="profile")
    first_name = models.CharField(max_length=250, blank=True)
    last_name = models.CharField(max_length=250, blank= True)
    image = models.ImageField(blank=True, null=True)
    description = models.TextField(blank= True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email
    
    class Meta:
        verbose_name = "پروفایل"
        verbose_name_plural = "پروفایل ها"


# =========================== Signals ===========================
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
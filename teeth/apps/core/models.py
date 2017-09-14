from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
import uuid
from .choices import *

class Details(models.Model):
    family_name = models.CharField(max_length=30, null= True)
    first_name = models.CharField(max_length=30, null= True)
    last_name = models.CharField(max_length=30, null= True)
    register_num = models.CharField(max_length=30, null= True)
    gender = models.IntegerField(choices=GENDER_CHOICES, default=1)
    phone_number = models.CharField(max_length=30, null= True)
    emd_number = models.CharField(max_length=30, null= True)
    emd_type = models.IntegerField(choices=EMD_CHOICES, default=1)
    ndd_number = models.CharField(max_length=30, null= True)
    erkhiin_bichig = models.CharField(max_length=30, null= True)

    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name_plural = "Details"

class Address(models.Model):
    #all req
    aimag_hot = models.IntegerField(choices=GENDER_CHOICES, default=1)
    sum_duureg = models.CharField(max_length=30, null= True)
    bag_horoo = models.CharField(max_length=30, null= True)
    horoolol_gudamj = models.CharField(max_length=30, null= True)
    bair_hashaa = models.CharField(max_length=30, null= True)
    toot = models.CharField(max_length=30, null= True)

    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name_plural = "Addresses"

class Occupation(models.Model):
    bolovsrol = models.IntegerField(choices=GENDER_CHOICES, default=1)
    ajil = models.IntegerField(choices=GENDER_CHOICES, default=1)
    alban_tushaal = models.IntegerField(choices=GENDER_CHOICES, default=1)
    mergejil = models.IntegerField(choices=GENDER_CHOICES, default=1)
    baiguullaga = models.CharField(max_length=30, null= True)
    erheldeg_ajil = models.CharField(max_length=30, null= True)
    hariyalal = models.IntegerField(choices=GENDER_CHOICES, default=1)

    def __str__(self):
        return str(self.id)

class Medical(models.Model):
    tsusni_buleg = models.IntegerField(choices=GENDER_CHOICES, default=1)
    em_buleg = models.IntegerField(choices=GENDER_CHOICES, default=1)
    heregledeg_jsa = models.IntegerField(choices=GENDER_CHOICES, default=1)
    tolov = models.IntegerField(choices=GENDER_CHOICES, default=1)
    arhag_ovchin1 = models.CharField(max_length=30, null= True)
    arhag_ovchin2 = models.CharField(max_length=30, null= True)
    arhag_ovchin3 = models.CharField(max_length=30, null= True)
    arhi_uudag = models.BooleanField(default=False)
    tamhi_tatdag = models.BooleanField(default=False)
    orhiin_emch = models.IntegerField(choices=GENDER_CHOICES, default=1)
    gerleltiin_baidal = models.IntegerField(choices=GENDER_CHOICES, default=1)

    def __str__(self):
        return str(self.id)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    details = models.OneToOneField(Details, on_delete=models.CASCADE, null= True, blank=True)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null= True, blank=True)
    occupation = models.OneToOneField(Occupation, on_delete=models.CASCADE, null= True, blank=True)
    medical = models.OneToOneField(Medical, on_delete=models.CASCADE, null= True, blank=True)

    username = models.CharField(max_length=30, blank=True)
    is_activeFirst = models.BooleanField(default=False)
    is_activeSecond = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Appointment(models.Model):
    profiles = models.ManyToManyField(Profile, blank=True, related_name='profiles')

    title = models.CharField(max_length=30)
    allowed_amount= models.IntegerField(default=0)
    published_date = models.DateTimeField(blank=True, null=True,default=timezone.now)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.title




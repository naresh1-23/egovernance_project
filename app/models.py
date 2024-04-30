from django.db import models
import uuid


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class BirthCertificate(BaseModel):
    GENDER_CHOICES = (
        ("MALE", "MALE"),
        ("FEMALE", "FEMALE"),
        ("OTHERS", "OTHERS")
    )

    BIRTHTYPES = (
        ("SINGLE", "SINGLE"),
        ("TWINS", "TWINS"),
        ("TRIPLETS", "TRIPLETS"),
        ("OTHERS", "OTHERS")
    )

    BIRTH_PLACES = (
        ("HOME", "HOME"),
        ("HOSPITAL", "HOSPITAL"),
        ("HEALTH POST", "HEALTH POST"),
        ("OTHERS", "OTHERS")
    )
    district = models.CharField(max_length=100, default="Kathmandu", null=True, blank=True)
    zone = models.CharField(max_length=100, default="Bagmati", null=True, blank=True)
    municipal = models.CharField(max_length=100, default="Tokha", null=True, blank=True)
    woda_no = models.PositiveIntegerField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    DOB = models.DateField()
    birth_place = models.CharField(max_length=100, choices=BIRTH_PLACES)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES)
    birth_type = models.CharField(max_length=100, choices=BIRTHTYPES)
    caste = models.CharField(max_length=100)
    number = models.PositiveIntegerField()
    email = models.EmailField()


class FathersModel(BaseModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    citizenship_no = models.CharField(max_length=200)
    district = models.CharField(max_length=100, default="Kathmandu", null=True, blank=True)
    municipal = models.CharField(max_length=100, default="Tokha", null=True, blank=True)
    woda_no = models.PositiveIntegerField()
    age = models.PositiveIntegerField()
    occupation = models.CharField(max_length=200)
    education = models.CharField(max_length=200)
    language = models.CharField(max_length=200)
    religion = models.CharField(max_length=200)
    child = models.ForeignKey(BirthCertificate, on_delete=models.CASCADE)


class MothersModel(BaseModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    citizenship_no = models.CharField(max_length=200)
    district = models.CharField(max_length=100, default="Kathmandu", null=True, blank=True)
    municipal = models.CharField(max_length=100, default="Tokha", null=True, blank=True)
    woda_no = models.PositiveIntegerField()
    age = models.PositiveIntegerField()
    occupation = models.CharField(max_length=200)
    education = models.CharField(max_length=200)
    language = models.CharField(max_length=200)
    religion = models.CharField(max_length=200)
    child = models.ForeignKey(BirthCertificate, on_delete=models.CASCADE)


class ConfirmationPersonDetail(BaseModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    relation = models.CharField(max_length=100)
    citizenship_no = models.CharField(max_length=200)
    district = models.CharField(max_length=100, default="Kathmandu", null=True, blank=True)
    municipal = models.CharField(max_length=100, default="Tokha", null=True, blank=True)
    woda_no = models.PositiveIntegerField()
    child = models.ForeignKey(BirthCertificate, on_delete=models.CASCADE)

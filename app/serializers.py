from app.models import BirthCertificate, FathersModel, MothersModel, ConfirmationPersonDetail
from rest_framework import serializers


class BirthCertificateSerilizer(serializers.ModelSerializer):
    class Meta:
        model = BirthCertificate
        fields = "__all__"


class FathersModelSerilizer(serializers.ModelSerializer):
    class Meta:
        model = FathersModel
        fields = "__all__"


class MothersModelSerilizer(serializers.ModelSerializer):
    class Meta:
        model = MothersModel
        fields = "__all__"


class ConfirmationPersonDetailSerilizer(serializers.ModelSerializer):
    class Meta:
        model = ConfirmationPersonDetail
        fields = "__all__"

from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import BirthCertificateSerilizer, FathersModelSerilizer, MothersModelSerilizer, ConfirmationPersonDetailSerilizer
from rest_framework.response import Response
from rest_framework import status
from app.models import BirthCertificate, FathersModel, MothersModel, ConfirmationPersonDetail


@api_view(["POST"])
def birth_certificate(request):
    data = request.data
    serializer = BirthCertificateSerilizer(data=data)
    if not serializer.is_valid():
        data = {
            "message": serializer.errors
        }
        return Response(data, status=status.HTTP_400_BAD_REQUEST)
    serializer.save()
    data = {
        'data': serializer.data
    }
    return Response(data, status=status.HTTP_200_OK)


@api_view(["POST"])
def fathers_detail(request):
    data = request.data
    serializer = FathersModelSerilizer(data=data)
    if not serializer.is_valid():
        data = {
            "message": serializer.errors
        }
        return Response(data, status=status.HTTP_400_BAD_REQUEST)
    serializer.save()
    data = {
        'data': serializer.data
    }
    return Response(data, status=status.HTTP_200_OK)


@api_view(["POST"])
def mothers_detail(request):
    data = request.data
    serializer = MothersModelSerilizer(data=data)
    if not serializer.is_valid():
        data = {
            "message": serializer.errors
        }
        return Response(data, status=status.HTTP_400_BAD_REQUEST)
    serializer.save()
    data = {
        'data': serializer.data
    }
    return Response(data, status=status.HTTP_200_OK)


@api_view(["POST"])
def confirmation_detail(request):
    data = request.data
    serializer = ConfirmationPersonDetailSerilizer(data=data)
    if not serializer.is_valid():
        data = {
            "message": serializer.errors
        }
        return Response(data, status=status.HTTP_400_BAD_REQUEST)
    serializer.save()
    data = {
        'data': serializer.data
    }
    return Response(data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_details(request, id):
    birth = BirthCertificate.objects.filter(id=id).first()
    if not birth:
        return Response({"message": "Data Doesn't exists"}, status=status.HTTP_404_NOT_FOUND)
    fathers_detail = FathersModel.objects.filter(child=birth.id).first()
    mothers_detail = MothersModel.objects.filter(child=birth.id).first()
    confirmation = ConfirmationPersonDetail.objects.filter(child=birth.id).first()
    birth_serializer = BirthCertificateSerilizer(birth)
    father_serializer = FathersModelSerilizer(fathers_detail)
    mother_serializer = MothersModelSerilizer(mothers_detail)
    confirmation_serializer = ConfirmationPersonDetailSerilizer(confirmation)
    data = {
        "child": birth_serializer.data,
        "father": father_serializer.data,
        "mother": mother_serializer.data,
        "confirmation_person": confirmation_serializer.data
    }
    return Response(data=data, status=status.HTTP_200_OK)

from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers


class CompanyViewset(viewsets.ModelViewSet):
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer

9
class SubjectViewset(viewsets.ModelViewSet):
    queryset = models.Subjects.objects.all()
    serializer_class = serializers.SubjectsSerializer


class LettersViewset(viewsets.ModelViewSet):
    queryset = models.Letters.objects.all()
    serializer_class = serializers.LettersSerializer
from rest_framework import serializers

from . import models


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = ('id', 'name', 'address')


class SubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Subjects
        fields = ('id', 'name')


class LettersSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Letters
        fields = ('id', 'addressee', 'recipient', 'subject', 'title', 'date', 'answer')
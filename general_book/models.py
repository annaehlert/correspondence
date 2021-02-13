from django.db import models


class OwnedModel(models.Model):
    owner = models.OneToOneField('auth.User', on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Belonging(OwnedModel):
    name = models.CharField(max_length=100)


class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)


class Subjects(models.Model):
    name = models.CharField(max_length=100)


class Letters(models.Model):
    addressee = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='addressee')
    recipient = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='recipient')
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    date = models.DateField()
    answer = models.BooleanField(default=False)
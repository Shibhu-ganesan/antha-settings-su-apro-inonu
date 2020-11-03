from django.db import models
from django.contrib.auth.models import User


class StartUp(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=50, null=False)
    Field = models.CharField(max_length=50, null=False)
    Email = models.EmailField(null=False)
    Description = models.TextField(max_length=500, blank=False, null=False)

    def __str__(self):
        return self.Name


class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=50, null=True)
    Field = models.CharField(max_length=50, null=False)
    Email = models.EmailField(null=False)
    Query = models.TextField(blank=False, null=False)

   
    def __str__(self):
        return self.Name


class Investor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=50, null=False)
    Email = models.EmailField(null=False)
    Field = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.Name

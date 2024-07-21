from django.db import models
from django.db.models import ForeignKey


# Create your models here.

class Status(models.TextChoices):
    ACTIVE = 'Active'
    INACTIVE = 'Inactive'
    DEACTIVATE = 'Deactivate'


class Task(models.Model):
    name = models.CharField(verbose_name="Task Name", max_length=100, unique=True)
    status = models.CharField(verbose_name="Task Status", max_length=10, choices=Status.choices)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True, default='')
    publisher = ForeignKey(Publisher, on_delete=models.CASCADE)
    add_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

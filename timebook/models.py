from django.db import models
from decimal import *
from django.core.validators import MinValueValidator

# Create your models here.


class Customer(models.Model):
        name = models.CharField(max_length=50)
        phone = models.CharField(max_length=50)
        address = models.CharField(max_length=200)


class Job(models.Model):
        description = models.CharField(max_length=500)
        order_number = models.PositiveIntegerField(unique=True)
        customer = models.ForeignKey('Customer')


class TimeType(models.Model):
        description = models.CharField(max_length=200)
        worker_pay = models.DecimalField(max_digits=6, decimal_places=2,
                                         default=0.0,
                                         validators=[MinValueValidator(Decimal('0.00'))])
        customer_cost = models.DecimalField(max_digits=6, decimal_places=2,
                                            default=0.0,
                                            validators=[MinValueValidator(Decimal('0.00'))])


class Worker(models.Model):
        first_name = models.CharField(max_length=50)
        last_name = models.CharField(max_length=50)
        phone = models.CharField(max_length=50, null=True)
        email = models.EmailField(max_length=75, null=True)


class Time(models.Model):
        date = models.DateField()
        hours = models.DecimalField(max_digits=4, decimal_places=1,
                                    validators=[MinValueValidator(Decimal('0.00'))])
        description = models.CharField(max_length=300, null=True)
        worker = models.ForeignKey('Worker')
        type = models.ForeignKey('TimeType')
        job = models.ForeignKey('Job')

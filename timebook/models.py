from django.db import models
from decimal import *
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
        name = models.CharField(max_length=50)
        phone = models.CharField(max_length=50)
        address = models.CharField(max_length=200)


class Job(models.Model):
        description = models.CharField(max_length=500)
        order_number = models.PositiveIntegerField(unique=True)
        customer = models.ForeignKey('Customer', related_name='jobs')


class TimeType(models.Model):
        description = models.CharField(max_length=200)
        worker_pay = models.DecimalField(max_digits=6, decimal_places=2,
                                         default=0.0,
                                         validators=[
                                            MinValueValidator(Decimal('0.00'))
                                            ])
        customer_cost = models.DecimalField(max_digits=6, decimal_places=2,
                                            default=0.0,
                                            validators=[
                                                MinValueValidator(
                                                    Decimal('0.00'))])


class Worker(models.Model):
        user = models.OneToOneField(User, unique=True)
        first_name = models.CharField(max_length=50)
        last_name = models.CharField(max_length=50)
        phone = models.CharField(max_length=50, null=True)
        email = models.EmailField(max_length=75, null=True)

        def __str__(self):
            return "{0} {1}".format(self.first_name, self.last_name)


class Time(models.Model):
        date = models.DateField()
        hours = models.DecimalField(max_digits=4, decimal_places=1,
                                    validators=[
                                        MinValueValidator(Decimal('0.00'))
                                        ])
        description = models.CharField(max_length=300, null=True)
        worker = models.ForeignKey('Worker', related_name='times')
        type = models.ForeignKey('TimeType', related_name='times')
        job = models.ForeignKey('Job', related_name='times')

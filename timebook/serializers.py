from django.forms import widgets
from rest_framework import serializers
from timebook.models import Customer, Job, TimeType, Worker, Time


class CustomerSerializer(serializers.ModelSerializer):
        class Meta:
                model = Customer
                fields = ('id', 'name', 'phone', 'address')


class JobSerializer(serializers.ModelSerializer):
        class Meta:
                model = Job
                fields = ('id', 'description', 'order_number', 'customer')


class TimeTypeSerializer(serializers.ModelSerializer):
        class Meta:
                model = TimeType
                fields = ('id', 'worker_pay', 'customer_cost', 'description')


class WorkerSerializer(serializers.ModelSerializer):
        class Meta:
                model = Worker
                fields = ('id', 'first_name', 'last_name', 'phone', 'email')


class TimeSerializer(serializers.ModelSerializer):
        class Meta:
                model = Time
                fields = ('id', 'date', 'hours', 'description', 'worker', 'job')
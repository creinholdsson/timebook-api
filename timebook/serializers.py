from django.forms import widgets
from rest_framework import serializers
from timebook.models import Customer, Job, TimeType, Worker, Time


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    jobs = serializers.HyperlinkedIdentityField(view_name='jobsoncustomer'
                                                + '-list')

    class Meta:
            model = Customer
            fields = ('id', 'url', 'name', 'phone', 'address', 'jobs')


class JobSerializer(serializers.HyperlinkedModelSerializer):
    times = serializers.HyperlinkedIdentityField(view_name='timeonjob-'
                                                 + 'list')

    class Meta:
            model = Job
            fields = ('id', 'url', 'description', 'order_number',
                      'customer', 'times')


class TimeTypeSerializer(serializers.HyperlinkedModelSerializer):
    times = serializers.HyperlinkedIdentityField(view_name='timeoftype-list')

    class Meta:
            model = TimeType
            fields = ('id', 'url', 'worker_pay', 'customer_cost',
                      'description', 'times')


class WorkerSerializer(serializers.HyperlinkedModelSerializer):
    times = serializers.HyperlinkedIdentityField(view_name='workedon-list')

    class Meta:
            model = Worker
            fields = ('id', 'url', 'first_name', 'last_name', 'phone',
                      'email', 'times')


class TimeSerializer(serializers.HyperlinkedModelSerializer):
    #worker = WorkerSerializer()
    #job = serializers.HyperlinkedRelatedField(view_name='job-detail')
    #type = serializers.HyperlinkedRelatedField(view_name='timetype-detail')

    class Meta:
            model = Time
            fields = ('id', 'date', 'hours', 'description', 'worker',
                      'job', 'type', 'url')

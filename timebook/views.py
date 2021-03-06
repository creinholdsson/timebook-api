from timebook.models import *
from timebook.serializers import *
from rest_framework import generics
from rest_framework import permissions
from timebook.permissions import IsOwnerOrAdmin
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from timebook.filters import *
import django_filters


class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = (permissions.IsAuthenticated,)


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = (permissions.IsAuthenticated,)


class WorkerList(generics.ListCreateAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    permission_classes = (permissions.IsAuthenticated,)


class WorkerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    permission_classes = (permissions.IsAuthenticated,)


class TimeTypeList(generics.ListCreateAPIView):
    queryset = TimeType.objects.all()
    serializer_class = TimeTypeSerializer
    permission_classes = (permissions.IsAuthenticated,)


class TimeTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TimeType.objects.all()
    serializer_class = TimeTypeSerializer
    permission_classes = (permissions.IsAuthenticated,)


class TimeList(generics.ListCreateAPIView):
    """
    Returns a list of all the times added, sorted by date added.
    Filtering is enabled for **worker**, **job**, **date**, **min_date**
    (including) and **max_date** (including).
    """
    queryset = Time.objects.all()
    serializer_class = TimeSerializer
    permission_classes = (IsOwnerOrAdmin, permissions.IsAuthenticated, )
    filter_class = TimeFilter

    def pre_save(self, obj):
        obj.worker = Worker.objects.get(user=self.request.user)

    def get_queryset(self):
        if self.request.user.is_staff:
            return Time.objects.all()
        else:
            return Time.objects.filter(worker=Worker.objects.get(
                user=self.request.user))


class TimeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Time.objects.all()
    serializer_class = TimeSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrAdmin,)


class JobList(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = (permissions.IsAuthenticated,)


class JobDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = (permissions.IsAuthenticated,)


class WorkedOnList(generics.ListAPIView):
    model = Time
    serializer_class = TimeSerializer
    filter_class = TimeFilter

    def get_queryset(self):
        queryset = super(WorkedOnList, self).get_queryset()
        return queryset.filter(worker=self.kwargs.get('pk'))


class TimeOnJobList(generics.ListAPIView):
    model = Time
    serializer_class = TimeSerializer
    filter_class = TimeFilter

    def get_queryset(self):
        queryset = super(TimeOnJobList, self).get_queryset()
        return queryset.filter(job=self.kwargs.get('pk'))


class TimeOfTypeList(generics.ListAPIView):
    model = Time
    serializer_class = TimeSerializer
    filter_class = TimeFilter

    def get_queryset(self):
        queryset = super(TimeOfTypeList, self).get_queryset()
        return queryset.filter(type=self.kwargs.get('pk'))


class JobsOnCustomerList(generics.ListAPIView):
    model = Job
    serializer_class = JobSerializer

    def get_queryset(self):
        queryset = super(JobsOnCustomerList, self).get_queryset()
        return queryset.filter(customer=self.kwargs.get('pk'))


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'customer': reverse('customer-list', request=request, format=format),
        'job': reverse('job-list', request=request, format=format),
        'time': reverse('time-list', request=request, format=format),
        'timetype': reverse('timetype-list', request=request, format=format),
        'worker': reverse('worker-list', request=request, format=format)
    })

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from timebook.models import *
from timebook.serializers import *


class JSONResponse(HttpResponse):
        def __init__(self, data, **kwargs):
                content = JSONRenderer().render(data)
                kwargs['content_type'] = 'application/json'
                super(JSONResponse, self).__init__(content, **kwargs)


def customer_list(request):
        customers = Customer.objects.all()
        serialized = CustomerSerializer(customers, many=True)
        return JSONResponse(serialized.data)


def customer_detail(request, pk):
        try:
            customer = Customer.objects.get(pk=pk)

        except Customer.DoesNotExist:
            return HttpResponse(status=404)

        serialized = CustomerSerializer(customer)
        return JSONResponse(serialized.data)


def worker_list(request):
        workers = Worker.objects.all()
        serialized = WorkerSerializer(workers, many=True)
        return JSONResponse(serialized.data)


def worker_detail(request, pk):
        try:
            worker = Worker.objects.get(pk=pk)
        except Worker.DoesNotExist:
            return HttpResponse(status=404)
        serialized = WorkerSerializer(worker)
        return JSONResponse(serialized.data)


def job_list(request):
        jobs = Job.objects.all()
        serialized = JobSerializer(jobs, many=True)
        return JSONResponse(serialized.data)


def job_detail(request, pk):
        try:
            job = Job.objects.get(pk=pk)
        except Job.DoesNotExist:
            return HttpResponse(status=404)
        serialized = JobSerializer(job)
        return JSONResponse(serialized.data)


def timetype_list(request):
        timetypes = TimeType.objects.all()
        serialized = TimeTypeSerializer(timetypes, many=True)
        return JSONResponse(serialized.data)


def timetype_detail(request, pk):
        try:
            timetype = TimeType.objects.get(pk=pk)
        except TimeType.DoesNotExist:
            return HttpResponse(status=404)
        serialized = TimeTypeSerializer(timetype)
        return JSONResponse(serialized.data)


def time_list(request):
        times = Time.objects.all()
        serialized = TimeSerializer(times, many=True)
        return JSONResponse(serialized.data)


def time_detail(request, pk):
        try:
            time = Time.objects.get(pk=pk)
        except Time.DoesNotExist:
            return HttpResponse(status=404)
        serialized = TimeSerializer(time)
        return JSONResponse(serialized.data)
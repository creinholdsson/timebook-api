import django_filters
from timebook.models import *
from timebook.serializers import *


class TimeFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(name="date", lookup_type="gte")
    end_date = django_filters.DateFilter(name="date", lookup_type="lte")

    class Meta:
        model = Time
        fields = ["worker", "job", "start_date", "end_date"]

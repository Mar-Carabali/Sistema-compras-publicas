import django_filters 

from .models import *

class ContratosFilter(django_filters.FilterSet):
    class Meta:
        model = Contratos
        fields = ['ocid', 'status', 'contractPeriod_startDate', 'contractPeriod_endDate', 'contractPeriod_durationInDays', 'amount']
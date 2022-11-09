from dataclasses import fields
from itertools import count
from rest_framework.serializers import ModelSerializer,SerializerMethodField
from .models import Advocate,company


class companySerializer(ModelSerializer):
    employee_count = SerializerMethodField(read_only=True)
    class Meta:
        model = company
        fields = '__all__'

    def get_employee_count(self,obj):
        count  = obj.advocate_set.count()
        return count

class AdvocateSerializer(ModelSerializer):
    company = companySerializer()
    class Meta:
        
        model = Advocate
        fields = ['username','bio','company']
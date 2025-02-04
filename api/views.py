from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company,Employee
from api.serializers import CompanySerializer , EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class CompnayViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    @action(detail=True,methods=['get'])
    def employee(self,request,pk=None):
        print("pk value : ",pk)
        company = Company.objects.get(pk=pk)
        emps = Employee.objects.filter(company=company)
        emps_serializer = EmployeeSerializer(emps,many=True,context={'request':request})
        return Response(emps_serializer.data)
    
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

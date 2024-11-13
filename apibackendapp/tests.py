from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from .models import Department, Employee
from datetime import date
from django.urls import reverse
from .serializers import EmployeeSerializer
from rest_framework import status
# Create your tests here.
class EmployeeViewSetTest(APITestCase):
    #defining a function to setup some basic data for testing
    #create a sample department
    def setUp(self):
        self.department = Department.objects.create(DepartmentName="HR")
        #create a sample employee object and assign the department
        self.employee = Employee.objects.create(
            EmployeeName = "Jackie Chan",
            Designation = "Kung fu master",
            DateOfJoining = date(2024, 11, 13),
            DepartmentId = self.department,
            Contact = "China",
            IsActive = True
        )
        self.client = APIClient()
    #defining function to test employee listing api/endpoints
    #test case 1
    def test_employee_list(self):
        #the default reverse url for listening modelname-list
        url=reverse('employee-list')
        response=self.client.get(url) #send the api url and get the response
        #get all the employee objects of Employee Model
        employee=Employee.objects.all()
        #create a serializer object from EmployeeSerializer
        serializer=EmployeeSerializer(employee,many=True) #get all response

        #check and compare the response
        self.assertEqual(response.status_code, status.HTTP_200_OK) 

        self.assertEqual(response.data, serializer.data)
        #test case 2
    def test_employee_details(self):
        #the default reverse url for listening modelname-details
        url=reverse('employee-details', args=[self.employee.EmployeeId])
        response=self.client.get(url) #send the api url and get the response
        #get all the employee objects of Employee Model
       
        #create a serializer object from EmployeeSerializer
        serializer=EmployeeSerializer(self.employee) #get all response

        #check and compare the response
        self.assertEqual(response.status_code, status.HTTP_200_OK) 

        self.assertEqual(response.data, serializer.data)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Hospital, Employee, Sick, Company
from sms import send_sms
from .serializer import HospitalSerializer, CompanySerializer, SickSerializer,EmployeeSerializer
from asgiref.sync import sync_to_async


@api_view(['POST'])
def get_sick_employee_by_hospital(request):
    hospital_name = request.data.get('hospital_name')
    try:
        hospital = Hospital.objects.get(name=hospital_name)
        sick_people = Sick.objects.filter(hospital=hospital)
        serializer = SickSerializer(sick_people, many=True)
        return Response(serializer.data)
    except Hospital.DoesNotExist:
        return Response({"error":"Hospitall not found"}, status=400)
  

@api_view(['POST'])
def get_sick_employee_by_company(request):
    company_name = request.data.get('company-name')
    try:
        company = Company.objects.get(name=company_name)
        sick_people = Sick.objects.felter(company=company)
        serializer = SickSerializer(sick_people, many=True)
        return Response(serializer.data)
    except Company.DoesNotExist:
        return Response({'error':'Company not found'}, status=400)



async def sms_link(request):
    national_codes = request.data.get('national_codes')
    for national_code in national_codes:
        Employee = await sync_to_async(Employee.objects.get)(nationalID = national_code)
        message = 'please adhere to health protocols'
        originator = None #use default sender
        recipients = [Employee.phone_number] #list of phone numbers
        fail_siletly = False #raise an exception if an error occurs
        connection = None #use default backend
        await sync_to_async(send_sms)(message, originator, recipients, fail_siletly, connection)
    return Response({'message': "sms sent successfuly"}, status=400)



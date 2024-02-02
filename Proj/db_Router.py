from rest_framework.routers import DefaultRouter
from doob.views import get_sick_employee_by_hospital, get_sick_employee_by_company

class HospRouter(DefaultRouter):
    def get_default_basename(self, viewset):
        return 'hospital'
    

class CompRouter(DefaultRouter):
    def get_default_basename(self, viewset):
        return 'company'  


router = HospRouter()
router.register(r'hospital', get_sick_employee_by_hospital, basename='hospital')

comp_router = CompRouter()
router.register(r'company', get_sick_employee_by_company, basename='company')
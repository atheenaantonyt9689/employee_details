from django.urls import path
from .views import EmployeeListView,EmployeeDetailView
urlpatterns = [
    path('employees/<int:pk>/', EmployeeDetailView.as_view(), name='employee_detail'),
    path('', EmployeeListView.as_view(), name='home'),
]
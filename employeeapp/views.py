from django.views.generic import ListView,DetailView
from .models import Employee

class EmployeeListView(ListView):
    model = Employee
    template_name = 'home.html'

class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employee_detail.html'
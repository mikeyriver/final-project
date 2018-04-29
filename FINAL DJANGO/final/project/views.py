from django.shortcuts import render
from project.models import Ic
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

class IcList(ListView):
    model = Ic

class IcCreate(CreateView):
    model = Ic
    success_url = reverse_lazy('ic_list')
    fields = ['first_name', 'last_name', 'interviwer']

class IcUpdate(UpdateView):
    model = Ic
    success_url = reverse_lazy('ic_list')
    fields = ['first_name', 'last_name', 'interviwer']

class IcDelete(DeleteView):
    model = Ic
    success_url = reverse_lazy('ic_list')
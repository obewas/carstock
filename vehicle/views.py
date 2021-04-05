from django.shortcuts import render
from django.views.generic import ListView
from .models import Car, Cost
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from django.views import View
from .forms import CostCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
# Create your views here.
class CarListView(LoginRequiredMixin ,ListView):
    template_name = 'list.html'
    model = Car
    fields = '__all__'

class CarCreateView(LoginRequiredMixin ,CreateView):
    template_name = 'create_car.html'
    model = Car
    fields = '__all__'
    success_url = '/'


class CarUpdateView(LoginRequiredMixin ,UpdateView):
    template_name = 'update_car.html'
    model = Car
    fields = '__all__'
    success_url = '/'
class CarDeleteView(LoginRequiredMixin ,DeleteView):
    template_name = 'delete_car.html'
    model = Car
    fields = '__all__'
    success_url = "/"
    
  

class CarDetailView(LoginRequiredMixin ,DetailView):
    template_name = 'car_detail.html'
    model = Car
    fields = '__all__'


@login_required
def total_cost(request):
   
    if request.method == "POST":
        form = CostCreationForm(request.POST)
        if form.is_valid():
            
            customs = form.cleaned_data["customs"]
            cif_cost = form.cleaned_data["cif_cost"]
            delivery_order = form.cleaned_data["delivery_order"]
            radiation = form.cleaned_data["radiation"]
            ntsa_sticker = form.cleaned_data["ntsa_sticker"]
            insurance = form.cleaned_data["insurance"]
            cfs_chgs = form.cleaned_data["cfs_chgs"]
            agency = form.cleaned_data["agency"]
    
            total = customs + cif_cost + delivery_order + radiation + ntsa_sticker + insurance + cfs_chgs + agency
            form.save()
            return render(request, "total_cost.html", {"form": form, "total": total})
    else:
        form = CostCreationForm()
    return render(request, "total_cost.html", {"form": form})


   
class CostListView(LoginRequiredMixin ,ListView):
    template_name = 'cost_list.html'
    model = Cost
    fields = '__all__'

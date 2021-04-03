from django.shortcuts import render
from django.views.generic import ListView
from .models import Car
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from django.views import View
from .forms import CostCreationForm

# Create your views here.
class CarListView(ListView):
    template_name = 'list.html'
    model = Car
    fields = '__all__'

class CarCreateView(CreateView):
    template_name = 'create_car.html'
    model = Car
    fields = '__all__'
    success_url = '/'


class CarUpdateView(UpdateView):
    template_name = 'update_car.html'
    model = Car
    fields = '__all__'
    success_url = '/'
class CarDeleteView(DeleteView):
    template_name = 'delete_car.html'
    model = Car
    fields = '__all__'
    success_url ="/"

class CarDetailView(DetailView):
    template_name = 'car_detail.html'
    model = Car
    fields = '__all__'



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
            
            return render(request, "total_cost.html", {"form": form, "total": total})
    else:
        form = CostCreationForm()
    return render(request, "total_cost.html", {"form": form})
   
       

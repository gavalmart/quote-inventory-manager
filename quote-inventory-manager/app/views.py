from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse


from .forms import CustomerForm, ProviderForm, MakerForm, HddCapacityForm
from .models import Customer, Provider, Maker, Hdd_Capacity

import sys 


def index(request):
    context = {}
    template = loader.get_template('app/index.html')
    return HttpResponse(template.render(context, request))


def gentella_html(request):
    context = {}
    # The template to be loaded as per gentelella.
    # All resource paths for gentelella end in .html.

    # Pick out the html file name from the url. And load that template.
    load_template = request.path.split('/')[-1]
    template = loader.get_template('app/' + load_template)
    return HttpResponse(template.render(context, request))


def add_customer(request):
    form = CustomerForm(request.POST or None)
    form_title = "Add new customer"

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("customers")

    return render(request, "app/_add_edit_customer.html", {"form": form, "form_title": form_title})


def edit_customer(request, cust_id):
    customer = Customer.objects.get(id=cust_id)
    form = CustomerForm(request.POST or None, instance=customer)
    form_title = "Edit customer"

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("customers")
        
    context = {"customer": customer, "form": form, "form_title": form_title}    
    return render(request,  "app/_add_edit_customer.html", context= context)

def delete_customer(request, cust_id):
    customer = Customer.objects.get(id=cust_id)
    form_title = "Deletion of Customer"

    if request.method == "POST":
        customer.delete()
        return redirect("customers")
    
    context = {"customer": customer, "form_title": form_title}
    return render(request, "app/_delete_customer.html", context=context)



def customers(request):
    customers_list = Customer.objects.all()

    return render(request, "app/_customers.html", {"customers": customers_list})

def providers(request):
    providers_list = Provider.objects.all()

    return render(request, "app/_providers.html", {"providers": providers_list})


def edit_provider(request, prov_id):
    provider = Provider.objects.get(id=prov_id)
    form = ProviderForm(request.POST or None, instance = provider)
    form_title = "Edit provider"
    
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("providers")
    
    
    context = {"provider": provider, "form": form, "form_title": form_title}
    return render(request, "app/_add_edit_provider.html", context=context)



def add_provider(request):
    form = ProviderForm(request.POST or None)
    context = {"form": form, "form_title": "Add new provider"}

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("providers")  
    
    return render(request, "app/_add_edit_provider.html", context=context)


def delete_provider(request, prov_id):
    provider = Provider.objects.get(id=prov_id)

    if request.method == "POST":
        provider.delete()
        return redirect("providers")
    
    return render(request, "app/_delete_provider.html", {"provider": provider, "form_title": "Deletion of Provider"})



def makers(request):
    makers_list = Maker.objects.all()

    return render(request, "app/_makers.html", {"makers": makers_list})


def add_maker(request):
    form = MakerForm(request.POST or None)
    form_title = "Add new maker"
    context = {"form": form, "form_title": form_title}

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("makers")
        
    return render(request, "app/_add_edit_maker.html", context=context)


def edit_maker(request, mk_id):
    maker =  Maker.objects.get(id = mk_id)
    form = MakerForm(request.POST or None, instance = maker)
    form_title = "Edit maker"

    context = {"maker": maker, "form": form, "form_title": form_title}

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("makers")
        
    return render(request, "app/_add_edit_maker.html", context=context)


def delete_maker(request, mk_id):
    maker = Maker.objects.get(id = mk_id)
    form_title = "Deletion of maker"

    context = {"maker": maker, "form_title": form_title}

    if request.method == "POST":
        maker.delete()
        return redirect("makers")

    return render(request, "app/_delete_maker.html", context=context)


def hdd_capacities(request):
    hdd_capacities_list = Hdd_Capacity.objects.all()

    return render(request, "app/_hdd_capacities.html", context={"hdd_capacities": hdd_capacities_list})

def add_hdd_capacity(request):
    form = HddCapacityForm(request.POST or None)
    form_title = "Add new HDD Capacity"
    context = {"form": form, "form_title": form_title}

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("hdd_capacities")
        
    return render(request, "app/_add_edit_hdd_capacity.html", context=context)


def edit_hdd_capacity(request, hdd_cap_id):
    hdd_capacity = Hdd_Capacity.objects.get(id=hdd_cap_id)
    form = HddCapacityForm(request.POST or None, instance= hdd_capacity)
    form_title = "Edit HDD Capacity"
    context = {"form": form, "form_title": form_title, "hdd_capacity": hdd_capacity}

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("hdd_capacities")
    
    return render(request, "app/_add_edit_hdd_capacity.html", context=context)

def delete_hdd_capacity(request, hdd_cap_id):
    hdd_capacity = Hdd_Capacity.objects.get(id=hdd_cap_id)
    context = {"hdd_capacity": hdd_capacity}

    print(hdd_capacity, sys.stderr)

    if request.method == "POST":
        hdd_capacity.delete()
        return redirect("hdd_capacities")
    
    return render(request, "app/_delete_hdd_capacity.html", context=context)

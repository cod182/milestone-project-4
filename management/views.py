from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.conf import settings
from django.db.models import Q
import requests
from .forms import VehicleForm


def add_vehicle(request):
    """ Add a new vhicle to the site"""

    if not request.user.is_superuser:
        messages.error(
            request,
            'Sorry, only authorised can do that!'
        )
        return redirect(reverse('home'))

    if request.method == 'POST':
        form_data = {
            'sku': request.POST['registration'].replace(" ", "").lower(),
            'name': request.POST['make'].lower() + '-' + request.POST['registration'].replace(" ", "").lower(),
            'registration': request.POST['registration'].lower(),
            'make': request.POST['make'].lower(),
            'model': request.POST['model'].lower(),
            'trim': request.POST['trim'].lower(),
            'colour': request.POST['colour'].lower(),
            'fuel': request.POST['fuel'].lower(),
            'engine_size': request.POST['engine_size'].lower(),
            'body_type': request.POST['body_type'].lower(),
            'gearbox': request.POST['gearbox'].lower(),
            'drivetrain': request.POST['drivetrain'].lower(),
            'seats': request.POST['seats'].lower(),
            'description': request.POST['description'].lower(),
            'price': 200,
            'full_price': request.POST['full_price'].lower(),
            'mileage': request.POST['mileage'].lower(),
            'model_year': request.POST['model_year'].lower(),
            'doors': request.POST['doors'].lower(),
            'type': 'vehicle',
            'available': 'yes',
            }
        form = VehicleForm(form_data)
        print(form)
        if form.is_valid():
            vehicle = form.save()
            messages.success(
                request,
                'Sucsessfully added vehicle!'
            )
            return redirect(reverse('vehicle_detail', args=[form_data['sku']]))
        else:
            messages.error(
                request,
                'Failed to add vehicle. Please ensure the form is valid'
                )
    else:
        form = VehicleForm()
    template = 'management/add_vehicle.html'
    context = {
        'form': form,
    }
    return render(request, template, context)

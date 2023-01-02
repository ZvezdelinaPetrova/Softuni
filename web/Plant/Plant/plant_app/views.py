from django.shortcuts import render, redirect

from Plant.plant_app.models import Profile, Plant

from Plant.plant_app.forms import ProfileCreateForm, PlantEditForm, \
    PlantDeleteForm, ProfileDeleteForm, PlantCreateForm, ProfileEditForm


def get_profile():
    profile = Profile.objects.first()
    if profile:
        return profile


def index(request):
    profile = get_profile()

    context = {
        'profile': profile,
    }

    return render(
        request,
        'home-page.html',
        context,
    )


def create_profile(request):
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show catalog')

    context = {
        'form': form,
        'profile': profile,

    }

    return render(
        request,
        'create-profile.html',
        context,
    )


def details_profile(request):
    profile = Profile.objects.filter().get()
    plants_all = Plant.objects.all()
    name = f"{profile.first_name} {profile.last_name}"

    plants_total = plants_all.count()

    context = {
        'profile': profile,
        'plants_all': plants_all,
        'name': name,
        'plants_total': plants_total,
    }

    return render(
        request,
        'profile-details.html',
        context,
    )


def edit_profile(request):
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details profile')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(
        request,
        'edit-profile.html',
        context,
    )


def delete_profile(request):
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show index')

    context = {
        'form': form,
    }

    return render(
        request,
        'delete-profile.html',
        context,
    )


def details_plant(request, pk):
    plant = Plant.objects.filter(pk=pk).get()

    profile = get_profile()

    context = {
        'plant': plant,
        'profile': profile,
    }

    return render(
        request,
        'plant-details.html',
        context,
    )


def add_plant(request):
    profile = get_profile()

    if request.method == 'GET':
        form = PlantCreateForm()
    else:
        form = PlantCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show catalog')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(
        request,
        'create-plant.html',
        context,
    )


def edit_plant(request, pk):
    plant = Plant.objects.filter(pk=pk).get()
    profile = get_profile()

    if request.method == 'GET':
        form = PlantEditForm(instance=plant)
    else:
        form = PlantEditForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('show catalog')

    context = {
        'form': form,
        'plant': plant,
        'profile': profile,
    }

    return render(
        request,
        'edit-plant.html',
        context,
    )


def delete_plant(request, pk):
    plant = Plant.objects.filter(pk=pk).get()

    profile = get_profile()

    if request.method == 'GET':
        form = PlantDeleteForm(instance=plant)
    else:
        form = PlantDeleteForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('show catalog')

    context = {
        'form': form,
        'plant': plant,
        'profile': profile,
    }

    return render(
        request,
        'delete-plant.html',
        context,
    )


def catalog_page(request):
    profile = get_profile()
    plants_all = Plant.objects.all()

    context = {
        'profile': profile,
        'plants_all': plants_all,
    }

    return render(
        request,
        'catalogue.html',
        context,
    )
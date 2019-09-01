from django.shortcuts import render, redirect
from .models import Pet
from .forms import PetForm, SignupForm, SigninForm, UpdateForm
from django.contrib.auth import login, authenticate, logout


def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            login(request, user)
            return redirect("pet-list")
    context = {
        "form":form,
    }
    return render(request, 'signup.html', context)

def signin(request):
    form = SigninForm()
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                return redirect('pet-list')
    context = {
        "form":form
    }
    return render(request, 'signin.html', context)

def signout(request):
    logout(request)
    return redirect("signin")

def pet_update(request, pet_id):
	pet=Pet.objects.get(id=pet_id)
	forms= UpdateForm(instance=pet)
	if request.method == "POST":
		forms= UpdateForm(request.POST, request.FILES, instance=pet)
		if forms.is_valid():
			forms.save()
			return redirect('pet-detail', pet_id=pet.id)
	context={
		"form": forms,
		"pet": pet,
	}
	return render(request, 'update.html', context)

def pet_delete(request, pet_id):
	pet=Pet.objects.get(id=pet_id)
	pet.delete()
	return redirect('pet-list')


def pet_create(request):
	forms= PetForm()
	if request.method == "POST":
		forms= PetForm(request.POST, request.FILES)
		if forms.is_valid():
			forms.save()
			return redirect('pet-list')
	context={
		'form': forms,
	}
	return render(request, 'create.html', context)

def pet_list(request):
	context={
		'pets': Pet.objects.filter(available=True),
	}

	return render(request, 'list.html', context)

def pet_detail(request, pet_id):
	context={
		'pet':Pet.objects.get(id=pet_id),
	}
	return render(request, 'detail.html', context)

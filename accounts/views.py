from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from .forms import UserForm
from .models import User

def registerUser(request):
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            adress = form.cleaned_data['adress']
            password = form.cleaned_data['password']
            
            user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, phone_number=phone_number, adress=adress, password=password)
            user.role = User.CUSTOMER
            user.save()

            messages.success(request, 'Te has registrado satisfactoriamente.')
            return redirect('registerUser')
    else:
        form = UserForm()

    context = { 'form' : form, }
    return render(request, 'accounts/registerUser.html', context)
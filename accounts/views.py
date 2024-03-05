from django.shortcuts import render, HttpResponse, redirect
from . forms import UserForm
from . models import User
from django.contrib import messages

def registerUser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # Create the user using the form
            # password = form.cleaned_data['password']
            # user = form.save(commit=False)
            # user.set_password(password)
            # user.role = User.CUSTOMER
            # user = form.save()
            # return redirect('registerUser')
            
            # Create the user using create_user method
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = form.cleaned_data['username']
            
            user = User.objects.create_user(first_name=first_name, last_name=last_name,username=username,email=email,password=password)
            user.role = User.CUSTOMER
            user.save()
            messages.success(request, 'Your data has been saved successfully!')
            return redirect('registerUser')
        else:
            print('invalid forms')
            print(form.errors)
    else:
        form = UserForm()
    context = {
        'form': form,
    }
    return render(request,'accounts/resgisterUser.html', context)
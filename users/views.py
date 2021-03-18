from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import login,  authenticate
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse


# Create your views here.

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('xlogs:index')) 

def register(request):
    # Register a new user
    if request.method != 'POST':
        # Display blank registration form
        form = UserCreationForm()
    else: 
        # Process completed form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user= form.save()
            # Log user in and redirest them to homepage
            authenticated_user = authenticate(username=new_user.username,
                    password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('xlogs:index'))
    
    context = {'form':form}
    return render(request, 'users/register.html', context)

        

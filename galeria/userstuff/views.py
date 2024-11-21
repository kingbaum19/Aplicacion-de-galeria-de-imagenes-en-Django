from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register_user(request):
        if request.method == 'POST':
          form = UserCreationForm(request.POST)
          if form.is_valid():
                user = form.save()
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                user = authenticate(username=username, password=password)
                login(request, user)
                messages.success(request, ('Su registro fue exitoso!'))
                return redirect('index')
        else:
         form = UserCreationForm()     

        return render (request, 'users/register.html', {
                'form': form,
                })
     
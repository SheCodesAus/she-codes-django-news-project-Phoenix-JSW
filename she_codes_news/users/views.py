from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm, UpdateProfileForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

def createAccount(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST) 
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/CreateAccount.html', {'form': form})

@login_required # Require user logged in before they can access profile page
def profile(request):
    user=request.user
    return render(request,'users/userProfile.html',{'user':user})

class AuthorView(generic.DetailView):
    model = CustomUser

class UpdateAccountView(UpdateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('updateprofile')
    template_name = 'users/userUpdate.html'

@login_required   #Required to update user profile
def updateProfile(request):
    if request.method == 'POST':
        
        p_form = UpdateProfileForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        u_form = CustomUserChangeForm(request.POST, instance=request.user) 
        if u_form.is_valid() and p_form.is_valid():
            p_form.save()
            u_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile') # Redirect back to profile page

    else:
        p_form = UpdateProfileForm(instance=request.user.profile)
        u_form = CustomUserChangeForm(instance=request.user)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/userUpdate.html', context)
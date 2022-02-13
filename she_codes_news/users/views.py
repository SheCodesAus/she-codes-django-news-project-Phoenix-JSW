from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm, UpdateProfileForm
from django.shortcuts import render, redirect
from django.contrib import messages

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

def profile(request):
    user=request.user
    return render(request,'users/userProfile.html',{'user':user})

class UserProfileView(UpdateView):
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('profile')
    template_name = 'users/userProfile.html'

# @login_required
def UpdateProfile(request):
    if request.method == 'POST':
        p_form = UpdateProfileForm(request.POST,request.FILES,instance=request.user.profile)
        u_form = CustomUserChangeForm(request.POST,instance=request.user)
        if p_form.is_valid() and u_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,'Your Profile has been updated!')
            return redirect('profile')
    else:
        p_form = UpdateProfileForm(instance=request.user)
        u_form = CustomUserChangeForm(instance=request.user.profile)

    context={'p_form': p_form, 'u_form': u_form}
    return render(request, 'users/userProfile.html',context )

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

class AuthorView(generic.DetailView):
    model = CustomUser

@login_required # Require user logged in before they can access profile page
def profile(request):
    user=request.user
    return render(request,'users/userProfile.html',{'user':user})

class UpdateAccountView(UpdateView):
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('updateProfile')
    template_name = 'users/userUpdate.html'

    def get_object(self, queryset=None):
        return self.request.user




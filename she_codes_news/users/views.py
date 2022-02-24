from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views import generic
from .models import CustomUser
from news.models import NewsStory
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
    return render(request, 'users/createAccount.html', {'form': form})

class AuthorView(generic.DetailView):
    model = CustomUser

@login_required # Require user to login before they can access profile page
def profile(request):
    user=request.user
    stories = NewsStory.objects.filter(author=user.id).order_by('-pub_date')
    return render(request,'users/userProfile.html',{'user':user, 'stories': stories})

class UpdateAccountView(UpdateView):
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('users:profile')
    template_name = 'users/userUpdate.html'

    def get_object(self, queryset=None):
        return self.request.user

    




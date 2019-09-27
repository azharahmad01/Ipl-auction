
from django.shortcuts import render,redirect
from .forms import UserForm,PlayerForm,OwnerForm
from django.contrib import messages
from django.contrib.auth import get_user_model
from .forms import UserUpdateForm
from django.contrib.auth.decorators import login_required

User = get_user_model()

# Create your views here.


def choose(request):  
    return render(request,'users/choose.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Your account has been created! You are now able to login.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request,'users/register.html',{'form':form})


def player_view(request):
	
    if request.method == 'POST':
            
        user_form = UserForm(request.POST, prefix='UF')
        player_form = PlayerForm(request.POST, prefix='PF')
            
        if user_form.is_valid() and player_form.is_valid():
                user = user_form.save(commit=False)
                user.is_player = True
                user.save()

                user.user_player.base_price = player_form.cleaned_data.get('base_price')
                user.user_player.name = user_form.cleaned_data.get('username')
                user.user_player.email = user_form.cleaned_data.get('email')
                user.user_player.save()

                return redirect('login')
			
    else:
        user_form = UserForm(prefix='UF')
        player_form = PlayerForm(prefix='PF')
		
    return render(request, 'users/player_register.html',{
    'user_form': user_form,
    'player_form': player_form,
    } )

def owner_view(request):
	
    if request.method == 'POST':
            
        user_form = UserForm(request.POST, prefix='UF')
        owner_form = OwnerForm(request.POST, prefix='OF')
            
        if user_form.is_valid() and owner_form.is_valid():
                user = user_form.save(commit=False)
                user.is_owner = True
                user.save()

                user.user_owner.team_name = owner_form.cleaned_data.get('team_name')
                user.user_player.email = user_form.cleaned_data.get('email')
                user.user_player.name = user_form.cleaned_data.get('username')
                user.user_owner.save()

                return redirect('login')
			
    else:
        user_form = UserForm(prefix='UF')
        owner_form = OwnerForm(prefix='OF')
		
    return render(request, 'users/owner_register.html',{
    'user_form': user_form,
    'owner_form': owner_form,
    } )

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,request.FILES,instance = request.user)
        if u_form.is_valid() :
            u_form.save()
            messages.success(request,f'Your account has been updated.')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance = request.user)

    context = {
        'u_form' : u_form,
    }
    return render(request,'users/profile.html',context)


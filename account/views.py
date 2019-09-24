from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# def user_login(request):
# 	if request.method == 'POST':
# 		form = LoginForm(request.POST)
# 		if form.is_valid():
# 			cd = form.cleaned_data
# 			user = authenticate(request, username = cd['username'], password = cd['password'])

# 			if user is not None:
# 				if user.is_active:
# 					login(request, user)
# 					return HttpResponse('Successfull login attempt.')
# 				else:
# 					return HttpResponse('Account is Disabled.')
# 			else:
# 				return HttpResponse('Invalid Login')
# 	else:
# 		form = LoginForm()
# 	return render(request, 'login.html', {'form': form})


@login_required
def dashboard(request):
	return render(request, 'account/dashboard.html', {'section': dashboard })

def register(request):
	if request.method == 'POST':
		user_reg_form = UserRegistrationForm(request.POST)
		if user_reg_form.is_valid():
			new_user = user_reg_form.save(commit=False)
			new_user.set_password(user_reg_form.cleaned_data['password'])
			new_user.save()
			Profile.objects.create(user=new_user)
			return render(request, 'account/register_done.html', {'new_user': new_user})

	else:
		user_reg_form = UserRegistrationForm()
	return render(request, 'account/register.html', {'user_reg_form': user_reg_form})


@login_required
def edit(request):
	if request.method == 'POST':
		user_form = UserEditForm(instance=request.user, data=request.POST)
		profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			messages.success(request, 'Profile updated Successfully')
		else:
			messages.error(request, 'Error updating your profile')
	else:
		user_form = UserEditForm(instance=request.user)
		profile_form = ProfileEditForm(instance=request.user.profile)

	return render(request, 'account/edit.html', {'user_form': user_form, 'profile_form': profile_form})

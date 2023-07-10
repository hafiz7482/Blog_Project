from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from django.views import View
from .models import  ProfileInfo
from .forms import SignUp,  ProfileInfoForm, ProfilePic
from django.contrib import messages
from .forms import SignUp
# Create your views here.


class SignUpView(View):
    def get(self, request):
        form = SignUp()
        return render(request, 'App_login/signup.html',locals())
    def post(self, request):
        form = SignUp(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ' Congratulation ! User SignUp Successfully !')
        else:
            messages.warning(request, ' Error ! User SignUp Failed.')
        return render(request, 'App_login/signup.html',locals())
    
class ProfileInfoView(View):
    def get(self, request):
        form = ProfileInfoForm()
        return render(request, 'App_login/profile.html',locals())
    def post(self, request):
        form  = ProfileInfoForm(request.POST)
        if form.is_valid():
            user = request.user 
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            zipcode = form.cleaned_data['zipcode']
            state = form.cleaned_data['state']

            reg = ProfileInfo(user=user, name=name, locality=locality, city=city,mobile=mobile, zipcode=zipcode, state=state)
            reg.save()
            messages.success(request, ' Congratulation ! User Registration Successfully Done.')
        else:
            messages.warning(request, ' Error ! User Registration Failed.')
        return render(request, 'App_login/profile.html',locals())
    

def Address(request):
    add =  ProfileInfo.objects.filter(user=request.user)
    return render(request, 'App_login/address.html',locals())

class AddressUpdate(View):
    def get(self, request,pk):
        add = ProfileInfo.objects.get(pk=pk)
        form = ProfileInfoForm(instance=add)
        return render(request, 'App_login/updateaddress.html',locals())
    def post(self, request,pk):
        form = ProfileInfoForm(request.POST)
        if form.is_valid():
            add = ProfileInfo.objects.get(pk=pk)
            add.name = form.cleaned_data['name']
            add.locality = form.cleaned_data['locality']
            add.city = form.cleaned_data['city']
            add.mobile = form.cleaned_data['mobile']
            add.zipcode = form.cleaned_data['zipcode']
            add.state = form.cleaned_data['state']
            add.save()
            messages.success(request, ' Congratulation ! Profile Update Successfully Done.')
        else:
            messages.warning(request, ' Error ! Profile Update Failed.')

        return redirect('App_login:address')
    
def add_pro_pic(request):
    form = ProfilePic()
    if request.method == 'POST':
        form = ProfilePic(request.POST, request.FILES)
        if form.is_valid():
            user_obj = form.save(commit=False)
            user_obj.user = request.user
            user_obj.save()
            return HttpResponseRedirect(reverse('App_login:address'))
    return render(request, 'App_login/add_pro_pic.html', context= {'form': form})

def ChangeProfilePic(request):
    form = ProfilePic(instance=request.user.user_profile)
    if request.method == 'POST':
        form = ProfilePic(request.POST, request.FILES, instance=request.user.user_profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('App_login:address'))
    return render(request, 'App_login/add_pro_pic.html', context= {'form': form})

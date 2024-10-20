from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from first_app.models import Topic,Webpage,AccessRecord
from . import forms
from first_app.forms import UserForm,UserProfileInfoForm
 

# Create your views here.

# def users(request):

#     form = forms()

#     if request.method == 'POST':
#         form = forms(request.POST)

#         if form.is_valid():
#             form.save(commit=True)
#             return index(request)
#         else:
#             print("Error Form Invalid")

#     return render(request,'user.html',{'form':form})

def index(request):
    # webpages_list = AccessRecord.objects.order_by('date')
    # date_dict = {'text': 'webpages list','number':100}
    return render(request,'index.html')#,context=date_dict)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("Your are logged In!")



def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account is not active")
        else:
            print("Someone tried to login but failed")
            print("Username : {} & password :{}".format(username,password))
            return HttpResponse("Invalid login Detail supplied!")
    else:
        return render(request,'login.html',{})


def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']


            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form= UserProfileInfoForm()

    return render(request,'registration.html',
                  {'user_form':user_form,
                   'profile_form':profile_form,
                   'registered':registered})

# def relative(request):
#     return render(request,'relative_url.html')

# def help(request):
#     help_dict = {'help' : 'HelpPage'}
#     return render(request,'help.html',context=help_dict)

# def form_name_view(request):
#     form = forms.FormName()

#     if request.method == 'POST':
#         form = forms.FormName(request.POST)

#         if form.is_valid():
#             print("Validation Success!")
#             print("Name:"+form.cleaned_data['name'])
#             print("Email:"+form.cleaned_data['email'])
#             print("Text:"+form.cleaned_data['text'])



#     return render(request,'form.html',{'form':form})

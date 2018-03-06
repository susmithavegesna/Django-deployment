from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from AppTwo.models import *
from AppTwo import forms
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout


# Create your views here
def index(emtag):
    return HttpResponse ('<em> My Second App <em>')

def help(abc):
    helpdict = {'help_insert':'Help Page, Dictionary value for the key help_insert','new_insert':'hello this is For practicing filters'}
    return render(abc,'Apptwo/help.html',context=helpdict )

#def Userview(req):
#    user_list = Usertab.objects.order_by('FirstName')
#    udict = {'user_insert':user_list}
#    return render(req,'AppTwo/Users.html',context=udict)

def UserView(req):
    form1 = forms.FormModel()
    if req.method == "POST":
        form1 = forms.FormModel(req.POST)

        if form1.is_valid():
            form1.save(commit=True)
            print("Valid Sucess")
            print("FIRST NAME "+form1.cleaned_data['FirstName'])
            print("EMAIL "+form1.cleaned_data['Email'])
            print("LAST NAME "+form1.cleaned_data['LastName'])

            return help(req)
        else:
            print("error invalid form")


    return render(req,'Apptwo/form.html',{'formkey':form1})

def relativeView(request):
    return render(request,"Apptwo/relative.html")

def registrationView(request):
    registered = False
    if request.method == "POST":
        User_Form = forms.UserForm(data=request.POST)
        Profile_Form = forms.UserProfileinfoForm(data=request.POST)

        if User_Form.is_valid() and Profile_Form.is_valid():
            user = User_Form.save()
            user.set_password(user.password)
            user.save()

            profile = Profile_Form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True
        else:
            print("failed registration")
            print(User_Form.errors, Profile_Form.errors)
    else:
        User_Form = forms.UserForm()
        Profile_Form = forms.UserProfileinfoForm()

    return render(request,"Apptwo/registration.html",{"registeredKey":registered,
                                                        "User_FormKey":User_Form,
                                                        "Profile_FormKey":Profile_Form}


#def user_loginView(request):
#    if request.methos == "POST":

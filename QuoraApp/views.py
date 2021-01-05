from django.shortcuts import render,redirect
from .forms import CreateUserForm
from django.contrib.auth.models import Group
from .models import Member,Tag
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models  import User
# Create your views here.

def HomePage(request):
    tag=Tag.objects.all()
    dictionary={'tag':tag}
    return render(request,'QuoraApp/HomePage.html',dictionary)



def Register(request):
    if request.method=="POST":
        name=request.POST.get('full_name')
        email=request.POST.get('your_email')
        password1=request.POST.get('password')
        password2=request.POST.get('comfirm_password')
        username=request.POST.get('full_name_1')
        password=request.POST.get('password_1')

        print(name,email,password1,password2)
        print(username,password)
        
        if name is not None and email is not  None and password1 is not None and password2 is not None:
            if password1==password2:
                user = User.objects.create_user(name, email, password1)
                member = Member(user=user, name=name, email=email)
                user.save()
                member.save()
                grp = Group.objects.get(name='normaluser')
                user.groups.add(grp)
                print('user created')

            else:
                print("password do not match")

        elif username is not  None and password is not None:
            user = authenticate(request, username=username, password=password)

            if user is not None:
                    login(request, user)
                    print('user logged in')
                    return redirect('HomePage')

    return render(request,'QuoraApp/register.html')

def AnswerPage(request):
    return render(request,'QuoraApp/AnswerPage.html')


def TagPage(request):
    return render(request,'QuoraApp/Tag.html')
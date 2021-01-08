from django.shortcuts import render,redirect
from .forms import CreateUserForm
from django.contrib.auth.models import Group
from .models import Member,Tag,Question,Answer
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models  import User
from django.contrib.auth.decorators import login_required
from .decorators import only_unauthenticated_users_allowed, only_admin_allowed, only_normal_users_allowed
# Create your views here.


@login_required(login_url='Register')
@only_normal_users_allowed
def HomePage(request):
    tag=Tag.objects.all()
    answers=Answer.objects.all()
    dictionary={'tag':tag,'answers':answers}
    return render(request,'QuoraApp/HomePage.html',dictionary)


@only_unauthenticated_users_allowed
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


def Logout(request):
    logout(request)
    return redirect('HomePage')


@login_required(login_url='Register')
@only_normal_users_allowed
def AnswerPage(request):
    return render(request,'QuoraApp/AnswerPage.html')


@login_required(login_url='Register')
@only_normal_users_allowed
def TagPage(request,pk):
    tag=Tag.objects.get(id=pk)
    questions=Question.objects.filter(tag=tag)
    print(questions)
    answers={}
    j=0;
    for  i in questions:
        answer={j:list(Answer.objects.filter(question=i))}
        j=j+1
        answers.update(answer)
    print(answers)
    dictionary={'tag':tag,'questions':questions,'answers':answers}
    return render(request,'QuoraApp/Tag.html',dictionary)


@login_required(login_url='Register')
@only_normal_users_allowed
def AskQuestion(request):
    return render(request, 'QuoraApp/AskQuestion.html')


@login_required(login_url='Register')
@only_normal_users_allowed
def IndividualQuestion(request):
    return render(request, 'QuoraApp/IndividualQuestion.html')


@login_required(login_url='Register')
@only_normal_users_allowed
def Profile(request):
    return render(request, 'QuoraApp/Profile.html')
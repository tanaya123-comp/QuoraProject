from django.shortcuts import render,redirect
from .forms import CreateUserForm, ProfileForm, EmployeeForm, StudentForm, QuestionForm
from django.contrib.auth.models import Group
from .models import Member,Tag,Question,Answer, Employee, Student
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models  import User
from django.contrib.auth.decorators import login_required
from .decorators import only_unauthenticated_users_allowed, only_admin_allowed, only_normal_users_allowed
from django.contrib import messages
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
                messages.success(request, f"New User Created: {username}")
                messages.info(request, f"You may Login now")
            else:
                messages.error(request, f"Passwords do not match")

        elif username is not  None and password is not None:
            user = authenticate(request, username=username, password=password)

            if user is not None:
                    login(request, user)
                    messages.success(request, f'User logged in')
                    return redirect('HomePage')
            else:
                messages.error(request, f"Username or Password is incorrect!")

    return render(request,'QuoraApp/register.html')


def Logout(request):
    logout(request)
    messages.info(request, f"Logged Out successfully")
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
    ques_form = QuestionForm()

    if request.method == 'POST':
        ques_form = QuestionForm(request.POST)
        if ques_form.is_valid():
            new_question = ques_form.save(commit=False)
            new_question.askedBy = request.user.member
            new_question.save()
            messages.success(request, f"Your Question was noted")
        else:
            messages.error(request, ques_form.errors)
    context = {
        'form': ques_form
    }
    return render(request, 'QuoraApp/AskQuestion.html', context)


@login_required(login_url='Register')
@only_normal_users_allowed
def IndividualQuestion(request):
    return render(request, 'QuoraApp/IndividualQuestion.html')


@login_required(login_url='Register')
@only_normal_users_allowed
def Profile(request):
    # Fetch the current user and prepare ProfileForm
    profile = request.user.member
    form = ProfileForm(instance=profile)

    # Check whether that Member has Educational/Job Details
    employee_detail = Employee.objects.filter(member__exact=profile)
    student_detail = Student.objects.filter(member__exact=profile)

    role = 'None'
    qualification_form = None
    blank_edu_form = StudentForm()
    blank_job_form = EmployeeForm()

    if len(employee_detail):
        # User is an employee
        role = 'Employee'
        qualification_form = EmployeeForm(instance=employee_detail[0])
    elif len(student_detail):
        # User is a student
        role = 'Student'
        qualification_form = StudentForm(instance=student_detail[0])

    if request.method == 'POST' and role in ['Employee', 'Student']:
        # When Employee/Student updates his information
        query_dict = request.POST
        if 'name' in query_dict:
            form = ProfileForm(request.POST, request.FILES, instance=profile)
        elif 'university' in query_dict:
            form = StudentForm(request.POST, instance=student_detail[0])
        elif 'company' in query_dict:
            form = EmployeeForm(request.POST, instance=employee_detail[0])
        if form.is_valid():
            form.save()
            messages.success(request, f"Details Updated!")
            return redirect('Profile')
    elif request.method == 'POST' and role in ['None']:
        # When user who hasn't filled any details, fills one by using Modal
        query_dict = request.POST
        if 'university' in query_dict:
            university = query_dict.get('university')
            degree = query_dict.get('degree')
            branch = query_dict.get('branch')
            new_details = Student(member=profile, university=university, degree=degree, branch=branch)
            messages.success(request, f"Your Educational Details were saved!")
            new_details.save()
        elif 'company' in query_dict:
            company = query_dict.get('company')
            job_post = query_dict.get('job_post')
            new_details = Employee(member=profile, company=company, job_post=job_post)
            messages.success(request, f"Your Job Details were saved!")
            new_details.save()
        return redirect('Profile')
    context = {
        'form': form,
        'role': role,
        'q_form': qualification_form,
    }
    if role == 'None':
        # When the user hasn't filled any details, we should pass 2 blank forms for modals
        context['blank_edu_form'] = blank_edu_form
        context['blank_job_form'] = blank_job_form

    return render(request, 'QuoraApp/Profile.html', context)
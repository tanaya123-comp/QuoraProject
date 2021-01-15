from django.shortcuts import render,redirect,HttpResponse
from .forms import CreateUserForm, ProfileForm, EmployeeForm, StudentForm, QuestionForm
from django.contrib.auth.models import Group
from .models import Member,Tag,Question,Answer, Employee, Student,Vote, Following
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models  import User
from django.contrib.auth.decorators import login_required
from .decorators import only_unauthenticated_users_allowed, only_admin_allowed, only_normal_users_allowed

from .forms import PostForm,TinyMCEWidget,AnswerForm

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
    answers=Answer.objects.all()
    questions=Question.objects.all()
    question=[]
    for i in questions:
        x=0
        for j in answers:
            if j.question==i :
                x=1

        if x==0:
            question.append(i)

    

    form=AnswerForm()

    return render(request,'QuoraApp/AnswerPage.html',{'questions':question,'form':form})


@login_required(login_url='Register')
@only_normal_users_allowed
def TagPage(request,pk):
    tag=Tag.objects.get(id=pk)
    answers=Answer.objects.filter(tag=tag)

    follow = False
    if Following.objects.filter(member=request.user.member,tag=tag):
        follow=True

    print(answers)
    form=AnswerForm()
    return render(request,'QuoraApp/Tag.html',{'answers':answers,'form':form,'follow':follow, 'cat_id':pk})

@login_required(login_url='Register')
@only_normal_users_allowed
def upVote(request):
    if request.method == 'GET':
        pk = request.GET['post_id']
        ans=Answer.objects.get(id=pk)


        if Vote.objects.filter(answer=ans,vote=1,votedBy=request.user.member).exists():


            return HttpResponse("<h1>Already Voted</h1>")

        if Vote.objects.filter(answer=ans,vote=2,votedBy=request.user.member).exists():

            v=Vote.objects.filter(answer=ans,vote=2,votedBy=request.user.member)
            v.delete()

            vote = Vote.objects.create(answer=ans, vote=1, votedBy=request.user.member)

            vote.save()

        #print(vote)

            return HttpResponse("<h1>Upvoted Successfully</h1>")

        vote = Vote.objects.create(answer=ans, vote=1, votedBy=request.user.member)

        vote.save()

        #print(vote)

        return HttpResponse("<h1>Upvoted Successfully</h1>")





@login_required(login_url='Register')
@only_normal_users_allowed
def downVote(request):
    if request.method == 'GET':
        pk = request.GET['post_id']
        ans = Answer.objects.get(id=pk)



        if Vote.objects.filter(answer=ans, vote=2, votedBy=request.user.member).exists():
            return HttpResponse("<h1>Already DownVoted</h1>")

        if Vote.objects.filter(answer=ans, vote=1, votedBy=request.user.member).exists():
            v = Vote.objects.filter(answer=ans, vote=1, votedBy=request.user.member)
            v.delete()

            vote = Vote.objects.create(answer=ans, vote=2, votedBy=request.user.member)

            vote.save()

        # print(vote)

            return HttpResponse("<h1>DownVoted Successfully</h1>")




        vote = Vote.objects.create(answer=ans, vote=2, votedBy=request.user.member)

        vote.save()

    #print(vote)

        return HttpResponse("<h1>Downvoted Successfully</h1>")


@login_required(login_url='Register')
@only_normal_users_allowed
def submitAnswer(request,pk):
    print(pk)
    question = Question.objects.get(id=pk)
    form = AnswerForm()
    if request.method == 'POST':
       query_dict=request.POST
       answer2=query_dict.get('answer')
       tag=question.tag
       answeredBy=request.user.member

       obj=Answer.objects.create(answer=answer2,question=question,tag=tag,answeredBy=answeredBy)

       obj.save()
       messages.success(request, f"Answer Submitted!")
       return redirect('HomePage')

    return render(request,'QuoraApp/submitAnswer.html',{'form':form})



@login_required(login_url='Register')
@only_normal_users_allowed
def AskQuestion(request):
    ques_form = QuestionForm()

    # Also, we need to list all the questions that the user has asked
    member = request.user.member
    all_questions = Question.objects.filter(askedBy__exact=member)

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
        'form': ques_form,
        'all_questions': all_questions,
    }
    return render(request, 'QuoraApp/AskQuestion.html', context)


@login_required(login_url='Register')
@only_normal_users_allowed
def IndividualQuestion(request, pk):
    # Fetch the question object
    question = Question.objects.filter(id__exact=pk)[0]

    # Fetch all the answers to that question
    all_answers = Answer.objects.filter(question__exact=question)

    tag = Tag.objects.all()

    form=AnswerForm()

    print(question.askedBy)
    # Populate one question with many answers...
    context = {
        'question' : question,
        'all_answers' : all_answers,
        'tag': tag,
        'form':form,
    }

    return render(request, 'QuoraApp/IndividualQuestion.html', context)


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

    # Additional stats:
    # 1. Number of questions asked by user
    num_ques = Question.objects.filter(askedBy__exact=profile).count()
    num_tags = Following.objects.filter(member__exact=profile).count()
    num_answers = Answer.objects.filter(answeredBy__exact=profile).count()
    context = {
        'form': form,
        'role': role,
        'q_form': qualification_form,
        'numQues': num_ques,
        'num_tags': num_tags,
        'num_answers': num_answers,
    }
    if role == 'None':
        # When the user hasn't filled any details, we should pass 2 blank forms for modals
        context['blank_edu_form'] = blank_edu_form
        context['blank_job_form'] = blank_job_form

    return render(request, 'QuoraApp/Profile.html', context)


@login_required(login_url='Register')
@only_normal_users_allowed
def following(request):
    member = request.user.member
    following_tags = Following.objects.filter(member__exact=member)
    following_tags_ids = following_tags.values('tag')
    print(following_tags_ids)
    remaining_tag = Tag.objects.exclude(id__in=following_tags_ids)
    print(remaining_tag)
    context = {
        'tag': remaining_tag,
        'following_tags': following_tags,
    }
    return render(request, 'QuoraApp/Followings.html', context)


@login_required(login_url='Register')
@only_normal_users_allowed
def UnfollowHandle(request):
    pk = request.GET['post_id']
    print('pk is ', pk)
    member = request.user.member
    tag = Tag.objects.filter(id__exact=pk)[0]
    current_following = Following.objects.get(member__exact=member, tag__exact=tag)
    current_following.delete()
    return HttpResponse('Success')


@login_required(login_url='Register')
@only_normal_users_allowed
def FollowHandle(request):
    pk = request.GET['post_id']
    member = request.user.member
    tag = Tag.objects.filter(id__exact=pk)[0]
    current_following = Following.objects.create(member=member, tag=tag)
    return HttpResponse('Success')

@login_required(login_url='Register')
@only_normal_users_allowed
def MyAnswers(request):
    answers = Answer.objects.filter(answeredBy__exact=request.user.member)
    context = {
        'answers': answers,
    }
    return render(request, 'QuoraApp/MyAnswers.html', context)

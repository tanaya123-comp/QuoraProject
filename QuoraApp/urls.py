from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import HomePage,Register,AnswerPage,TagPage, Logout, AskQuestion, IndividualQuestion, Profile,upVote,downVote,submitAnswer

urlpatterns = [
    path('',HomePage,name="HomePage"),
    path('tinymce/', include('tinymce.urls')),
    path('register/',Register, name="Register"),
    path('answerpage/',AnswerPage,name="AnswerPage"),
    path('tagpage/<str:pk>/',TagPage,name="TagPage"),
    path('logout/', Logout, name='Logout'),
    path('askquestion/', AskQuestion, name='AskQuestion'),
    path('upvote/<str:pk>',upVote,name="upvote"),
    path('downvote/<str:pk>',downVote,name="downvote"),
    path('submitAnswer/<str:pk>',submitAnswer,name="submitanswer"),
    # For now, we are keeping individual question url simple
    # Afterwards, we will change it to something like this: question/1 or question/question_name
    path('ques/<str:pk>/', IndividualQuestion, name="Question"),
    path('profile/', Profile, name='Profile'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
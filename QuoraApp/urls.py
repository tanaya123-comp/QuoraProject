from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import (HomePage,Register,AnswerPage,TagPage, Logout, AskQuestion,
                        IndividualQuestion, Profile,upVote,downVote,submitAnswer,
                        following, UnfollowHandle, FollowHandle, MyAnswers,getupvote,getdownvote, editAnswer, deleteAnswer,clearVote)

urlpatterns = [
    path('',HomePage,name="HomePage"),
    path('tinymce/', include('tinymce.urls')),
    path('register/',Register, name="Register"),
    path('answerpage/',AnswerPage,name="AnswerPage"),
    path('tagpage/<str:pk>/',TagPage,name="TagPage"),
    path('logout/', Logout, name='Logout'),
    path('askquestion/', AskQuestion, name='AskQuestion'),
    path('upvote/',upVote,name="upvote"),
    path('downvote/',downVote,name="downvote"),
    path('submitAnswer/<str:pk>',submitAnswer,name="submitanswer"),
    # For now, we are keeping individual question url simple
    # Afterwards, we will change it to something like this: question/1 or question/question_name
    path('ques/<str:pk>/', IndividualQuestion, name="Question"),
    path('profile/', Profile, name='Profile'),
    path('following/', following, name='Following'),
    path('unfollow/', UnfollowHandle, name='Unfollow'),
    path('follow/', FollowHandle, name='Follow'),
    path('myanswers/', MyAnswers, name='MyAnswers'),
    path('getupvote/',getupvote,name="getupvote"),
    path('getdownvote/',getdownvote,name="getdownvote"),
    path('editAnswer/<str:pk>', editAnswer, name='editAnswer'),
    path('deleteAnswer/', deleteAnswer, name='deleteAnswer'),
    path('clearvote/',clearVote,name='clearVote'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import HomePage,Register,AnswerPage,TagPage

urlpatterns = [
    path('homepage',HomePage,name="HomePage"),
    path('tinymce/', include('tinymce.urls')),
    path('register/',Register),
    path('answerpage/',AnswerPage,name="AnswerPage"),
    path('tagpage/',TagPage,name="TagPage"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
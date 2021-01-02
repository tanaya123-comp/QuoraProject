from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import HomePage

urlpatterns = [
    path('homepage',HomePage),
    path('tinymce/', include('tinymce.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
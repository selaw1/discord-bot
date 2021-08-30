from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from .quizbot import views as qviews
from .score import views as sviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('api/random/', qviews.RandomQuestion.as_view(), name='random' ),
    path('api/score/update/', sviews.UpdateScores.as_view(), name='score' )
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


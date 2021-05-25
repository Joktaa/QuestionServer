from django.contrib import admin
from django.urls import path

from question import views as question

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('get-questions/', question.getQuestions),
]

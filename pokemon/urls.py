from django.urls import path
from pokemon import views

app_name = 'pokemon'
urlpatterns = [
    path('', views.answer_question, name='answer_question'),
]

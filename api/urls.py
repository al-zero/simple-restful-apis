from django.urls import path
from . import views

urlpatterns = [
    path('', views.overview, name='overview'),
    path('index/', views.index, name='index'),
    path('message/', views.Message.as_view(), name='message'),

    path('quizes/', views.QuizView.as_view(), name='quiz'),
    path('functionViewQuiz/', views.QuizV, name='fbq'),

    path('genericView/', views.GenericQuizView.as_view(),name='generic_view')
]

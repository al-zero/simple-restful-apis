from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.notes_overview, name='overview'),
    path('notes-list/', views.notes_list, name='notes-list'),
    path('note-detail/<int:pk>/', views.note_detail, name='note-detail'),
    path('note-create/', views.note_create, name='note_create'),
    path('note-update/<int:pk>', views.note_update, name='note_update'),
    path('note-delete/<int:pk>/', views.note_delete, name='note_delete'),

]

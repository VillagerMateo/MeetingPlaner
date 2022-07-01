from django.urls import path

from . import views


urlpatterns = [
    path('<int:id>/', views.detail, name='detail'),
    path('rooms/', views.rooms_list, name='rooms'),
    path('new/', views.new, name='new'),
    path('edit-meeting/<int:pk>/', views.updateMeeting, name='edit'),
    path('delete-meeting/<int:pk>/', views.deleteMeeting, name='delete'),
]
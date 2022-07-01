
from django.contrib import admin
from django.urls import path, include
from website.views import welcome, date, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome, name='welcome'),
    path('date/', date, name='date'),
    path('about/', about, name='about'),
    path('meetings/', include('meetings.urls')),
]

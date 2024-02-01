from django.urls import path, include
from . import views

app_name='myapp'
urlpatterns = [
    path('', include('myapp.api.urls',),name='api_myapp'),
	path('detail/<int:pk>', views.home, name='detail'),
	path('list/', views.listpage),
]
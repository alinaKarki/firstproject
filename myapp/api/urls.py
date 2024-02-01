from myapp.api import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter


app_name='api_myapp'

# Create a router and register our ViewSets with it.
router = DefaultRouter()    
router.register(r'Student-views', views.StudentViewset,)
urlpatterns = [
    path('students/', views.student_list.as_view()),
    # path('student/<int:pk>/', views.student)
    # path('', include('router.urls'), name='router-list'),

]

urlpatterns += router.urls
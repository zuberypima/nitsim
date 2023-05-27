from django.urls import path
from .views import  add_exam,teacherdashboard
urlpatterns = [
    path('examregister', add_exam,name='examregister'),
    path('teacherdash',teacherdashboard,name='teacherdash')
]

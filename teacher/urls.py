from django.urls import path
from .views import  add_exam,teacherdashboard,results,ca_results
urlpatterns = [
    path('examregister', add_exam,name='examregister'),
    path('teacherdash',teacherdashboard,name='teacherdash'),
    path('results',results,name='results'),
    path('caresults',ca_results,name='caresults')
]

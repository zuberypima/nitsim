from django.urls import path
from .views import  add_exam,teacherdashboard,results,ca_results,add_caresults,update_caresults
urlpatterns = [
    path('examregister', add_exam,name='examregister'),
    path('teacherdash',teacherdashboard,name='teacherdash'),
    path('results',results,name='results'),
    path('caresults',ca_results,name='caresults'),
    path('addcaresult',add_caresults,name='addcaresult'),
    path('updateca/<str:pk>',update_caresults,name='updateca')
    
] 

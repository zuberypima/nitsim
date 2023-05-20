from django.urls import path
from .views import homepage,caresultPage,resultUpload,regStudent,claimpage,regfunc

urlpatterns = [
    path("dashboard",homepage, name='dashboard'),
    path("caresultpage",caresultPage, name='caresultpage'),
    path("resultupload",resultUpload, name='resultupload'),
    path("studentreg",regStudent, name='studentreg'),
    path("claimpopup",claimpage, name='claimpopup'),
    path("studentreg",regfunc, name='studentreg')

]


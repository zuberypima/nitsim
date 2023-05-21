from django.urls import path
from .views import homepage,caresultPage,resultUpload,regStudent,claimpage,regfunc,teacherdash,studentdash,examreg,admindash,allresults,loginpage

urlpatterns = [
    path("loginpage",loginpage, name='loginpage'),
    path("teacherdash",teacherdash, name='teacherdash'),
    path("admindash",admindash, name='admindash'),
    path("studentdash",studentdash, name='studentdash'),
    path("caresultpage",caresultPage, name='caresultpage'),
    path("resultupload",resultUpload, name='resultupload'),
    path("studentreg",regStudent, name='studentreg'),
    path("claimpopup",claimpage, name='claimpopup'),
    path("studentreg",regfunc, name='studentreg'),
    path("examreg",examreg, name='examreg'),
    path("allresults",allresults, name='allresults')
    ]




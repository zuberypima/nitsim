from django.urls import path
from  .views import add_program,add_course,add_student,registerdash,studentdahs

urlpatterns = [
     path("programreg",add_program, name='programreg'),
     path("coursereg",add_course, name='coursereg'),
     path("studentsregister",add_student, name='studentsregister'),
     path("admindash",registerdash, name='admindash'),
     path("studentdash",studentdahs, name='studentdash'),
    # path("resultupload",resultUpload, name='resultupload'),
    # path("studentreg",regStudent, name='studentreg'),
    # path("examreg",program, name='examreg'),
    # # path("examreg",examreg, name='examreg'),
    # path("claimpopup",claimpage, name='claimpopup'),
    # path("studentreg",regfunc, name='studentreg'),   
    # path("allresults",allresults, name='allresults'),
    ]




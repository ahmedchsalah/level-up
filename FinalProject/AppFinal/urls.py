from django.urls import path
from .views import (RegisterStudentView, RegisterTeacherView, RegisterSpecialistView, RegisterAdminView,
                    VerifiyUserEmail, LoginUserView, ManageCourseView,
                    PasswordResetRequestView, PasswordResetConfirmView, SetNewPasswordView, getCourses,
                    ValidateEmailView,
                    ResendOTPView, TeacherCourseAssignmentView)

urlpatterns = [

    path('register/student/', RegisterStudentView.as_view(), name='signupStudent'),
    path('register/teacher/', RegisterTeacherView.as_view(), name='signupTeacher'),
    path('register/specialist/', RegisterSpecialistView.as_view(), name='registerSpecialist'),
    path('register/admin/', RegisterAdminView.as_view(), name='registerAdmin'),
    path('validate/email/', ValidateEmailView.as_view(), name='validateEmail'),
    path('resend/otp/', ResendOTPView.as_view(), name='resendOTP'),
    path('verify/otp/', VerifiyUserEmail.as_view(), name='verify'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('courses/', getCourses, name='courses'),
    path('courses/assignement/', TeacherCourseAssignmentView.as_view(), name='teacherCourseAssignment'),
    # path('profile', TestAuthentication.as_view(), name='profile'),
    path('course/create', ManageCourseView.as_view(), name='create_course'),
    # path('/password_reset', PasswordResetRequestView.as_view(), name='reset_password'),
    # path('/password_reset_confirm/<uidb64>/<token>', PasswordResetConfirmView.as_view(), name='reset_password_confirm'),
    # path('/set_new_password', SetNewPasswordView.as_view(), name='set_password'),
]

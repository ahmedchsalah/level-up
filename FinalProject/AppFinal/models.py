from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group, Permission
from django.utils.translation import gettext_lazy as _
from .managers import UserManager
from rest_framework_simplejwt.tokens import RefreshToken


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=100, unique=True, verbose_name=_('Email Address'))
    first_name = models.CharField(max_length=100, verbose_name=_('First Name'))
    last_name = models.CharField(max_length=100, verbose_name=_('Last Name'))
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return str(f"{self.first_name} {self.last_name}")

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    groups = models.ManyToManyField(Group, related_name='custom_user_set', verbose_name=_('Groups'))
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set',
                                              verbose_name=_('User Permissions'))


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    university = models.CharField(max_length=100, null=True, verbose_name=_('University'))
    degree = models.CharField(max_length=100, null=True, verbose_name=_('Degree'))
    speciality = models.CharField(max_length=50, null=True, verbose_name=_('speciality'))
    courses_of_interest = models.CharField(max_length=255, null=True, verbose_name=_('Courses of Interest'))
    img = models.ImageField(upload_to='images/', null=True)
    score = models.IntegerField(default=0)
    daily_time_spent = models.IntegerField(default=0)
    weekly_time_spent = models.IntegerField(default=0)
    monthly_time_spent = models.IntegerField(default=0)


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    university = models.CharField(max_length=100, null=True, verbose_name=_('University'))
    img = models.ImageField(upload_to='images/', null=True)


class Role(models.Model):
    RoleChoices = (
        ('student', 'STUDENT'),
        ('teacher', 'TEACHER'),
        ('specialist', 'SPECIALIST'),
        ('admin', 'ADMIN')
    )
    name = models.CharField(max_length=50, choices=RoleChoices)
    abstract = True


class User_Roles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)


class OneTimePassword(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6, unique=True)

    def __str__(self):
        return f'{self.user.first_name} passcode'


class Badge(models.Model):
    name = models.CharField(max_length=50)
    score = models.IntegerField()
    description = models.TextField()
    students = models.ManyToManyField(Student, related_name='students')


class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    degree = models.CharField(max_length=75)
    level = models.CharField(max_length=75)
    teachers = models.ManyToManyField(Teacher)
    img_url = models.URLField(max_length=90, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} - {self.description}'


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    order = models.IntegerField()
    chapter_number = models.IntegerField()
    description = models.TextField()


class Slide(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    order = models.IntegerField()
    description = models.TextField()
    content = models.TextField()


class Game(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    link = models.URLField(max_length=150)
    score = models.IntegerField()
    type = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Enroll_Course(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    progress = models.IntegerField()
    score_earned = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ChatRoom(models.Model):
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    theme_color = models.TextField()


class Message(models.Model):
    ChatRoom = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    content = models.TextField()
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Participation(models.Model):
    ChatRoom = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now=True)
    status = models.IntegerField()

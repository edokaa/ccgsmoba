from django.urls import path

from django.contrib.auth import views as auth_views

from . import views

app_name = 'attendance'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('attendance/', views.AttendanceView.as_view(), name='attendance'),
    path('attendance/login/', views.LoginView.as_view(), name='login'),
    path('attendance/mass-<int:pk>/', views.MassView.as_view(), name='mass'),
    path('attendance/mass-<int:pk>/select-member', views.SelectMemberView.as_view(), name='select-member'),
    path('attendance/mass-<int:pk>/new-member', views.AddNewView.as_view(), name='new-member'),
    path('attendance/final-details', views.FinalView.as_view(), name='final'),
    path('files/', views.FilesView.as_view(), name='files'),

    # path('attendance/login-2/', auth_views.LoginView.as_view(), name='login-2'),

]

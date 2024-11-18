from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('login/', views.login_view, name='login'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    path('manage_students/', views.manage_students, name='manage_students'),
    path('manage_marks/', views.manage_marks, name='manage_marks'),
    path('student_view_marks/', views.student_view_marks, name='student_view_marks'),
]

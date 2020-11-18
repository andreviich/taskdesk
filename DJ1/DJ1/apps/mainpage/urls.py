from django.urls import path
from . import views
app_name = 'mainpage'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('leave_task/', views.leave_task, name = 'leave_task'),
    path('leave_task_ajax/', views.leave_task_ajax, name="leave_task_ajax"),
    path('educators/', views.educators, name="educators")
]
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.StudentListApiView.as_view() , name="student_list"),
    path('create/', views.StudentCreateApiView.as_view(), name="student_create"),
    path('<int:id>', views.StudentRetrieveUpdateDestroyApiView.as_view(), name="student_update_or_destroy"),
]
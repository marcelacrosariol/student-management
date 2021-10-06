from django.http import JsonResponse

from rest_framework.filters import SearchFilter
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveUpdateDestroyAPIView

from .models import (
    Student,
)

from .serializers import (
    StudentListSerializer,
    StudentSerializer
)


class StudentListApiView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentListSerializer
    filter_backends =  [SearchFilter]
    search_fields =  ['name', 'family_name', 'student_id']


class StudentCreateApiView(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'id'

    # def delete(self, request, *args, **kwargs):
    #     student_id = request.data.get('id')
    #     response = super().delete(request, *args, **kwargs)
    #     return response

    # def update(self, request, *args, **kwargs):
    #     return super().update
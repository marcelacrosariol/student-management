from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
)

from .models import Student


class StudentListSerializer(ModelSerializer):
    status = SerializerMethodField()
    gender = SerializerMethodField()

    class Meta:
        model =  Student
        fields = (
            'name',
            'family_name',
            'gender',
            'student_id',
            'status',
        )
    
    def get_gender(self, obj):
        return obj.get_gender()

    def get_status(self, obj):
        return obj.get_status()


class StudentSerializer(ModelSerializer):
    class Meta:
        model =  Student
        fields = (
            'name',
            'family_name',
            'birthday',
            'gender',
            'student_id',
            'status'
        )

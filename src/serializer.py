import json

from src import domain


class Serializer:

    def serialize(self, obj):
        serializer = self.get_right_serializer(type(obj))
        return serializer(obj)

    @staticmethod
    def list_serializer(obj_list):
        for i, obj in enumerate(obj_list):
            obj_list[i] = obj.to_dict()
        res = json.dumps(obj_list, ensure_ascii=False)
        return res

    def get_right_serializer(self, obj_type):
        if obj_type == domain.Student:
            return self.student_serializer
        elif obj_type == domain.StudentWorkVariant:
            return self.work_variant_serializer

    @staticmethod
    def student_serializer(student: domain.Student):
        student_dict = student.to_dict()
        return json.dumps(student_dict)

    @staticmethod
    def work_variant_serializer(student_work: domain.StudentWorkVariant):
        student_work_dict = student_work.to_dict()
        return json.dumps(student_work_dict)

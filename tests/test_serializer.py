import json
from unittest import TestCase

from src.serializer import Serializer
from src.domain import Student


class SerializerTest(TestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_student_serializer(self):
        ser = Serializer()
        student = Student(name="kek", surname="joj", patronymic="il", student_id=1)
        res = ser.serialize(student)
        right_json = json.dumps({"id": 1, "name": "kek", "surname": "joj", "patronymic": "il"})
        self.assertEqual(right_json, res)

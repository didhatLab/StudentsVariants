from typing import List
from flask import Flask, request
from src import bootstrap, commands
from src.serializer import Serializer
from src import domain

app = Flask(__name__)
command_handler = bootstrap.bootstrap()


@app.route("/api/students")
def students_list():
    students = command_handler.handle_command(commands.GetAllStudents())
    students = Serializer().list_serializer(students)
    response = app.response_class(
        response=students,
        status=200,
        mimetype="application/json",
    )
    return response


@app.route("/api/variants")
def variants_list():
    variants: List[domain.Variant] = command_handler.handle_command(commands.GetAllVariants())
    variants = Serializer().list_serializer(variants)
    response = app.response_class(
        response=variants,
        status=200,
        mimetype="application/json",
    )
    return response


@app.route("/api/get_students_variant/<string:work_name>")
def students_variants(work_name: str):
    works: List[domain.StudentWorkVariant] = \
        command_handler.handle_command(commands.GetWork(work_name=work_name))

    works = Serializer().list_serializer(works)
    response = app.response_class(
        response=works,
        status=200,
        mimetype="application/json"

    )
    return response


@app.route("/api/generate_work", methods=["POST"])
def generate_new_work():
    work_name = request.json.get("work_name")
    result = command_handler.handle_command(commands.GenerateWork(work_name=work_name))
    new_work = Serializer().list_serializer(result)
    response = app.response_class(
        response=new_work,
        status=201,
        mimetype="application/json"
    )
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0')

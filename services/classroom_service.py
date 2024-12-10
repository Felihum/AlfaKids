from flask import Request, jsonify
from db import database
from models.classroom.classroom_status import ClassroomStatus
from models.classroom.classroom import Classroom
from models.student.student import Student
from models.class_allocation.class_allocation import ClassAllocation


class ClassroomService:

    @staticmethod
    def initialize_classroom(request: Request):
        classroom_request = request.get_json()

        number: int = classroom_request["number"]
        status: str = ClassroomStatus.INITIALIZED.name
        year: int = classroom_request["year"]
        id_professor: int = classroom_request["id_professor"]

        if not number or not status or not year or not id_professor:
            return jsonify({"error": "Some field is missing!"}), 400

        print("Number: ", number,"\n",
              "Status: ", status, "\n",
              "Year: ", year, "\n",
              "Id_Professor: ", id_professor, "\n")

        classroom: Classroom = Classroom(number, year, status, id_professor)

        database.session.add(classroom)
        database.session.commit()

        return jsonify({"message": "Classroom initialized successfully!",
                        "classroom": classroom.to_dict()}), 201

    @staticmethod
    def allocate_student_in_classroom(request: Request):
        allocation_request = request.get_json()

        id_classroom: int = allocation_request["id_classroom"]
        id_student: int = allocation_request["id_student"]

        if not id_classroom or not id_student:
            return jsonify({"error": "Some field is missing!"}), 400

        classroom: Classroom = Classroom.query.get(id_classroom)
        student: Student = Student.query.get(id_student)

        existing_allocation = ClassAllocation.query.filter_by(id_student=id_student, id_classroom=id_classroom).first()

        if existing_allocation:
            return jsonify({"error": "Student already allocated in this classroom!"}), 500

        if classroom.status == ClassroomStatus.FULFILLED.name or classroom.status == ClassroomStatus.CLOSED.name:
            return jsonify({"error": "Classroom is not available!"}), 400

        if not student:
            return jsonify({"error": "Student not found!"}), 404

        if not classroom:
            return jsonify({"error": "Classroom not found!"}), 404

        allocation: ClassAllocation = ClassAllocation(id_student, id_classroom)

        database.session.add(allocation)
        database.session.commit()

        return jsonify({"message": "Allocation created successfully!",
                        "allocation": allocation.to_dict()}), 201

    @staticmethod
    def get_classroom_by_id(id_classroom: int):
        classroom: Classroom = Classroom.query.get(id_classroom)

        if not classroom:
            return jsonify({"error": "Classroom not found"}), 404

        return jsonify({"message": "Classroom found",
                        "classroom": classroom.to_dict()}), 200

    @staticmethod
    def get_classroom_by_number_and_year(number: int, year: int):
        classroom: Classroom = Classroom.query.filter_by(number=number, year=year).first()

        if not classroom:
            return jsonify({"error": "Classroom not found"}), 404

        return jsonify({"message": "Classroom found",
                        "classroom": classroom.to_dict()}), 200

    @staticmethod
    def get_classrooms_by_student_id(id_student: int):
        class_allocations = ClassAllocation.query.filter_by(id_student=id_student).all()
        classrooms = list()

        if not class_allocations:
            return jsonify({"error": "There are no classrooms!"}), 404

        for class_allocation in class_allocations:
            classrooms.append(Classroom.query.get(class_allocation.id_classroom))

        classrooms_dict_list = [classroom.to_dict() for classroom in classrooms]

        return jsonify({"message": "Classrooms found",
                        "classrooms": classrooms_dict_list}), 200

    @staticmethod
    def fulfill_classroom(id_classroom: int):
        classroom: Classroom = Classroom.query.get(id_classroom)

        if not classroom:
            return jsonify({"error": "Classroom not found"}), 404

        classroom.status = ClassroomStatus.FULFILLED.name

        database.session.commit()

        return jsonify({"message": "Classroom fulfilled successfully",
                        "classroom": classroom.to_dict()}), 200

    @staticmethod
    def close_classroom(id_classroom: int):
        classroom: Classroom = Classroom.query.get(id_classroom)

        if not classroom:
            return jsonify({"error": "Classroom not found"}), 404

        classroom.status = ClassroomStatus.CLOSED.name

        database.session.commit()

        return jsonify({"message": "Classroom closed successfully",
                        "classroom": classroom.to_dict()}), 200

    @staticmethod
    def update_classroom_professor(id_classroom: int, request: Request):
        classroom: Classroom = Classroom.query.get(id_classroom)

        if not classroom:
            return jsonify({"error": "Activity not found"}), 404

        id_professor: int = request.get_json()["id_professor"]

        if not id_professor:
            return jsonify({"error": "Some field is missing!"}), 400

        classroom.id_professor = id_professor

        database.session.commit()

        return jsonify({"message": "Classroom updated successfully",
                        "classroom": classroom.to_dict()}), 200

    @staticmethod
    def delete_classroom(id_classroom: int):
        classroom: Classroom = Classroom.query.get(id_classroom)

        if not classroom:
            return jsonify({"error": "Classroom not found"}), 404

        database.session.delete(classroom)
        database.session.commit()

        return jsonify({"message": "Classroom deleted successfully!"}), 200
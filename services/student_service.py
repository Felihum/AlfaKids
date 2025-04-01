import uuid

from flask import Request, jsonify
from models.student.student import Student
from db import database
from models.class_allocation.class_allocation import ClassAllocation
import bcrypt

class StudentService:
    @staticmethod
    def create_student(request: Request):
        request_student: Student = request.get_json()

        name: str = request_student["name"]
        email: str = request_student["email"]
        password: str = request_student["password"]
        age: int = request_student["age"]
        gender: str = request_student["gender"]
        # autism_level: int = request_student["autism_level"]
        school_year: int = request_student["school_year"]

        if not name or not email or not password or not age or not gender or not school_year:
            return jsonify({"error": "Some field(s) has no value."}), 400

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()) # Encripted Password

        new_student: Student = Student(name, email, hashed_password.decode('utf-8'), age, gender, school_year)
        database.session.add(new_student)
        database.session.commit()

        return jsonify({"message": "Student registered successfully!",
                        "student": new_student.to_dict()}), 201

    @staticmethod
    def get_all_students():
        students: Student = Student.query.all()

        if not students:
            return jsonify({"error": "There are no students."}), 404
        
        students_dict_list = [student.to_dict() for student in students]

        return jsonify({"message": "Students found",
                        "students": students_dict_list}), 200
    
    @staticmethod
    def get_student_by_id(id_student):
        student: Student = Student.query.get(id_student)

        if not student:
            return jsonify({"error": "Student not found"}), 404

        return jsonify({"message": "Student found",
                        "student": student.to_dict()}), 200

    @staticmethod
    def get_student_by_email(email):
        student: Student = Student.query.filter_by(email=email).first()

        if not student:
            return jsonify({"error": "Student not found"}), 404

        return jsonify({"message": "Student found",
                        "student": student.to_dict()}), 200

    @staticmethod
    def filter_students_by_email(email):
        students = Student.query.where(Student.email.contains(email)).all()

        if not students:
            return jsonify({"error": "There are no students."}), 404

        students_dict_list = [student.to_dict() for student in students]

        return jsonify({"message": "Students found",
                        "students": students_dict_list}), 200

    @staticmethod
    def get_students_by_classroom_id(id_classroom):
        class_allocations = ClassAllocation.query.filter_by(id_classroom=id_classroom).all()
        students = list()

        if not class_allocations:
            return jsonify({"message": "There are no students in this classroom!",
                            "students": []}), 200

        for class_allocation in class_allocations:
            students.append(Student.query.get(class_allocation.id_student))

        students_dict_list = [student.to_dict() for student in students]

        return jsonify({"message": "Students found",
                        "students": students_dict_list}), 200

    @staticmethod
    def update_student(id_student, request: Request):
        student: Student = Student.query.get(id_student)

        if not student:
            return jsonify({"error": "Student not found"}), 404

        request_student = request.get_json()

        name: str = request_student["name"]
        email: str = request_student["email"]
        password: str = request_student["password"]
        age: int = request_student["age"]
        gender: str = request_student["gender"]
        autism_level: int = request_student["autism_level"]
        school_year: int = request_student["school_year"]

        if not name or not email or not password or not age or not gender or not school_year:
            return jsonify({"error": "Some field(s) has no value."}), 400

        student.name = name
        student.email = email
        student.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode()
        student.age = age
        student.gender = gender
        # student.autism_level = autism_level
        student.school_year = school_year

        database.session.commit()

        return jsonify({"message": "Student updated successfully!",
                        "student": student.to_dict()}), 200

    @staticmethod
    def update_password(email, request: Request):
        student: Student = Student.query.filter_by(email=email).first()

        if not student:
            return jsonify({"error": "Student not found"}), 404

        request_student = request.get_json()

        password: str = request_student["password"]

        if not password:
            return jsonify({"error": "Some field(s) has no value."}), 400

        student.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode()

        database.session.commit()

        return jsonify({"message": "Password updated successfully!",
                        "student": student.to_dict()}), 200

    @staticmethod
    def delete_student(id_student):
        student: Student = Student.query.get(id_student)

        if not student:
            return jsonify({"error": "Student not found"}), 404

        database.session.delete(student)
        database.session.commit()

        return jsonify({"message": "Student deleted successfully!"}), 200

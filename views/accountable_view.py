from flask import Blueprint, request
from services.accountable_service import AccountableService

bp_accountable = Blueprint("accountable", __name__, url_prefix="/accountable")

__accountable_service = AccountableService()

@bp_accountable.route("/register", methods=["POST"])
def create_accountable():
    return __accountable_service.create_accountable(request)


@bp_accountable.route("/findById/<int:id_accountable>", methods=["GET"])
def get_accountable_by_id(id_accountable):
    return __accountable_service.get_accountable_by_id(id_accountable)


@bp_accountable.route("/findByEmail/<string:email>", methods=["GET"])
def get_accountable_by_email(email):
    return __accountable_service.get_accountable_by_email(email)


@bp_accountable.route("/findByStudentId/<int:id_student>", methods=["GET"])
def get_accountable_by_student_id(id_student):
    return __accountable_service.get_accountables_by_student_id(id_student)


@bp_accountable.route("/update/<int:id_accountable>", methods=["PUT"])
def update_accountable(id_accountable):
    return __accountable_service.update_accountable(id_accountable, request)


@bp_accountable.route("/delete/<int:id_accountable>", methods=["DELETE"])
def delete_accountable(id_accountable):
    return __accountable_service.delete_accountable(id_accountable)

from flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.teachers import Teacher
from core.apis.teachers.schema import TeacherSchema

principal_teacher_resources = Blueprint('principal_teacher_resources', __name__)


@principal_teacher_resources.route('/teachers', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_teachers(p):
    """Returns list of teachers"""
    principals_teachers = Teacher.get_all_teachers()
    principals_teachers_dump = TeacherSchema().dump(principals_teachers, many=True)
    return APIResponse.respond(data=principals_teachers_dump)

from flask import Blueprint

auth_bp = Blueprint('auth', __name__)
student_bp = Blueprint('student', __name__)
teacher_bp = Blueprint('teacher', __name__)
admin_bp = Blueprint('admin', __name__)
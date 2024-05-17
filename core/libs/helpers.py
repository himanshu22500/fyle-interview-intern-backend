import random
import string
from datetime import datetime
from core import db

TIMESTAMP_WITH_TIMEZONE_FORMAT = '%Y-%m-%dT%H:%M:%S.%f%z'


class GeneralObject:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


def get_utc_now():
    return datetime.utcnow()

def create_and_get_assignment_for_test(state):
    from core.models.assignments import Assignment

    assignment = Assignment()
    assignment.student_id = 1
    assignment.teacher_id = 1
    assignment.content = "test content"
    assignment.state = state

    db.session.add(assignment)
    db.session.commit()

    return assignment.id
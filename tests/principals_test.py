from core.libs.helpers import create_and_get_assignment_for_test
from core.models.assignments import AssignmentStateEnum, GradeEnum


def test_get_assignments(client, h_principal):
    response = client.get(
        '/principal/assignments',
        headers=h_principal
    )

    assert response.status_code == 200

    data = response.json['data']
    for assignment in data:
        assert assignment['state'] in [AssignmentStateEnum.SUBMITTED, AssignmentStateEnum.GRADED]


def test_grade_assignment_draft_assignment(client, h_principal):
    """
    failure case: If an assignment is in Draft state, it cannot be graded by principal
    """
    response = client.post(
        '/principal/assignments/grade',
        json={
            'id': create_and_get_assignment_for_test(state=AssignmentStateEnum.DRAFT),
            'grade': GradeEnum.A.value
        },
        headers=h_principal
    )

    assert response.status_code == 400


def test_grade_assignment(client, h_principal):
    response = client.post(
        '/principal/assignments/grade',
        json={
            'id': 4,
            'grade': GradeEnum.C.value
        },
        headers=h_principal
    )

    assert response.status_code == 200

    assert response.json['data']['state'] == AssignmentStateEnum.GRADED.value
    assert response.json['data']['grade'] == GradeEnum.C


def test_regrade_assignment(client, h_principal):
    response = client.post(
        '/principal/assignments/grade',
        json={
            'id': 4,
            'grade': GradeEnum.B.value
        },
        headers=h_principal
    )

    assert response.status_code == 200

    assert response.json['data']['state'] == AssignmentStateEnum.GRADED.value
    assert response.json['data']['grade'] == GradeEnum.B


def test_grade_assignment_unauthorized_access(client):
    response = client.post(
        '/principal/assignments/grade',
        json={
            'id': 1,
            'grade': 'A'
        }
    )

    # Check that the response has a status code of 401
    assert response.status_code == 401

def test_list_teachers(client, h_principal):
    # Send a request to list teachers
    response = client.get(
        '/principal/teachers',
        headers=h_principal
    )

    # Check that the response has a status code of 200
    assert response.status_code == 200

    # Check that the response contains a list of teachers
    data = response.json
    assert isinstance(data['data'], list)
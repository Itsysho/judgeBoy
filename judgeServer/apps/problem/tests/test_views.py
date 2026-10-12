import pytest
from rest_framework import status
from rest_framework.test import APIClient
from apps.problem.models import Problem
from apps.core.errors import ErrorStatus

LIST_URL = '/api/v1/problems/'
DETAIL_URL = '/api/v1/problems/:id/'

FAKE_PROBLEM = {
    "public_status": 0,
    # "time_stamp": null,
    "src": "Fake problem src",
    "title": "Fake problem title",
    "level": 1,
    # "post_order": null
}


@pytest.mark.django_db
def test_get_problem_list_succeeded():
    """
        Ensure we get problem list succeeded.
    """
    client = APIClient()

    problems = []
    for i in range(5):
        problems.append(
            Problem(**{**FAKE_PROBLEM, "title": f"Problem {i}"}))
    for i in range(5):
        problems.append(
            Problem(**{**FAKE_PROBLEM, "title": f"Problem {i + 5}", "public_status": 1}))
    Problem.objects.bulk_create(problems)

    response = client.get(LIST_URL)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data["results"]) == 5

    for data in response.data["results"]:
        assert "id" in data
        assert "src" not in data
        assert "title" in data
        assert "level" in data
        assert "time_stamp" in data


@pytest.mark.django_db
def test_get_problem_list_with_parameters_succeeded():
    """
        Ensure we get correct problem list with parameters.
    """
    client = APIClient()
    problems = []
    for i in range(5):
        problems.append(
            Problem(**{**FAKE_PROBLEM, "title": f"Problem {i}"}))
    for i in range(5):
        problems.append(
            Problem(**{**FAKE_PROBLEM, "title": f"Problem {i + 5}", "public_status": 1}))
    for i in range(5):
        problems.append(
            Problem(**{**FAKE_PROBLEM, "title": f"Problem {i + 10}", "public_status": 1, "level": 0}))
    Problem.objects.bulk_create(problems)

    response = client.get(LIST_URL + "?level=0")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data["results"]) == 5

    for data in response.data["results"]:
        assert "id" in data
        assert "title" in data
        assert "time_stamp" in data
        assert data["level"] == 0


@pytest.mark.django_db
def test_get_problem_detail_succeeded():
    """
        Ensure we get current problem succeeded.
    """
    client = APIClient()

    problem = Problem.objects.create(**{**FAKE_PROBLEM, "public_status": 1})
    url = DETAIL_URL.replace(":id", str(problem.id))
    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK

    assert "id" in response.data
    assert "title" in response.data
    assert "level" in response.data
    assert "src" in response.data
    assert "time_stamp" in response.data
    assert response.data["id"] == problem.id


@pytest.mark.django_db
def test_get_unpublicized_problem_detail_failed():
    """
        Ensure we couldn't get unpublicized problem.
    """
    client = APIClient()

    problem = Problem.objects.create(**{**FAKE_PROBLEM, "public_status": 0})
    url = DETAIL_URL.replace(":id", str(problem.id))
    response = client.get(url)

    assert response.status_code == ErrorStatus.NOT_FOUND.http_code

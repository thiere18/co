from jose import jwt
from app.config import schemas
from app.config.config import settings
import pytest
import os

base_api = "/api/v1"


def test_root(client):
    res = client.get("/")
    assert res.json().get("status") == "ok"
    assert res.status_code == 200


def test_create_user(client):
    os.system("make init_test")
    res = client.post(
        f"{base_api}/users/signup",
        json={
            "username": "thierno",
            "email": "thierno@gmail.com",
            "password": "thierno",
        },
    )
    new_user = schemas.UserOut(**res.json())
    assert new_user.username == "thierno"
    assert res.status_code == 201


def test_login_user(test_user, client):
    res = client.post(
        f"{base_api}/login",
        data={
            "username": test_user["email"],
            "password": test_user["password"],
        },  # noqa
    )
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(
        login_res.access_token,
        settings.secret_key,
        algorithms=[settings.algorithm],  # noqa
    )

    id = payload.get("user_id")
    assert id == test_user["id"]
    assert login_res.token_type == "bearer"
    assert res.status_code == 200


@pytest.mark.parametrize(
    "email, password, status_code",
    [
        ("user@exampld.com", "bearer", 403),
        (None, "bearer", 422),
        ("thiere", "thierno", 200),
    ],
)
def test_incorrect_user(test_user, client, email, password, status_code):
    res = client.post(
        f"{base_api}/login", data={"username": email, "password": password}
    )
    assert res.status_code == status_code


@pytest.mark.parametrize(
    "actual_password, new_password, status_code",
    [("worng_pass", "bearer", 403), ("thierno", "good_pass", 200)],
)
def test_correct_incorrect_user_reset(
    test_user, authorized_client, actual_password, new_password, status_code
):
    data = {"actual_password": actual_password, "new_password": new_password}
    res = authorized_client.put(f"{base_api}/users/{test_user['id']}", json=data)
    assert res.status_code == status_code


def test_unauthenticated_user_reset_password(client):
    data = {"actual_password": "howwwe", "new_password": "new_password"}
    res = client.put(f"{base_api}/users/1", json=data)
    assert res.status_code == 401
    assert res.json().get("detail") == "Not authenticated"

from apps.authentication.factories import UserFactory
from apps.core.factories import SnakeFactory
from apps.tournament.factories import TeamFactory

user_factory = UserFactory()
team_factory = TeamFactory()
snake_factory = SnakeFactory()


def test_index(client):
    user = user_factory.login_as(client)
    team_factory.basic(user=user)
    response = client.get("/team/")
    assert response.status_code == 200


def test_index_redirect(client):
    user_factory.login_as(client)
    response = client.get("/team/")
    assert response.status_code == 302


def test_create(client):
    # user = user_factory.login_as(client)
    response = client.post("/team/new/", {"name": "test2", "description": "test"})
    # assert response.status_code == 302
    # assert TeamMember.objects.get(user=user) is not None
    # Note: we've temporarily disabled the team creation endpoint
    assert response.status_code == 404


def test_edit(client):
    user = user_factory.login_as(client)
    team_factory.basic(user=user)
    response = client.get(f"/team/edit/")
    # assert response.status_code == 200
    # Note: we've temporarily disabled the team edit endpoint
    assert response.status_code == 404


def test_update(client):
    # user = user_factory.login_as(client)
    # team = team_factory.basic(user=user)
    response = client.post(
        f"/team/", {"name": "test3", "description": "test", "_method": "put"}
    )
    # assert response.status_code == 302
    # team.refresh_from_db()
    # assert team.name == "test3"
    # Note: we've temporarily disabled the team update endpoint
    assert response.status_code == 405

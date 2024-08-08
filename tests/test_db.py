from sqlalchemy import select
from sqlalchemy.orm import Session

from madr.models import User


def test_create_user(session: Session):
    user = User(username="test", email="test@mail.com", password="secret")
    session.add(user)
    session.commit()
    session.refresh(user)
    result = session.scalar(
        select(User).where(User.email == "test@mail.com")
    )
    assert result.id == 1
    assert result.username == "test"
    assert result.password == "secret"
    # TODO: validar que foi armazenado o hash da password

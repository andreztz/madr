from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column, registry
from sqlalchemy.sql import func

table_registry = registry()
# TODO: publisher, subjects, description?


@table_registry.mapped_as_dataclass
class User:
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now(), onupdate=func.now()
    )


# @table_registry.mapped_as_dataclass
# class Book:
#     __tablename__ = "books"
#     id: Mapped[int] = mapped_column(init=False, primary_key=True, index=True)
#     title: Mapped[str] = mapped_column(index=True)
#     year: Mapped[str] = mapped_column(index=True)
#
#     created_at: Mapped[datetime] = mapped_column(
#         init=False, server_default=func.now()
#     )
#     updated_at: Mapped[datetime] = mapped_column(
#         init=False, server_default=func.now(), onupdate=func.now()
#     )
#     author: Mapped["Author"] = relationship(init=False, back_populates="books")
#
#
# @table_registry.mapped_as_dataclass
# class Author:
#     __tablename__ = "authors"
#     id: Mapped[int] = mapped_column(init=False, primary_key=True, index=True)
#     name: Mapped[str] = mapped_column(index=True)
#
#     created_at: Mapped[datetime] = mapped_column(
#         init=False, server_default=func.now()
#     )
#     updated_at: Mapped[datetime] = mapped_column(
#         init=False, server_default=func.now(), onupdate=func.now()
#     )
#     books: Mapped[list["Book"]] = relationship(
#         init=False, back_populates="author", cascade="all, delete-orphan"
#     )

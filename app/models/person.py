# -*- coding: utf-8 -*-
"""
models.py auto-generated thanks to sqlacodegen (https://github.com/agronholm/sqlacodegen/tree/master)

Command
sqlacodegen postgresql://postgres:<your-password-here>@localhost:5432/test --tables item,person,comment
--generator declarative --outfile models.py
"""

# --- Python modules ---
# datetime: provides classes for simple and complex date and time manipulation.
import datetime
# typing: provides runtime support for type hints
from typing import List, Optional

# --- Third Party Libraries ---
# sqlalchemy: SQL and ORM toolkit for accessing relational databases.
from sqlalchemy import DateTime, Identity, Integer, PrimaryKeyConstraint, String, \
    UniqueConstraint, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

# --- App modules ---
from app.pg_base import Base


class Person(Base):
    __tablename__ = 'person'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='person_pkey'),
        UniqueConstraint('email', name='person_email_unique'),
        {'comment': 'People', 'extend_existing': True},
    )

    id: Mapped[int] = mapped_column(Integer,
                                    Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647,
                                             cycle=False, cache=1),
                                    primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(50))
    created_by: Mapped[Optional[str]] = mapped_column(String(100))
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('now()'))
    updated_by: Mapped[Optional[str]] = mapped_column(String(100))
    updated_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)

    comment: Mapped[List['Comment']] = relationship('Comment', back_populates='person')

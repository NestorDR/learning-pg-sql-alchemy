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
from typing import Optional

# --- Third Party Libraries ---
# sqlalchemy: SQL and ORM toolkit for accessing relational databases.
from sqlalchemy import DateTime, ForeignKeyConstraint, Identity, Integer, PrimaryKeyConstraint, String, \
    text
from sqlalchemy.orm import Mapped, mapped_column, relationship

# --- App modules ---
from app.pg_base import Base


class Comment(Base):
    __tablename__ = 'comment'
    __table_args__ = (
        ForeignKeyConstraint(['item_id'], ['item.id'], name='comment_item_fkey'),
        ForeignKeyConstraint(['person_id'], ['person.id'], name='comment_person_fkey'),
        PrimaryKeyConstraint('id', name='comment_pkey'),
        {'comment': 'Comments on the items made by the people', 'extend_existing': True},
    )

    id: Mapped[int] = mapped_column(Integer,
                                    Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647,
                                             cycle=False, cache=1),
                                    primary_key=True)
    person_id: Mapped[int] = mapped_column(Integer)
    item_id: Mapped[int] = mapped_column(Integer)
    comment: Mapped[str] = mapped_column(String(10485760))
    created_by: Mapped[Optional[str]] = mapped_column(String(100))
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('now()'))
    updated_by: Mapped[Optional[str]] = mapped_column(String(100))
    updated_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)

    item: Mapped['Item'] = relationship('Item', back_populates='comment')
    person: Mapped['Person'] = relationship('Person', back_populates='comment')

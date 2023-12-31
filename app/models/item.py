# -*- coding: utf-8 -*-
"""
models auto-generated thanks to sqlacodegen (https://github.com/agronholm/sqlacodegen/tree/master)

Command
sqlacodegen postgresql://postgres:<your-password-here>@localhost:5432/test --tables item,person,comment
--generator declarative --outfile models.py
"""

# --- Python modules ---
# datetime: provides classes for simple and complex date and time manipulation.
import datetime
# typing: provides runtime support for type hints
from typing import Any, List, Optional

# --- Third Party Libraries ---
# sqlalchemy: SQL and ORM toolkit for accessing relational databases.
from sqlalchemy import DateTime, Float,  Identity, Integer, PrimaryKeyConstraint, String, \
    UniqueConstraint, text
from sqlalchemy.dialects.postgresql import MONEY
from sqlalchemy.orm import Mapped, mapped_column, relationship

# --- App modules ---
from app.pg_base import Base


class Item(Base):
    __tablename__ = 'item'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='item_pkey'),
        UniqueConstraint('name', name='item_name_unique'),
        {'comment': 'Generic items', 'extend_existing': True},
    )

    id: Mapped[int] = mapped_column(Integer,
                                    Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647,
                                             cycle=False, cache=1),
                                    primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    position: Mapped[int] = mapped_column(Integer)
    price: Mapped[Any] = mapped_column(MONEY)
    amount: Mapped[Optional[float]] = mapped_column(Float)
    created_by: Mapped[Optional[str]] = mapped_column(String(100))
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('now()'))
    updated_by: Mapped[Optional[str]] = mapped_column(String(100))
    updated_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)

    comment: Mapped[List['Comment']] = relationship('Comment', back_populates='item')

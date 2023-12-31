# -*- coding: utf-8 -*-

# --- Python modules ---
# os: allows access to functionalities dependent on the Operating System
from os import environ
# urllib: collects several modules for working with URLs
from urllib import parse

# --- Third Party Libraries ---
# sqlalchemy: SQL and ORM toolkit for accessing relational databases.
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


class Base(DeclarativeBase):
    pass


# Configure PostgreSQL Database Connection String
# Visit https://www.postgresql.org/docs/16/libpq-envars.html
host_server = environ.get('PGHOST', 'localhost')
db_server_port = parse.quote_plus(str(environ.get('PGPORT', '5432')))
database_name = environ.get('PGDATABASE', 'test')
db_username = parse.quote_plus(str(environ.get('PGUSER', 'postgres')))
db_password = parse.quote_plus(str(environ.get('PGPASSWORD', 'password')))
ssl_mode = parse.quote_plus(str(environ.get('PGSSLMODE', 'prefer')))
database_url = \
    f'postgresql://{db_username}:{db_password}@{host_server}:{db_server_port}/{database_name}?sslmode={ssl_mode}'

# Visit https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/#SQLAlchemy-Introduction
engine = create_engine(database_url)

"""
SQLAlchemy ORM uses Sessions to implement the Unit of Work design pattern. As explained by Martin Fowler, a Unit of Work
 is used to maintain a list of objects affected by a business transaction and to coordinate the writing out of changes.
This means that all modifications tracked by Sessions (Units of Works) will be applied to the underlying database 
 together, or none of them will. In other words, Sessions are used to guarantee the database consistency.
"""
# Use session_factory() to get a new Session
_SessionFactory = sessionmaker(bind=engine)


def session_factory():
    Base.metadata.create_all(engine)
    return _SessionFactory()

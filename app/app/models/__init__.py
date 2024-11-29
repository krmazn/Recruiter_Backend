"""
Adds support for alembic's migrations autogenrate feature.
"""
# ruff: noqa: F401
from .base import Base
# Import your models here
from .sqlalchemy_model import ScreeningRequest



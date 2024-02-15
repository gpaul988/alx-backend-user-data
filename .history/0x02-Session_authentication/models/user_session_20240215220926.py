#!/usr/bin/env python3
# Graham S. Paul - user-session.py
"""Module for User session.
"""
from models.base import Base


class UserSession(Base):
    """Class for user session.
    """

    def __init__(self, *args: list, **kwargs: dict):
        """Boots User session instance.
        """
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')

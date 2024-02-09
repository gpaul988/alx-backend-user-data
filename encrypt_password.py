#!/usr/bin/env python3
# Graham S. Paul - encrypt_password.py
"""encrypting password module.
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Hashes password using a random salt.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Checks hashed password was formed from the given password.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
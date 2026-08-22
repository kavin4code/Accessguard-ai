"""
app/security/password.py

Password hashing utilities for AccessGuard AI.

Exposes two public functions:
    hash_password(password: str) -> str
    verify_password(password: str, password_hash: str) -> bool

The PasswordHash instance is intentionally private.
No other module should interact with pwdlib directly.
"""

from pwdlib import PasswordHash

# Private hasher instance configured with pwdlib's recommended defaults.
# PasswordHash.recommended() selects the best available algorithm
# (Argon2) with production-safe parameters.
_password_hasher = PasswordHash.recommended()


def hash_password(password: str) -> str:
    """
    Hash a plaintext password using the recommended algorithm.

    Returns a self-contained hash string that includes the algorithm,
    parameters, salt, and digest. Store this value in the database —
    never store the plaintext password.
    """
    return _password_hasher.hash(password)


def verify_password(password: str, password_hash: str) -> bool:
    """
    Verify a plaintext password against a stored hash.

    Returns True if the password matches, False otherwise.
    An incorrect password is an expected input — pwdlib returns False
    for a non-matching password without raising an exception.
    """
    return _password_hasher.verify(password, password_hash)

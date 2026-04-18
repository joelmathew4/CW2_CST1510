import bcrypt

def generate_hash(password: str) -> str:
    """Generate a hashed password."""
    password_bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)
    return hashed.decode("utf-8")


def is_valid_hash(password: str, hashed_password: str) -> bool:
    """Check if the password matches the stored hash."""
    password_bytes = password.encode("utf-8")
    hashed_bytes = hashed_password.encode("utf-8")
    return bcrypt.checkpw(password_bytes, hashed_bytes)

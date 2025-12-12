import os
from typing import Optional

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer


BETTER_AUTH_SECRET = os.getenv("BETTER_AUTH_SECRET")
ALGORITHMS = ["HS256"]
bearer_scheme = HTTPBearer(auto_error=False)


def decode_jwt(token: str) -> Optional[dict]:
    try:
        return jwt.decode(token, BETTER_AUTH_SECRET, algorithms=ALGORITHMS)
    except jwt.PyJWTError:
        return None


async def get_current_user_id(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
) -> str:
    if credentials is None or credentials.scheme.lower() != "bearer":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authorization header missing or invalid",
        )

    payload = decode_jwt(credentials.credentials)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
        )

    user_id = payload.get("user_id") or payload.get("sub")
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token payload"
        )

    return str(user_id)

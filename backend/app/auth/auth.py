from fastapi import Depends, HTTPException
from jose import jwt, JWTError

from app.auth.security import (
    SECRET_KEY,
    ALGORITHM,
    oauth2_scheme,
)
from fastapi import Depends, HTTPException
from jose import jwt, JWTError

from app.auth.security import (
    SECRET_KEY,
    ALGORITHM,
    oauth2_scheme,
)
from app.models.company import Company

from sqlalchemy.orm import Session

from app.auth.models import User

from app.auth.security import (
    hash_password,
    verify_password,
)


def create_user(db, full_name, company_name, email, password):

    company = db.query(Company).filter(
        Company.name == company_name
    ).first()

    if not company:

        company = Company(
            name=company_name
        )

        db.add(company)

        db.commit()

        db.refresh(company)

    user = User(
        full_name=full_name,
        email=email,
        password=hash_password(password),
        company_id=company.id,
    )

    db.add(user)

    db.commit()

    db.refresh(user)

    return user
def authenticate_user(db: Session, email, password):

    user = db.query(User).filter(
        User.email == email
    ).first()

    if not user:
        return None

    if not verify_password(
        password,
        user.password,
    ):
        return None

    return user
def get_current_user(
    token: str = Depends(oauth2_scheme),
):

    from app.db.database import SessionLocal

    db = SessionLocal()

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM],
        )

        email = payload.get("sub")

        if email is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

        user = (
            db.query(User)
            .filter(User.email == email)
            .first()
        )

        if user is None:
            raise HTTPException(
                status_code=401,
                detail="User not found"
            )

        return user

    except JWTError:

        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    finally:

        db.close()
def get_current_user(
    token: str = Depends(oauth2_scheme),
):

    from app.db.database import SessionLocal

    db = SessionLocal()

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM],
        )

        email = payload.get("sub")

        if email is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid token",
            )

        user = (
            db.query(User)
            .filter(User.email == email)
            .first()
        )

        if user is None:
            raise HTTPException(
                status_code=401,
                detail="User not found",
            )

        return user

    except JWTError:

        raise HTTPException(
            status_code=401,
            detail="Invalid token",
        )

    finally:

        db.close()

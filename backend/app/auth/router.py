from fastapi import HTTPException

from fastapi.security import OAuth2PasswordRequestForm

from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.db.database import get_db

from app.auth.schemas import UserRegister, UserLogin

from app.auth.auth import create_user, authenticate_user

from app.auth.security import create_access_token


router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register")
def register(user: UserRegister, db: Session = Depends(get_db)):

    create_user(
        db,
        user.full_name,
        user.company_name,
        user.email,
        user.password,
    )

    return {
        "message": "User created successfully"
    }
@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):

    db_user = authenticate_user(
        db,
        form_data.username,   # اینجا username همان ایمیل است
        form_data.password,
    )

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password",
        )

    token = create_access_token(
        {
            "sub": db_user.email
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer",
    }


from sqlalchemy import Column, Integer, String

from app.db.database import Base


class Company(Base):

    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, unique=True)

    description = Column(String, nullable=True)

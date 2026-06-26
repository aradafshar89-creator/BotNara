from sqlalchemy import Column, Integer, Float, String, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class Upload(Base):
    __tablename__ = "uploads"

    id = Column(Integer, primary_key=True, index=True)

    filename = Column(String)
    upload_date = Column(DateTime, default=datetime.utcnow)

    total_sales = Column(Float)
    total_orders = Column(Integer)

    top_customer = Column(String)
    top_product = Column(String)

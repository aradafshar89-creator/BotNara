from sqlalchemy import Column, Integer, Float, String, Date
from app.models.upload import Base


class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)

    customer = Column(String)

    product = Column(String)

    quantity = Column(Integer, default=1)

    sale_amount = Column(Float)

    purchase_price = Column(Float, default=0)

    profit = Column(Float, default=0)

    city = Column(String, nullable=True)

    salesperson = Column(String, nullable=True)

    sale_date = Column(Date, nullable=True)

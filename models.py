from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from database import Base 

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String, index=True)
    product_description = Column(String)

    capital_price = Column(Integer, default=0)
    selling_price = Column(Integer, default=0)

    status = Column(String, default="SUCCESS")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
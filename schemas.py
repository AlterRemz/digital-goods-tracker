from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# 1. skema dasar yang berisi atribut umum
class TransactionBase(BaseModel):
    customer_name: str
    product_description: str
    capital_price: int
    selling_price: int
    status: Optional[str] = "SUCCESS"

# 2. skema untuk menerima input saat mencatat transaksi baru
class TransactionCreate(TransactionBase):
    pass 

# 3. skema untuk mereturn data
class TransactionRespone(TransactionBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True # agar pydantic bisa membaca object SQLAlchemy dari database
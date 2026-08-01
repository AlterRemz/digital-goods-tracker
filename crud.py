from sqlalchemy.orm import Session
import models, schemas

# 1. fungsi untuk mencatat transaksi baru (CREATE)
def create_transaction(db: Session, transaction: schemas.TransactionCreate):
    db_transaction = models.Transaction(
        customer_name=transaction.customer_name,
        product_description=transaction.product_description,
        capital_price=transaction.capital_price,
        selling_price=transaction.selling_price,
        status=transaction.status
    )

    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)

    return db_transaction

# 2. fungsi untuk melihat riwayat transaksi (READ)
def get_transactions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Transaction).offset(skip).limit(limit).all()
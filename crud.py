from sqlalchemy.orm import Session
from sqlalchemy import func
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

# 3. fungsi untuk menghitung total profit (READ)
def get_total_profit(db: Session):
    # menghitung total dari: (selling_price - capital_price)
    # HANYA untuk transaksi yang berstatus "SUCCESS"
    profit = db.query(
        func.sum(models.Transaction.selling_price - models.Transaction.capital_price)
    ).filter(models.Transaction.status == "SUCCESS").scalar()

    return profit or 0

# 4. fungsi untuk mengubah data transaksi (UPDATE)
def update_transaction(db: Session, transaction_id: int, transaction_update: schemas.TransactionUpdate):
    db_transaction = db.query(models.Transaction).filter(models.Transaction.id == transaction_id).first()

    if db_transaction:
        if transaction_update.status is not None:
            db_transaction.status = transaction_update.status
            
        if transaction_update.capital_price is not None:
            db_transaction.capital_price = transaction_update.capital_price

        if transaction_update.selling_price is not None:
            db_transaction.selling_price = transaction_update.selling_price

        if transaction_update.product_description is not None:
            db_transaction.product_description = transaction_update.product_description

        if transaction_update.customer_name is not None:
            db_transaction.customer_name = transaction_update.customer_name

        db.commit()
        db.refresh(db_transaction)

    return db_transaction

# 5. fungsi untuk menghapus transaksi (DELETE)
def delete_transaction(db: Session, transaction_id: int):
    db_transaction = db.query(models.Transaction).filter(models.Transaction.id == transaction_id).first()

    if db_transaction:
        db.delete(db_transaction)
        db.commit()

    return db_transaction
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schemas, database

router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"]
)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint 1: Mencatat Transaksi Baru
@router.post("/", response_model=schemas.TransactionRespone)
def create_transaction(transaction: schemas.TransactionCreate, db: Session = Depends(get_db)):
    return crud.create_transaction(db=db, transaction=transaction)

# Endpoint 2: Melihat Riwayat Transaksi
@router.get("/", response_model=list[schemas.TransactionRespone])
def read_transaction(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_transactions(db=db, skip=skip, limit=limit)

# Endpoint 3: Mengubah Data Transaksi
@router.put("/{transaction_id}", response_model=schemas.TransactionRespone)
def update_transaction(transaction_id: int, transaction_update: schemas.TransactionUpdate, db: Session = Depends(get_db)):
    db_transaction = crud.update_transaction(db=db, transaction_id=transaction_id, transaction_update=transaction_update)

    if db_transaction is None:
        raise HTTPException(status_code=404, detail="Transaksi tidak ditemukan")

    return db_transaction

# Endpoint 4: Menghapus Data Transaksi
@router.delete("/{transaction_id}")
def delete_transaction(transaction_id: int, db: Session = Depends(get_db)):
    db_transaction = crud.delete_transaction(db=db, transaction_id=transaction_id)

    if db_transaction is None:
        raise HTTPException(status_code=404, detail="Transaksi tidak ditemukan")

    return {"pesan": f"Transaksi dengan ID {transaction_id} berhasil dihapus"}
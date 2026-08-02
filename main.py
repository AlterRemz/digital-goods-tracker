from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="NexusLedger")

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint 1: Mencatat Transaksi Baru
@app.post("/transactions/", response_model=schemas.TransactionRespone)
def create_transaction(transaction: schemas.TransactionCreate, db: Session = Depends(get_db)):
    return crud.create_transaction(db=db, transaction=transaction)

# Endpoint 2: Melihat Riwayat Transaksi
@app.get("/transactions/", response_model=list[schemas.TransactionRespone])
def read_transaction(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_transactions(db=db, skip=skip, limit=limit)

# Endpoint 3: Melihat Total Profit
@app.get("/profit/")
def get_profit(db: Session = Depends(get_db)):
    total_profit = crud.get_total_profit(db=db)
    return {
        "pesan": "Ini total keuangan bersihmu sejauh ini",
        "total_profit": total_profit,
        "mata_uang": "IDR"
    }

# Endpoint 4: Mengubah Data Transaksi
@app.put("/transactions/{transaction_id}", response_model=schemas.TransactionRespone)
def update_transaction(transaction_id: int, transaction_update: schemas.TransactionUpdate, db: Session = Depends(get_db)):
    db_transaction = crud.update_transaction(db=db, transaction_id=transaction_id, transaction_update=transaction_update)

    if db_transaction is None:
        raise HTTPException(status_code=404, detail="Transaksi tidak ditemukan")

    return db_transaction

# Endpoint 5: Menghapus Data Transaksi
@app.delete("/transaction/{transaction_id}")
def delete_transaction(transaction_id: int, db: Session = Depends(get_db)):
    db_transaction = crud.delete_transaction(db=db, transaction_id=transaction_id)

    if db_transaction is None:
        raise HTTPException(status_code=404, detail="Transaksi tidak ditemukan")

    return {"pesan": f"Transaksi dengan ID {transaction_id} berhasil dihapus"}
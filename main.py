from fastapi import FastAPI, Depends
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
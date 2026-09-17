from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas, database
import transaction

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="NexusLedger")

app.include_router(transaction.router)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint 1: Melihat Total Profit
@app.get("/profit/")
def get_profit(db: Session = Depends(get_db)):
    total_profit = crud.get_total_profit(db=db)
    return {
        "pesan": "Ini total keuangan bersihmu sejauh ini",
        "total_profit": total_profit,
        "mata_uang": "IDR"
    }
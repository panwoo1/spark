from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from database import SessionLocal, engine
from models import Base, Charger

app = FastAPI()

# Create the tables in the database
Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/chargers/")
def read_chargers(db: Session = Depends(get_db)):
    chargers = db.query(Charger).all()
    return [
        {
            "station_charger_id": charger.station_charger_id,
            "address": charger.address,
            "lat": charger.lat,
            "lng": charger.lng,
            "occupancy_rate": charger.occupancy_rate,
            "charging_rate": charger.charging_rate,
        }
        for charger in chargers
    ]

from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Charger(Base):
    __tablename__ = "charger"
    station_charger_id = Column(String, primary_key=True)
    lat = Column(Float)
    lng = Column(Float)
    address = Column(String)
    zscode = Column(String)
    kind_detail = Column(String)
    year_month = Column(String, primary_key=True)
    occupancy_rate = Column(Float)
    charging_rate = Column(Float)

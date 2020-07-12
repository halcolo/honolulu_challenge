"""This module implements the models mapped from the Database as objects.
"""

from sqlalchemy import Column, Integer, TEXT, Float
from honolulu.db import db_connection


base = db_connection()[0]


class Measurement(base):
    __tablename__ = "measurement"

    id = Column(Integer, nullable=False, primary_key=True)
    station = Column(TEXT)
    date = Column(TEXT)
    prcp = Column(Float)
    tobs = Column(Float)

    def __init__(self, station, date, prcp, tobs):
        self.station = station
        self.date = date
        self.prcp = prcp
        self.tobs = tobs

    def __repr__(self):
        return (f'Measurement({self.station}, {self.date} ' 
                f'{self.prcp}, {self.tobs})')


class Station(base):
    __tablename__ = "station"

    id = Column(Integer, nullable=False, primary_key=True)
    station = Column(TEXT)
    name = Column(TEXT)
    latitude = Column(Float)
    longitude = Column(Float)
    elevation = Column(Float)

    def __init__(self, station, name, latitude,
                 longitude, elevation):
        self.station = station
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.elevation = elevation

    def __repr__(self):
        return (f'Measurement({self.station}, {self.date} ' 
                f'{self.prcp}, {self.tobs})')


base.prepare(db_connection()[2], reflect=True)

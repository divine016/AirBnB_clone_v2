#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, Float, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ 
        This is the class for Place
            Attributes:
            city_id: city id
            user_id: user id
            name: name 
            description: string of description
            number_rooms: number of room in integer
            number_bathrooms: number of bathrooms in integer
            max_guest: maximum guest in integer
            price_by_night:: pice for a staying in integer
            latitude: latitude in flaot
            longitude: longitude in float
     """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Integer, nullable=True)
    amenity_ids = []
    reviews = relationship("Review", cascade='all, delete, delete-orphan', 
                           backref="place")

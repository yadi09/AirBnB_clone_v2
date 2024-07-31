#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
import os


place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column(
        'place_id',
        String(60),
        ForeignKey('places.id'),
        primary_key=True
    ),

    Column(
        'amenity_id',
        String(60),
        ForeignKey('amenities.id'),
        primary_key=True
    )
)


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship(
            'Review',
            cascade="all, delete, delete-orphan",
            backref='place'
        )

        amenities = relationship(
            'Amenity',
            secondary=place_amenity,
            viewonly=False,
            backref='place_amenities'
        )
    else:
        @property
        def reviews(self):
            """returns the list of Review instances"""
            from models import storage
            review_lists = []
            for v in storage.all(Review).values():
                if v.place_id == self.id:
                    review_list.append(v)
            return review_list

        @property
        def amenities(self):
            from models import storage
            amenities_lists = []
            for v in storage.all(Amenity).values():
                if v.id in self.amenity_ids:
                    amenities_lists.append(v)
            return amenities_lists

        @amenities.setter
        def amenities(self, val):
            if type(val) is Amenity:
                if val.id not in self.amenity_ids:
                    self.amenity_ids.append(val.id)

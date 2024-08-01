#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(
            String(128),
            nullable=False
        )
        cities = relationship(
            'City',
            backref='states',
            cascade='all, delete-orphan'
        )
    else:
        name = ''

        @property
        def cities(self):
            """Getter attribute to return a list of City instances"""
            from models import storage
            from models.city import City
            city_list = storage.all(City)
            city_list = storage.all(City)
            filter_by_id = [city for city in city_list.values()
                            if city.state_id == self.id]
            return filter_by_id

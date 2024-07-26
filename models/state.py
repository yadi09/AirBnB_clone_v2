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
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade='all, delete-orphan')
    else:
        name = ''

        @property
        def cities(self):
            """Getter attribute to return a list of City instances"""
            from models import storage
            city_list = storage.all(City)
            filter_by_id = []
            for key, value in city_list.items():
                if key.split('.')[1] == self.id:
                    filter_by_id.append(value)
                return filter_by_id

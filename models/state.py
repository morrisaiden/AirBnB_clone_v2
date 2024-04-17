#!/usr/bin/python3
""" State Module for HBNB project """

import models
from models.city import City
from models import storage
from sqlalchemy.orm import relationship
import sqlalchemy
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from os import getenv


class State(BasseModel, Base):
    """ State class """
    __tablename__ = 'states'

    if getenv('HBNB_TYPE_STORAGE' == 'db':
            name = Column(String(128), nullable=False)
            cities = relationship('City', cascade='all, delete', backref='state')
    else:
        """
        Storage relationship
        """

        @property
        def cities(self):
            city_list = []
            city_dit = storage.all(City)

        for ciy in city_dic.values():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list

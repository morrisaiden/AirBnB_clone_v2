#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from models.place import place
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey



class City(BaseModel):
    """ The city class, contains state ID and name """

    __tablename__ = "cities"
    name = Column(String(128), nullable=False) 
    state_id = Column(String(60), ForeighKey('state.id'), nullable=False)
    place = relationship("pace", cascade='all, delete, delete-orphan', backref="cities")

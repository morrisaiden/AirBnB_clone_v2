#!/usr/bin/python3

from os import getenv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from sqlalchemy.ext.declarative import declarative_base
from models.user import User
from models.city import City
from models.state import State
from models.base_model import Base
from models.amenity import Amenity
from models.review import Review
from models.amenity import Amenity

class DBStorage:
    """
    table environments"""
    __engine = None
    __session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                user, passwd, host, db, pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        dict = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            
            for comp in query:
                key = "{}.{}".format(type(comp).__name__, comp.id)
                dict[key] = comp
        else:
            arra = [State, City, User, Place, Review, Amenity]
            for elem in arr:
                query = self.__session.querry(elem)
                for comp in querry:
                    key = "{}.{}".format(type(comp).__name__, comp.id)
        return(dict)

    def new(self, obj):

        self.__session.add(obj)

    def save(self):

        self.__session.commit()

    def delete(self, obj=None):

        if obj:
            self.session.delete(obj)

    def reload(self):

        Base.metadata.create_all(self.__engine)
        sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sec)
        self.__session = Session()

    def close(self):

        self.__session.close()    

#!/usr/bin/python3
"New engine DBStorage"
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        env = os.getenv('HBNB_ENV')
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db_name = os.getenv('HBNB_MYSQL_DB')
        storage = os.getenv('HBNB_TYPE_STORAGE')
        db_url = "mysql+mysqldb://{}:{}@{}:3306/{}".format(
                user, pwd, host, db_name
            )

        self.__engine = create_engine(db_url, pool_pre_ping=True)

        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        "query on the current database session"
        objs = {}
        all_cls = (State, City)
        if cls is None:
            for cls_type in all_cls:
                query = self.__session.query(cls_type)
                for obj in query.all():
                    obj_key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                    objs[obj_key] = obj
        else:
            query = self.__session.query(cls)
            for obj in query.all():
                obj_key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                objs[obj_key] = obj
        return objs

    def new(self, obj):
        "add the object to the current database session"
        self.__session.add(obj)

    def save(self):
        "commit all changes of the current database session"
        self.__session.commit()

    def delete(self, obj=None):
        "delete from the current database session obj if not None"
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        "create all tables in the database"
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = scoped_session(Session)

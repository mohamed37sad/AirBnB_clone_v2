#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, DateTime, Column
import models


Base = declarative_base()
timeFormat = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Initialises data """
        updatedAtSet = createdAtSet = False
        if kwargs:
            for key, value in kwargs.items():
                if hasattr(self, "created_at") and\
                   type(self.created_at) is str:
                    self.created_at = datetime.\
                        strptime(kwargs["created_at"], timeFormat)
                    createdAtSet = True
                if hasattr(self, "updated_at") and\
                   type(self.updated_at) is str:
                    self.updated_at = datetime.\
                        strptime(kwargs["updated_at"], timeFormat)
                    updatedAtSet = True
                if key != "__class__":
                    setattr(self, key, value)
        self.id = str(uuid.uuid4())
        if not createdAtSet:
            self.created_at = datetime.now()
        if not updatedAtSet:
            self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the instance"""
        return ("[{}] ({}) {}".
                format(self.__class__.__name__,
                       self.id,
                       self.__dict__))

    def save(self):
        """Updates updated_at with current time when instance is changed
        and create new sotrage engine obj and save it in storage"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' in dictionary:
            del dictionary["_sa_instance_state"]
        return dictionary

    def delete(self):
        """ Delete the current instance from the storage """
        models.storage.delete(self)

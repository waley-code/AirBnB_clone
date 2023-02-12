#!/usr/bin/python3
"""
This is the base_model module which contains the class BaseModel
"""
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """
    This defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Instantiates Objet with id, created_at, updated_at atr
        """
        if kwargs:
            # use kwargs to create instance if it's not empty
            kwargs_copy = kwargs.copy()
            del kwargs_copy['__class__']
            for key, value in kwargs_copy.items():
                if key in ['created_at', 'updated_at']:
                    value = datetime.fromisoformat(value)
                    kwargs_copy.update({key: value})
                setattr(self, key, value)
        else:
            # creates instances if kwargs is empty
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        print: [<class name>] (<self.id>) <self.__dict__>
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        updates updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        returns a dictionary of the object instance
        """
        new_dic = {
            i: (j.isoformat() if i in ["created_at", "updated_at"] else j)
            for i, j in self.__dict__.items()
            if not i.startswith("__")
        }
        new_dic['__class__'] = self.__class__.__name__
        return new_dic

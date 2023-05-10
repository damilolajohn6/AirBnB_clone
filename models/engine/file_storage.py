#!/usr/bin/python3
"""Module for FileStorage class."""
import datetime
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:

    """Class for serializtion and deserialization of base classes."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns a copy of the dictionary that represents the storage's content."""
        return self.__objects.copy()

    def new(self, obj):
        """Saves obj in __objects dictionary."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save (self):
        """Serializes __objects to JSON file."""
        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as file:
            json_data = {key: val.to_dict() for key, val in FileStorage.__objects.items()}
            json.dump(json_data, file)

    def classes(self):
        """Returns a dictionary of valid classes and thier referencess"""
        classes = {"BAseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes

    def reload(self):
        """Deserializes JSON file into __objects."""
        """ check if the file path exists before proceeding"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        # TODO:  open the file and load its contents to the obj_dict
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
        # TODO: recreate the objects based on their class type
        for k, v in obj_dict.items():
            class_name = v.get("__class__")
            if class_name in self.classes():
                obj_dict[k] = self.classes()[class_name](**v)
            else:
                # raise an error if the class is not registered in classes
                raise ValueError("Unknown class: {}".format(class_name))
        FileStorage.__objects = obj_dict

    def attributes() -> dict:
        attributes = {
            "BaseModel": {
                "id": str,
                "created_at": datetime.datetime,
                "updated_at": datetime.datetime
            },
            "User": {
                "email": str,
                "password": str,
                "first_name": str,
                "last_name": str
            },
            "State": {
                "name": str
            },
            "City": {
                "state_id": str,
                "name": str
            },
            "Amenity": {
                "name": str
            },
            "Place": {
                "city_id": str,
                "user_id": str,
                "name": str
                "description": str,
                "number_rooms": int,
                "number_bathrooms": int,
                "max_guest": int,
                "price_by_night": int,
                "latitude": float,
                "longitude": float,
                "amenity_ids": list
            },
            "Review": {
                "place_id": str,
                "user_id": str,
                "text": str
            }
        }
        return attributes
